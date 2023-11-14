"""
This module contains Python wrappers for PAL linear model algorithms.

The following classes are available:

    * :class:`LinearRegression`
    * :class:`LogisticRegression`
    * :class:`OnlineLinearRegression`
    * :class:`OnlineMultiLogisticRegression`
"""
# pylint: disable=too-many-arguments,too-many-instance-attributes, too-many-locals, too-many-statements, too-many-branches
#pylint: disable=too-many-lines, line-too-long, relative-beyond-top-level, attribute-defined-outside-init, invalid-name
#pylint: disable=c-extension-no-member
import itertools
import logging
import uuid
try:
    import pyodbc
except ImportError as error:
    pass
from hdbcli import dbapi
from hana_ml.ml_base import try_drop
from hana_ml.ml_exceptions import FitIncompleteError
from .sqlgen import trace_sql
from .pal_base import (
    PALBase,
    ParameterTable,
    parse_one_dtype,
    ListOfStrings,
    ListOfTuples,
    pal_param_register,
    require_pal_usable
)
from . import metrics

logger = logging.getLogger(__name__) #pylint: disable=invalid-name

class LinearRegression(PALBase):
    r"""
    Linear regression is an approach to model the linear relationship between a variable,
    usually referred to as dependent variable, and one or more variables, usually referred to as independent variables, denoted as predictor vector.

    .. note::
        Linear Regression supports model evaluation and parameter selection, explanations of this topic can be seen in
        :ref:`param_select-label`.

    Parameters
    ----------

    solver : {'QR', 'SVD', 'CD', 'Cholesky', 'ADMM'}, optional

        Algorithms to use to solve the least square problem. Case-insensitive.

        - 'QR': QR decomposition (numerically stable, but fails when A is rank-deficient).
        - 'SVD': singular value decomposition (numerically stable and can handle rank deficiency but computationally expensive).
        - 'CD': cyclical coordinate descent method to solve elastic net regularized multiple linear regression.
        - 'Cholesky': Cholesky decomposition (fast but numerically unstable).
        - 'ADMM': Alternating direction method of multipliers (ADMM) to solve elastic net regularized multiple linear regression. This method is faster than the cyclical coordinate descent method in many cases and recommended.

        'CD' and 'ADMM' are supported only when ``var_select`` is 'all'.

        Defaults to 'QR' decomposition.

    var_select : {'all', 'forward', 'backward', 'stepwise'}, optional

        Method to perform variable selection.

        - 'all': all variables are included.
        - 'forward': forward selection.
        - 'backward': backward selection.
        - 'stepwise': stepwise selection.

        'forward', 'backward' and 'stepwise' are supported only when ``solver``
        is not 'CD', 'ADMM' and ``intercept`` is True.

        Defaults to 'all'.

    features_must_select: str or list of str, optional

        Specifies the column name that needs to be included in the final training model when executing the variable selection.

        This parameter can be specified multiple times, each time with one column name as feature.

        Only valid when ``var_select`` is not 'all'.

        Note that This parameter is a hint.
        There are exceptional cases that a specified mandatory feature is excluded in the final model.

        For instance, some mandatory features can be represented as a linear combination of other features, among which some are also mandatory features.

        No default value.

    intercept : bool, optional

        - True : include the intercept term in the model.
        - False : ignore the intercept.

        Defaults to True.

    alpha_to_enter : float, optional

        P-value for forward and stepwise selection.

        Valid only when ``var_select`` is 'forward' or 'stepwise'.

        Defaults to 0.05 when ``var_select`` is 'forward', 0.15 when ``var_select`` is 'stepwise'.

    alpha_to_remove : float, optional

        P-value for backward and stepwise selection.

        Valid only when ``var_select`` is 'backward' or 'stepwise'.

        Defaults to 0.1 when `var_select`` is 'backward', and 0.15  when ``var_select`` is 'stepwise'.

    enet_lambda : float, optional

        Penalized weight. Value should be greater than or equal to 0.

        Valid only when ``solver`` is 'CD' or 'ADMM'.

    enet_alpha : float, optional

        Elastic net mixing parameter.

        Ranges from 0 (Ridge penalty) to 1 (LASSO penalty) inclusively.

        Valid only when ``solver`` is 'CD' or 'ADMM'.

        Defaults to 1.0.

    max_iter : int, optional

        Maximum number of passes over training data.

        If convergence is not reached after the specified number of
        iterations, an error will be generated.

        Valid only when ``solver`` is 'CD' or 'ADMM'.

        Defaults to 1e5.

    tol : float, optional

        Convergence threshold for coordinate descent.

        Valid only when ``solver`` is 'CD'.

        Defaults to 1.0e-7.

    pho : float, optional

        Step size for ADMM. Generally, it should be greater than 1.

        Valid only when ``solver`` is 'ADMM'.

        Defaults to 1.8.

    stat_inf : bool, optional

        If true, output t-value and Pr(>|t|) of coefficients.

        Defaults to False.

    adjusted_r2 : bool, optional

        If true, include the adjusted R2 value in statistics.

        Defaults to False.

    dw_test : bool, optional

        If true, conduct Durbin-Watson test under null hypothesis that errors do not follow a first order autoregressive process.

        Not available if elastic net regularization is enabled or ``intercept`` is False.

        Defaults to False.

    reset_test : int, optional

        Specifies the order of Ramsey RESET test.

        Ramsey RESET test with power of variables ranging from 2 to this value (greater than 1) will be conducted.

        Value 1 means RESET test will not be conducted. Not available if elastic net regularization is enabled or ``intercept`` is False.

        Defaults to 1.

    bp_test : bool, optional

        If true, conduct Breusch-Pagan test under null hypothesis that homoscedasticity is satisfied.

        Not available if elastic net regularization is enabled or ``intercept`` is False.

        Defaults to False.

    ks_test : bool, optional

        If true, conduct Kolmogorov-Smirnov normality test under null hypothesis that errors follow a normal distribution.

        Not available if elastic net regularization is enabled or ``intercept`` is False.

        Defaults to False.

    thread_ratio : float, optional

        Controls the proportion of available threads to use.

        The value range is from 0 to 1, where 0 means only using 1 thread, and 1 means using at most all the currently available threads.

        Values outside this range tell PAL to heuristically determine the number of threads to use.

        Valid only when ``solver`` is 'QR', 'CD', 'Cholesky' or 'ADMM'.

        Defaults to 0.0.

    categorical_variable : str or ist of str, optional

        Specifies INTEGER columns specified that should be be treated as categorical.

        Other INTEGER columns will be treated as continuous.

    pmml_export : {'no', 'multi-row'}, optional

        Controls whether to output a PMML representation of the model, and how to format the PMML. Case-insensitive.

            - 'no' or not provided: Does not export multiple linear regression model in PMML.
            - 'multi-row': Exports a PMML model, exports multiple linear regression model in PMML. The maximum length of each row is 5000 characters.

        Currently either PMML or JSON format model can be exported. JSON format is preferred if both formats are to be exported.

        Defaults to 'no'.

    resampling_method : {'cv', 'bootstrap', 'cv_sha', 'bootstrap_sha', 'cv_hyperband', 'bootstrap_hyperband'}, optional

        Specifies the resampling method for model evaluation/parameter selection.

        If no value is specified for this parameter, neither model evaluation

        nor parameter selection is activated.

        Must be set together with ``evaluation_metric``.

        No default value.

        .. note::
            Resampling methods that end with 'sha' or 'hyperband' are used for
            parameter selection only, not for model evaluation.
    evaluation_metric : {'rmse'}, optional

        Specifies the evaluation metric for model evaluation or parameter selection.

        Must be set together with ``resampling_method``.

        No default value.

    fold_num : int, optional

        Specifies the fold number for the cross validation method.
        Mandatory and valid only when ``resampling_method`` is set to 'cv',
        'cv_sha' or 'cv_hyperband'.

        No default value.

    repeat_times : int, optional

        Specifies the number of repeat times for resampling.

        Defaults to 1.

    search_strategy : {'grid', 'random'}, optional

        Specifies the search strategy for parameter selection.

        Mandatory if ``resampling_method`` is specified and ends with 'sha'.

        Defaults to 'random' and cannot be changed if ``resampling_method`` is specified and
        ends with 'hyperband'; otherwise no default value, and parameter selection
        cannot be carried out if not specified.

    random_search_times : int, optional

        Specifies the number of times to randomly select candidate parameters for selection.

        Mandatory and valid when ``search_strategy`` is set to 'random', or when ``resampling_method``
        is 'cv_hyperband' or 'bootstrap_hyperband'.

        No default value.

    random_state : int, optional

        Specifies the seed for random generation. Use system time when 0 is specified.

        Defaults to 0.

    timeout : int, optional

        Specifies maximum running time for model evaluation or parameter

        selection, in seconds. No timeout when 0 is specified.

        Defaults to 0.

    progress_indicator_id : str, optional

        Sets an ID of progress indicator for model evaluation or parameter selection.

        No progress indicator is active if no value is provided.

        No default value.

    param_values : dict or list of tuples, optional

        Specifies values of specific parameters to be selected.

        Valid only when ``resampling_method`` and ``search_strategy`` are both specified.

        Specified parameters could be ``enet_lambda`` and ``enet_alpha``.

        No default value.

    param_range : dict or list of tuples, optional

        Specifies range of specific parameters to be selected.

        Valid only when ``resampling_method`` and ``search_strategy`` are both specified.

        Specified parameters could be ``enet_lambda``, ``enet_alpha``.

        No default value.

    handle_missing : bool, optional

        - True : handle missing values.
        - False : do not handle missing values.

        Defaults to True.

    json_export : bool, optional

        - False : Does not export multiple linear regression model in JSON.
        - True : Exports multiple linear regression model in JSON.

        Currently either PMML or JSON format model can be exported.
        JSON format is preferred if both formats are to be exported.

        Defaults to False.


    precompute_lms_sketch : bool, optional

        - False : Do not perform LMS sketch.
        - True : Performs LMS sketch.

        LMS sketch will only perform when ``resampling_method`` is set,
        and the size of ``data`` is larger than the number of features.

        Defaults to True.

    stable_sketch_alg : bool, optional

        When computing LMS sketch, there are two algorithms to choose. One algorithm is more numerical stable than the other one, but is slower.

          - False : Do not use stable algorithm.
          - True : Uses stable algorithm.

        Only valid when LMS sketch is performed (``precompute_lms_sketch`` = True) and ``sparse_sketch_alg`` is False.

        Defaults to True.

    sparse_sketch_alg : bool, optional

        This is specific LMS sketch algorithm to cope with sparse data.

          - False : Do not use sparse LMS sketch algorithm.
          - True : Uses sparse LMS sketch algorithm.

        Only valid when LMS sketch is performed (``precompute_lms_sketch`` = True).

        Defaults to False.

    resource : str, optional
        Specifies the resource type used in successive-halving and hyperband algorithm for parameter selection.

        Currently the only valid option is 'max_iter'.

        Mandatory and valid only when ``resampling_method`` is set as 'cv_sha', 'bootstrap_sha',
        'cv_hyperband' or 'bootstrap_hyperband'.

    max_resource : int, optional
        Maximum allowed resource budget for single hyper-parameter candidate, must be greater than 0.

        Mandatory and valid only wen ``resource`` is set.

    reduction_rate : float, optional
        Specifies the reduction rate of available size of hyper-parameter candidates.
        For each round, the available parameter candidate size will be divided by value of this parameter.
        Thus valid value for this parameter must be greater than 1.0

        Valid only when ``resource`` is set.

        Defaults to 3.0.

    aggressive_elimination : bool, optional
        Specifies whether to perform aggressive elimination behavior for successive-halving algorithm or not.

        When set to True, it will eliminate more parameter candidates than expected(defined via ``reduction_rate``).
        This can enhance the run-time performance but could result in sub-optimal hyper-parameter candidate.

        Valid only when ``resampling_method`` is 'cv_sha' or 'bootstrap_sha'.

        Defaults to False.

    ps_verbose : bool, optional
        Specifies whether to output optimal hyper-parameter and all evaluation statistics of related
        hyper-parameter candidates in attribute `statistics_` or not.

        Defaults to True.

    min_resource_rate : float, optional
        Specifies the minimum required resource budget compared to maximum resource
        for single hyper-parameter candidate. Valid value should be greater than or equal to 0,
        but less than 1.

        Valid only when ``resource`` is set.

        Defaults to 0.

    Attributes
    ----------

    coefficients_ : DataFrame

        Fitted regression coefficients.

    fitted_ : DataFrame

        Predicted dependent variable values for training data.
        Set to None if the training data has no row IDs.

    statistics_ : DataFrame

        Regression-related statistics, such as mean squared error.

    optim_param_ : DataFrame
        If parameter selection is enabled, the optimal parameters will be selected.

    pmml_ : DataFrame

        PMML model. (deprecate as JSON format is also supported in the model).
        Please use `semistructured_result_` shown below to get the model.

    semistructured_result_ : DataFrame

        Linear regression model in PMML or JSON format.

    Examples
    --------
    Training data:

    >>> df.collect()
      ID       Y    X1 X2  X3
    0  0  -6.879  0.00  A   1
    1  1  -3.449  0.50  A   1
    2  2   6.635  0.54  B   1
    3  3  11.844  1.04  B   1
    4  4   2.786  1.50  A   1
    5  5   2.389  0.04  B   2
    6  6  -0.011  2.00  A   2
    7  7   8.839  2.04  B   2
    8  8   4.689  1.54  B   1
    9  9  -5.507  1.00  A   2

    Training the model:

    >>> lr = LinearRegression(thread_ratio=0.5,
    ...                       categorical_variable=["X3"])
    >>> lr.fit(data=df, key='ID', label='Y')

    Prediction:

    >>> df2.collect()
       ID     X1 X2  X3
    0   0  1.690  B   1
    1   1  0.054  B   2
    2   2  0.123  A   2
    3   3  1.980  A   1
    4   4  0.563  A   1
    >>> lr.predict(data=df2, key='ID').collect()
       ID      VALUE
    0   0  10.314760
    1   1   1.685926
    2   2  -7.409561
    3   3   2.021592
    4   4  -3.122685

    **Biased Linear Model with Elastic-net Regularization**

    Relevant parameters: ``enet_alpha``, ``enet_lambda``

    Training data:

    >>> df.collect()
      ID  V1     V2    V3   V4
    0  0 1.2    0.1 0.205  0.9
    1  1 0.2 -1.705  -3.4  1.7
    2  2 1.1    0.4   0.8  0.5
    3  3 1.1    0.1 0.201  0.8
    4  4 0.3 -0.306  -0.6  0.2

    Class initialization and model training:

    >>> lr = LinearRegression(solver='ADMM', enet_lambda=0.003194, enet_alpha=0.95)
    >>> lr.fit(data = df)

    **Biased Linear Model with Variable Selection**

    Relevant parameters: ``var_select``, ``features_must_select``, ``alpha_to_enter``, ``alpha_to_remove``

    >>> lr = LinearRegression(var_select=True, alpha_to_enter=0.1)
    """

    solver_map = {'qr': 1, 'svd': 2, 'cd': 4, 'cholesky': 5, 'admm': 6}
    var_select_map = {'all': 0, 'forward': 1, 'backward': 2, 'stepwise':3}
    pmml_export_map = {'no': 0, 'multi-row': 2}
    values_list = {'enet_alpha': 'ENET_ALPHA', 'enet_lambda': 'ENET_LAMBDA'}
    resampling_method_map = {mtd:mtd for mtd in ['cv', 'bootstrap',
                                                 'cv_sha', 'bootstrap_sha',
                                                 'cv_hyperband',
                                                 'bootstrap_hyperband']}
    evaluation_metric_map = {'rmse': 'RMSE'}
    search_strategy_map = {'grid': 'grid', 'random': 'random'}
    resource_type = {'max_iter':'MAX_ITERATION'}
    pal_funcname = 'PAL_LINEAR_REGRESSION'
    def __init__(self,
                 solver=None,
                 var_select=None,
                 features_must_select=None,
                 intercept=True,
                 alpha_to_enter=None,
                 alpha_to_remove=None,
                 enet_lambda=None,
                 enet_alpha=None,
                 max_iter=None,
                 tol=None,
                 pho=None,
                 stat_inf=False,
                 adjusted_r2=False,
                 dw_test=False,
                 reset_test=None,
                 bp_test=False,
                 ks_test=False,
                 thread_ratio=None,
                 categorical_variable=None,
                 pmml_export=None,
                 resampling_method=None,
                 evaluation_metric=None,
                 fold_num=None,
                 repeat_times=None,
                 search_strategy=None,
                 random_search_times=None,
                 random_state=None,
                 timeout=None,
                 progress_indicator_id=None,
                 param_values=None,
                 param_range=None,
                 handle_missing=None,
                 json_export=None,
                 precompute_lms_sketch=None,
                 stable_sketch_alg=None,
                 sparse_sketch_alg=None,
                 resource=None,
                 max_resource=None,
                 reduction_rate=None,
                 aggressive_elimination=None,
                 ps_verbose=None,
                 min_resource_rate=None):

        super(LinearRegression, self).__init__()
        setattr(self, 'hanaml_parameters', pal_param_register())
        self.op_name = 'MLR_Regressor'
        self.solver = self._arg('solver', solver, self.solver_map)
        self.var_select = self._arg('var_select', var_select, self.var_select_map)
        if isinstance(features_must_select, str):
            features_must_select = [features_must_select]
        self.features_must_select = self._arg('features_must_select',
                                              features_must_select, ListOfStrings)
        self.intercept = self._arg('intercept', intercept, bool)
        if self.intercept is None:
            self.intercept = True
        self.alpha_to_enter = self._arg('alpha_to_enter', alpha_to_enter, float)
        self.alpha_to_remove = self._arg('alpha_to_remove', alpha_to_remove, float)
        self.enet_lambda = self._arg('enet_lambda', enet_lambda, float)
        self.enet_alpha = self._arg('enet_alpha', enet_alpha, float)
        self.max_iter = self._arg('max_iter', max_iter, int)
        self.tol = self._arg('tol', tol, float)
        self.pho = self._arg('pho', pho, float)
        self.stat_inf = self._arg('stat_inf', stat_inf, bool)
        self.adjusted_r2 = self._arg('adjusted_r2', adjusted_r2, bool)
        self.dw_test = self._arg('dw_test', dw_test, bool)
        self.reset_test = self._arg('reset_test', reset_test, int)
        self.bp_test = self._arg('bp_test', bp_test, bool)
        self.ks_test = self._arg('ks_test', ks_test, bool)
        self.thread_ratio = self._arg('thread_ratio', thread_ratio, float)
        self.handle_missing = self._arg('handle_missing', handle_missing, bool)
        self.json_export = self._arg('json_export', json_export, bool)
        self.precompute_lms_sketch = self._arg('precompute_lms_sketch', precompute_lms_sketch, bool)
        self.stable_sketch_alg = self._arg('stable_sketch_alg', stable_sketch_alg, bool)
        self.sparse_sketch_alg = self._arg('sparse_sketch_alg', sparse_sketch_alg, bool)
        if isinstance(categorical_variable, str):
            categorical_variable = [categorical_variable]
        self.categorical_variable = self._arg('categorical_variable',
                                              categorical_variable, ListOfStrings)
        self.pmml_export = self._arg('pmml_export', pmml_export, self.pmml_export_map)
        if solver is not None:
            if solver.lower() == 'cd' or solver.lower() == 'admm':
                if var_select is not None and var_select.lower() != 'all':
                    msg = ('var_select cannot be {} when solver ' +
                           'is {}.').format(var_select.lower(), solver.lower())
                    logger.error(msg)
                    raise ValueError(msg)
        if solver is None or (solver.lower() != 'cd' and solver.lower() != 'admm'):
            if enet_lambda is not None:
                msg = ('enet_lambda is applicable only when solver is ' +
                       'coordinate descent or admm.')
                logger.error(msg)
                raise ValueError(msg)
            if enet_alpha is not None:
                msg = ('enet_alpha is applicable only when solver is ' +
                       'coordinate descent or admm.')
                logger.error(msg)
                raise ValueError(msg)
            if max_iter is not None:
                msg = ('max_iter is applicable only when solver is ' +
                       'coordinate descent or admm.')
                logger.error(msg)
                raise ValueError(msg)
        if (solver is None or solver.lower() != 'cd') and tol is not None:
            msg = 'tol is applicable only when solver is coordinate descent.'
            logger.error(msg)
            raise ValueError(msg)
        if (solver is None or solver.lower() != 'admm') and pho is not None:
            msg = 'pho is applicable only when solver is admm.'
            logger.error(msg)
            raise ValueError(msg)
        if var_select is None or var_select.lower() not in ['forward', 'stepwise']:
            if alpha_to_enter is not None:
                msg = 'alpha_to_enter is applicable only when var_select is forward or stepwise!'
                logger.error(msg)
                raise ValueError(msg)
        if var_select is None or var_select.lower() not in ['backward', 'stepwise']:
            if alpha_to_remove is not None:
                msg = 'alpha_to_remove is applicable only when var_select is backward or stepwise!'
                logger.error(msg)
                raise ValueError(msg)
        if enet_lambda is not None or enet_alpha is not None or intercept is False:
            if dw_test is not None and dw_test is not False:
                msg = ('dw_test is applicable only when elastic net regularization ' +
                       'is disabled and the model includes an intercept.')
                logger.error(msg)
                raise ValueError(msg)
            if reset_test is not None and reset_test != 1:
                msg = ('reset_test is applicable only when elastic net regularization ' +
                       'is disabled and the model includes an intercept.')
                logger.error(msg)
                raise ValueError(msg)
            if bp_test is not None and bp_test is not False:
                msg = ('bp_test is applicable only when elastic net regularization ' +
                       'is disabled and the model includes an intercept.')
                logger.error(msg)
                raise ValueError(msg)
            if ks_test is not None and ks_test is not False:
                msg = ('ks_test is applicable only when elastic net regularization ' +
                       'is disabled and the model includes an intercept.')
                logger.error(msg)
                raise ValueError(msg)
        if isinstance(reset_test, bool):
            msg = ('reset_test should be an integer, not a boolean ' +
                   'indicating whether or not to conduct the Ramsey RESET test.')
            logger.error(msg)
            raise TypeError(msg)
        if enet_alpha is not None and not 0 <= enet_alpha <= 1:
            msg = 'enet_alpha {!r} is out of bounds.'.format(enet_alpha)
            logger.error(msg)
            raise ValueError(msg)
        self.resampling_method = self._arg('resampling_method', resampling_method,
                                           self.resampling_method_map)
        self.evaluation_metric = self._arg('evaluation_metric', evaluation_metric,
                                           self.evaluation_metric_map)
        self.fold_num = self._arg('fold_num', fold_num, int)
        self.repeat_times = self._arg('repeat_times', repeat_times, int)
        self.search_strategy = self._arg('search_strategy', search_strategy,
                                         self.search_strategy_map,
                                         required='sha' in str(self.resampling_method))
        self.random_search_times = self._arg('random_search_times', random_search_times, int)
        self.random_state = self._arg('random_state', random_state, int)
        self.timeout = self._arg('timeout', timeout, int)
        self.progress_indicator_id = self._arg('progress_indicator_id',
                                               progress_indicator_id, str)
        self.resource, self.max_resource, self.reduction_rate = None, None, None
        self.aggressive_elimination, self.ps_verbose, self.min_resource_rate = None, None, None
        if self.resampling_method is not None:
            sha_act = any(tlw in self.resampling_method for tlw in ['sha', 'hyperband'])
            if sha_act:
                self.resource = self._arg('resource', resource, self.resource_type,
                                          required=True)
                self.max_resource = self._arg('max_resource', max_resource, int,
                                              required=True)
                self.reduction_rate = self._arg('reduction_rate', reduction_rate, float)
                self.aggressive_elimination = self._arg('aggressive_elimination',
                                                        aggressive_elimination,
                                                        bool)
                self.ps_verbose = self._arg('ps_verbose', ps_verbose, bool)
                self.min_resource_rate = self._arg('min_resource_rate',
                                                   min_resource_rate, float)
        if isinstance(param_range, dict):
            param_range = [(x, param_range[x]) for x in param_range]
        self.param_range = self._arg('param_range', param_range, ListOfTuples)
        if isinstance(param_values, dict):
            param_values = [(x, param_values[x]) for x in param_values]
        self.param_values = self._arg('param_values', param_values, ListOfTuples)
        search_param_count = 0
        for param in (self.resampling_method, self.evaluation_metric):
            if param is not None:
                search_param_count += 1
        if search_param_count not in (0, 2):
            msg = "`resampling_method`, and `evaluation_metric` must be set together."
            logger.error(msg)
            raise ValueError(msg)
        if self.search_strategy is not None and self.resampling_method is None:
            msg = "`search_strategy` cannot be set if `resampling_method` is not specified."
            logger.error(msg)
            raise ValueError(msg)
        if 'cv' in str(self.resampling_method) and self.fold_num is None:
            msg = ("`fold_num` must be set when "+
                   "`resampling_method` is set as 'cv', 'cv_sha' or 'cv_hyperband'.")
            logger.error(msg)
            raise ValueError(msg)
        if 'cv' not in str(self.resampling_method) and self.fold_num is not None:
            msg = ("`fold_num` is not valid when parameter selection is not" +
                   " enabled, or `resampling_method` is not set as 'cv', 'cv_sha' or 'cv_hyperband'.")
            logger.error(msg)
            raise ValueError(msg)
        if (self.search_strategy == 'random' or 'hyperband' in str(self.resampling_method)) and \
        self.random_search_times is None:
            msg = ("`random_search_times` must be set when " +
                   "`search_strategy` is set as 'random', or when " +
                   "`resampling_method` is set as 'cv_hyperband' or 'bootstrap_hyperband'.")
            logger.error(msg)
            raise ValueError(msg)
        if 'hyperband' in str(self.resampling_method) and self.search_strategy == 'grid':
            msg = "`search_strategy` can only be 'random' if `resampling_method` is 'cv_hyperband'" +\
            " or 'bootstrap_hyperband'."
            logger.warning(msg)
        if 'hyperband' not in str(self.resampling_method) and self.search_strategy == 'grid' and\
        self.random_search_times is not None:
            msg = ("`random_search_times` is not valid " +
                   "when parameter selection is not enabled" +
                   ", or `search_strategy` is not set as 'random'.")
            logger.warning(msg)
        if self.search_strategy is None and 'hyperband' not in str(self.resampling_method):
            if self.param_values is not None:
                msg = ("`param_values` can only be specified " +
                       "when `search_strategy` is enabled.")
                logger.error(msg)
                raise ValueError(msg)
            if self.param_range is not None:
                msg = ("`param_range` can only be specified " +
                       "when `search_strategy` is enabled.")
                logger.error(msg)
                raise ValueError(msg)
        if self.search_strategy is not None:
            set_param_list = []
            if self.enet_lambda is not None:
                set_param_list.append("enet_lambda")
            if self.enet_alpha is not None:
                set_param_list.append("enet_alpha")
            if self.param_values is not None:
                for x in self.param_values:#pylint:disable=invalid-name
                    if len(x) != 2:#pylint:disable=bad-option-value
                        msg = ("Each tuple that specifies the values of a parameter should"+
                               " contain exactly 2 elements: 1st is parameter name,"+
                               " 2nd is a list of valid values.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] not in self.values_list:
                        msg = ("Specifying the values of `{}` for ".format(x[0])+
                               "parameter selection is invalid.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] in set_param_list:
                        msg = ("Parameter `{}` is invalid for ".format(x[0])+
                               "re-specification in parameter selection.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if self.solver not in (4, 6):
                        msg = ("Parameter `{}` is invalid when ".format(x[0])+
                               "`solver` is not set as 'cd' or 'admm'.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if not (isinstance(x[1], list) and all(isinstance(t, (int, float)) for t in x[1])):#pylint:disable=line-too-long
                        msg = "Valid values of `{}` must be a list of numerical values.".format(x[0])
                        logger.error(msg)
                        raise TypeError(msg)
                    set_param_list.append(x[0])

            if self.param_range is not None:
                rsz = [3] if self.search_strategy == 'grid'else [2, 3]
                for x in self.param_range:#pylint:disable=invalid-name
                    if len(x) != 2:#pylint:disable=bad-option-value
                        msg = ("Each tuple that specifies the range of a parameter should contain"+
                               " exactly 2 elements: 1st is parameter name, 2nd is value range.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] not in self.values_list:
                        msg = ("Specifying the values of `{}` for ".format(x[0])+
                               "parameter selection is invalid.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] in set_param_list:
                        msg = ("Parameter `{}` is invalid for ".format(x[0])+
                               "re-specification in parameter selection.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if self.solver not in (4, 6):
                        msg = ("Parameter `{}` is invalid when ".format(x[0])+
                               "`solver` is not set as 'cd' or 'admm'.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if not (isinstance(x[1], list) and len(x[1]) in rsz and all(isinstance(t, (int, float)) for t in x[1])):#pylint:disable=line-too-long
                        msg = ("The provided `{}` is either not ".format(x[0])+
                               "a list of numerical values, or it contains wrong number of values.")
                        logger.error(msg)
                        raise TypeError(msg)

    @trace_sql
    def fit(self, data, key=None, features=None,
            label=None, categorical_variable=None):
        r"""
        Fit regression model based on training data.

        Parameters
        ----------

        data : DataFrame

            Training data.

        key : str, optional

            Name of the ID column.

            If ``key`` is not provided, then:

            - if ``data`` is indexed by a single column, then ``key`` defaults
              to that index column;
            - otherwise, it is assumed that ``data`` contains no ID column.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.
            If ``label`` is not provided, it defaults to the last column.

        categorical_variable : str or list of str, optional

            Specifies INTEGER column(s) that should be treated as categorical.

            Other INTEGER columns will be treated as continuous.

        Returns
        -------
        LinearRegression

            A fitted object.
        """
        # pylint: disable=too-many-locals
        setattr(self, 'hanaml_fit_params', pal_param_register())
        conn = data.connection_context
        key = self._arg('key', key, str)
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        if isinstance(categorical_variable, str):
            categorical_variable = [categorical_variable]
        categorical_variable = self._arg('categorical_variable', categorical_variable, ListOfStrings)
        if not self._disable_hana_execution:
            require_pal_usable(conn)
            index = data.index
            if isinstance(index, str):
                if key is not None and index != key:
                    msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                    "and the designated index column '{}'.".format(index)
                    logger.warning(msg)
            key = index if key is None else key
            cols = data.columns
            if key is not None:
                id_col = [key]
                cols.remove(key)
            else:
                id_col = []
            if label is None:
                label = cols[-1]
            cols.remove(label)
            if features is None:
                features = cols
            data_ = data[id_col + [label] + features]
        else:
            data_ = data
        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        outputs = ['COEF', 'PMML', 'FITTED', 'STATS', 'OPTIMAL_PARAM']
        outputs = ['#PAL_LINEAR_REGRESSION_{}_TBL_{}_{}'.format(name, self.id, unique_id)
                   for name in outputs]
        coef_tbl, pmml_tbl, fitted_tbl, stats_tbl, opt_param_tbl = outputs
        param_rows = [('ALG', self.solver, None, None),
                      ('VARIABLE_SELECTION', self.var_select, None, None),
                      ('NO_INTERCEPT', not self.intercept, None, None),
                      ('ALPHA_TO_ENTER', None, self.alpha_to_enter, None),
                      ('ALPHA_TO_REMOVE', None, self.alpha_to_remove, None),
                      ('ENET_LAMBDA', None, self.enet_lambda, None),
                      ('ENET_ALPHA', None, self.enet_alpha, None),
                      ('MAX_ITERATION', self.max_iter, None, None),
                      ('THRESHOLD', None, self.tol, None),
                      ('PHO', None, self.pho, None),
                      ('STAT_INF', self.stat_inf, None, None),
                      ('ADJUSTED_R2', self.adjusted_r2, None, None),
                      ('DW_TEST', self.dw_test, None, None),
                      ('RESET_TEST', self.reset_test, None, None),
                      ('BP_TEST', self.bp_test, None, None),
                      ('KS_TEST', self.ks_test, None, None),
                      ('PMML_EXPORT', self.pmml_export, None, None),
                      ('HAS_ID', key is not None, None, None),
                      ('RESAMPLING_METHOD', None, None, self.resampling_method),
                      ('EVALUATION_METRIC', None, None, self.evaluation_metric),
                      ('SEED', self.random_state, None, None),
                      ('REPEAT_TIMES', self.repeat_times, None, None),
                      ('PARAM_SEARCH_STRATEGY', None, None, self.search_strategy),
                      ('FOLD_NUM', self.fold_num, None, None),
                      ('RANDOM_SEARCH_TIMES', self.random_search_times, None, None),
                      ('TIMEOUT', self.timeout, None, None),
                      ('PROGRESS_INDICATOR_ID', None, None, self.progress_indicator_id),
                      ('HANDLE_MISSING', self.handle_missing, None, None),
                      ('JSON_EXPORT', self.json_export, None, None),
                      ('PRECOMPUTE_LMS_SKETCH', self.precompute_lms_sketch, None, None),
                      ('STABLE_SKETCH_ALG', self.stable_sketch_alg, None, None),
                      ('SPARSE_SKETCH_ALG', self.sparse_sketch_alg, None, None),
                      ('RESOURCE', None, None, self.resource),
                      ('MAX_RESOURCE', self.max_resource, None, None),
                      ('REDUCTION_RATE', None, self.reduction_rate, None),
                      ('AGGRESSIVE_ELIMINATION', self.aggressive_elimination,
                       None, None),
                      ('PS_VERBOSE', self.ps_verbose, None, None),
                      ('MIN_RESOURCE_RATE', None, self.min_resource_rate, None)]
        if self.param_values is not None:
            for x in self.param_values:#pylint:disable=invalid-name
                values = str(x[1]).replace('[', '{').replace(']', '}')
                param_rows.extend([(self.values_list[x[0]]+"_VALUES",
                                    None, None, values)])
        if self.param_range is not None:
            for x in self.param_range:#pylint:disable=invalid-name
                range_ = str(x[1])
                if len(x[1]) == 2 and self.search_strategy == 'random':
                    range_ = range_.replace(',', ',,')
                param_rows.extend([(self.values_list[x[0]]+"_RANGE",
                                    None, None, range_)])
        if self.solver != 2:
            param_rows.append(('THREAD_RATIO', None, self.thread_ratio, None))
        if self.features_must_select is not None:
            param_rows.extend(('MANDATORY_FEATURE', None, None, variable)
                              for variable in self.features_must_select)
        if self.categorical_variable is not None:
            param_rows.extend(('CATEGORICAL_VARIABLE', None, None, variable)
                              for variable in self.categorical_variable)
        if categorical_variable is not None:
            param_rows.extend(('CATEGORICAL_VARIABLE', None, None, variable)
                              for variable in categorical_variable)
        try:
            self._call_pal_auto(conn,
                                'PAL_LINEAR_REGRESSION',
                                data_,
                                ParameterTable().with_data(param_rows),
                                *outputs)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, outputs)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, outputs)
            raise
        # pylint: disable=attribute-defined-outside-init
        self.coefficients_ = conn.table(coef_tbl)
        self.pmml_ = conn.table(pmml_tbl) if self.pmml_export else None
        self.semistructured_result_ = conn.table(pmml_tbl)
        self.fitted_ = conn.table(fitted_tbl) if key is not None else None
        self.statistics_ = conn.table(stats_tbl)
        self.optim_param_ = conn.table(opt_param_tbl)
        self.model_ = self.coefficients_
        return self

    @trace_sql
    def predict(self, data, key=None, features=None):
        r"""
        Predict dependent variable values based on fitted model.

        Parameters
        ----------

        data : DataFrame

            Independent variable values to predict for.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID columns.

        Returns
        -------

        DataFrame

            Predicted values, structured as follows:

                - ID column: with same name and type as ``data`` 's ID column.
                - VALUE: type DOUBLE, representing predicted values.
        """
        conn = data.connection_context
        if getattr(self, 'pmml_', None) is not None:
            model = self.pmml_
        elif getattr(self, 'model_') is not None:
            model = self.model_
        else:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")

        index = data.index
        key = self._arg('key', key, str, required=not isinstance(index, str))
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        cols = data.columns
        cols.remove(key)
        if features is None:
            features = cols
        data_ = data[[key] + features]
        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        fitted_tbl = '#PAL_LINEAR_REGRESSION_FITTED_TBL_{}_{}'.format(self.id, unique_id)
        param_rows = [('THREAD_RATIO', None, self.thread_ratio, None)]
        try:
            self._call_pal_auto(conn,
                                'PAL_LINEAR_REGRESSION_PREDICT',
                                data_,
                                model,
                                ParameterTable().with_data(param_rows),
                                fitted_tbl)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, fitted_tbl)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, fitted_tbl)
            raise
        return conn.table(fitted_tbl)

    def score(self, data, key=None, features=None, label=None):
        r"""
        Returns the coefficient of determination R2 of the prediction.

        Parameters
        ----------

        data : DataFrame

            Data on which to assess model performance.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.

            If ``label`` is not provided, it defaults to the last column.

        Returns
        -------

        float

            Returns the coefficient of determination R2 of the prediction.
        """
        if getattr(self, 'pmml_', None) is None and (getattr(self, 'model_') is None):
            raise FitIncompleteError("Model not initialized. Perform a fit first.")

        index = data.index
        key = self._arg('key', key, str, required=not isinstance(index, str))
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        cols = data.columns
        cols.remove(key)
        if label is None:
            label = cols[-1]
        cols.remove(label)
        if features is None:
            features = cols
        prediction = self.predict(data, key=key, features=features)
        prediction = prediction.rename_columns(['ID_P', 'PREDICTION'])
        original = data[[key, label]].rename_columns(['ID_A', 'ACTUAL'])
        joined = original.join(prediction, 'ID_P=ID_A').select('ACTUAL', 'PREDICTION')
        return metrics.r2_score(joined,
                                label_true='ACTUAL',
                                label_pred='PREDICTION')

    def create_model_state(self, model=None, function=None,
                           pal_funcname='PAL_LINEAR_REGRESSION',
                           state_description=None, force=False):
        r"""
        Create PAL model state.

        Parameters
        ----------
        model : DataFrame, optional
            Specify the model for AFL state.

            Defaults to self.model\_.

        function : str, optional
            Specify the function in the unified API.

            A placeholder parameter, not effective for Linear Regression.

        pal_funcname : int or str, optional
            PAL function name. Must be a valid PAL procedure that supports model state.

            Defaults to 'PAL_LINEAR_REGRESSION'.

        state_description : str, optional
            Description of the state as model container.

            Defaults to None.

        force : bool, optional
            If True it will delete the existing state.

            Defaults to False.
        """
        super()._create_model_state(model, function, pal_funcname, state_description, force)

    def set_model_state(self, state):
        """
        Set the model state by state information.

        Parameters
        ----------
        state: DataFrame or dict
            If state is DataFrame, it has the following structure:

                - NAME: VARCHAR(100), it mush have STATE_ID, HINT, HOST and PORT.
                - VALUE: VARCHAR(1000), the values according to NAME.

            If state is dict, the key must have STATE_ID, HINT, HOST and PORT.
        """
        super()._set_model_state(state)

    def delete_model_state(self, state=None):
        """
        Delete PAL model state.

        Parameters
        ----------
        state : DataFrame, optional
            Specified the state.

            Defaults to self.state.
        """
        super()._delete_model_state(state)

class OnlineLinearRegression(PALBase):
    r"""
    Online linear regression (Stateless) is an online version of the linear regression and is used when the training data are obtained multiple rounds.
    Additional data are obtained in each round of training. By making use of the current computed linear model and combining with the obtained data in each round,
    online linear regression adapts the linear model to make the prediction as precise as possible.

    .. note::

        We currently support Online Linear Regression(stateless) in SAP HANA Cloud.
        Online Linear Regression(stateful) version available in SAP HANA SPS05/06 has not been supported in hana-ml yet.

    Parameters
    ----------

    enet_lambda : float, optional
        Penalized weight. Value should be greater than or equal to 0.

        Defaults to 0.
    enet_alpha : float, optional
        Elastic net mixing parameter.
        Ranges from 0 (Ridge penalty) to 1 (LASSO penalty) inclusively.

        Defaults to 0.
    max_iter : int, optional
        Maximum iterative cycle.
        Defaults to 1000.

    tol : float, optional
        Convergence threshold.
        Defaults to 1.0e-5.

    Attributes
    ----------

    intermediate_result_ : DataFrame
        Intermediate model.

    coefficients_ : DataFrame
        Fitted regression coefficients.

    Examples
    --------

    First, initialize an online linear regression instance:

    >>> onlinelr = OnlineLinearRegression(enet_lambda=0.1,
                                          enet_alpha=0.5,
                                          max_iter=1200,
                                          tol=1E-6)

    Three rounds of data:

    >>> df_1.collect()
      ID      Y    X1    X2
    0  1  130.0   7.0  26.0
    1  2  124.0   1.0  29.0
    2  3  262.0  11.0  56.0
    3  4  162.0  11.0  31.0

    >>> df_2.collect()
       ID      Y    X1    X2
    0   5  234.0   7.0  52.0
    1   6  258.0  11.0  55.0
    2   7  298.0   3.0  71.0
    3   8  132.0   1.0  31.0

    >>> df_3.collect()
       ID      Y    X1    X2
    0   9  227.0   2.0  54.0
    1  10  256.0  21.0  47.0
    2  11  168.0   1.0  40.0
    3  12  302.0  11.0  66.0
    4  13  307.0  10.0  68.0

    Round 1, invoke partial_fit() for training the model with df_1:

    >>> onlinelr.partial_fit(df_1, key='ID', label='Y', features=['X1', 'X2'])

    Output:

    >>> onlinelr.coefficients_.collect()
          VARIABLE_NAME   COEFFICIENT_VALUE
    0  __PAL_INTERCEPT__           5.076245
    1                 X1           2.987277
    2                 X2           4.000540

    >>> onlinelr.intermediate_result_.collect()
      SEQUENCE                                 INTERMEDIATE_MODEL
    0        0  {"algorithm":"batch_algorithm","batch_algorith...

    Round 2, invoke partial_fit() for training the model with df_2:

    >>> onlinelr.partial_fit(df_2, key='ID', label='Y', features=['X1', 'X2'])

    Output:

    >>> onlinelr.coefficients_.collect()
           VARIABLE_NAME  COEFFICIENT_VALUE
    0  __PAL_INTERCEPT__           5.094444
    1                 X1           2.988419
    2                 X2           3.999563

    >>> onlinelr.intermediate_result_.collect()
      SEQUENCE                                 INTERMEDIATE_MODEL
    0        0  {"algorithm":"batch_algorithm","batch_algorith...

    Round 3, invoke partial_fit() for training the model with df_3:

    >>> onlinelr.partial_fit(df_3, key='ID', label='Y', features=['X1', 'X2'])

    Output:

    >>> onlinelr.coefficients_.collect()
           VARIABLE_NAME  COEFFICIENT_VALUE
    0  __PAL_INTERCEPT__           5.073338
    1                 X1           2.994118
    2                 X2           3.999389


    >>> onlinelr.intermediate_result_.collect()
      SEQUENCE                                 INTERMEDIATE_MODEL
    0        0  {"algorithm":"batch_algorithm","batch_algorith...

    Call predict() with df_predict:

    >>> df_predict.collect()
       ID    X1    X2
    0  14     2    67
    1  15     3    51

    Invoke predict():

    >>> fitted = onlinelr.predict(df_predict, key='ID', features=['X1', 'X2'])
    >>> fitted.collect()
      ID       VALUE
    0 14  279.020611
    1 15  218.024511

    Call score()

    >>> score = onlinelr.score(df_2, key='ID', label='Y', features=['X1', 'X2'])
    0.9999997918249237

    """
    def __init__(self,
                 enet_lambda=None,
                 enet_alpha=None,
                 max_iter=None,
                 tol=None):
        setattr(self, 'hanaml_parameters', pal_param_register())
        super(OnlineLinearRegression, self).__init__()
        self.enet_lambda = self._arg('enet_lambda', enet_lambda, float)
        self.enet_alpha = self._arg('enet_alpha', enet_alpha, float)
        self.max_iter = self._arg('max_iter', max_iter, int)
        self.tol = self._arg('tol', tol, float)

        self.model_ = None
        self.intermediate_result_ = None

    @trace_sql
    def partial_fit(self,
                    data,
                    key=None,
                    features=None,
                    label=None,
                    thread_ratio=None):
        r"""
        Online training based on each round of training data.

        Parameters
        ----------

        data : DataFrame

            Training data.

        key : str, optional

            Name of the ID column.

            If ``key`` is not provided, then:

            - if ``data`` is indexed by a single column, then ``key`` defaults
              to that index column;
            - otherwise, it is assumed that ``data`` contains no ID column.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.

            If ``label`` is not provided, it defaults to the last column.

        thread_ratio : float, optional

            Controls the proportion of available threads to use.

            The value range is from 0 to 1, where 0 means only using 1 thread, and 1 means using at most all the currently available threads.

            Values outside this range tell PAL to heuristically determine the number of threads to use.

            Defaults to 0.0.

        Returns
        -------
        OnlineLinearRegression

            A fitted object.

        """
        setattr(self, 'hanaml_fit_params', pal_param_register())
        if data is None:
            msg = 'The data for fit cannot be None!'
            logger.error(msg)
            raise ValueError(msg)

        conn = data.connection_context
        require_pal_usable(conn)
        execute_statement = None
        # init process, need to generate self.intermediate_result_ in the first time
        if self.model_ is None:
            unique_id = str(uuid.uuid1()).replace('-', '_').upper()
            inter_tbl = '#PAL_ONLINE_LINEAR_REGRESSION_INTER_TBL_{}_{}'.format(self.id, unique_id)
            param_rows = [('ENET_LAMBDA', None, self.enet_lambda, None),
                          ('ENET_ALPHA', None, self.enet_alpha, None),
                          ('MAX_ITERATION', self.max_iter, None, None),
                          ('THRESHOLD', None, self.tol, None)]
            try:
                self._call_pal_auto(conn,
                                    'PAL_INIT_ONLINE_LINEAR_REGRESSION',
                                    ParameterTable().with_data(param_rows),
                                    inter_tbl)
            except dbapi.Error as db_err:
                logger.exception(str(db_err))
                try_drop(conn, inter_tbl)
                raise
            except pyodbc.Error as db_err:
                logger.exception(str(db_err.args[1]))
                try_drop(conn, inter_tbl)
                raise
            self.intermediate_result_ = conn.table(inter_tbl)
        execute_statement = self.execute_statement
        key = self._arg('key', key, str)
        index = data.index
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        self.thread_ratio = self._arg('thread_ratio', thread_ratio, float)

        cols = data.columns
        if key is not None:
            id_col = [key]
            cols.remove(key)
        else:
            id_col = []
        if label is None:
            label = cols[-1]
        cols.remove(label)
        if features is None:
            features = cols
        data_ = data[id_col + [label] + features]

        # create inter tbl based on model_[1] or intermediate_result_ (for the first time)
        if self.model_ is not None:
            inter_tbl = self.model_[1]
        else:
            inter_tbl = self.intermediate_result_

        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        outputs = ['COEF', 'INTER_UPDATE']
        outputs = ['#PAL_ONLINE_LINEAR_REGRESSION_{}_TBL_{}_{}'.format(name, self.id, unique_id)
                   for name in outputs]
        coef_tbl, inter_update_tbl = outputs
        param_rows = [('HAS_ID', key is not None, None, None),
                      ('THREAD_RATIO', None, self.thread_ratio, None)]

        try:
            self._call_pal_auto(conn,
                                'PAL_TRAIN_ONLINE_LINEAR_REGRESSION',
                                data_,
                                inter_tbl,
                                ParameterTable().with_data(param_rows),
                                *outputs)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, outputs)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, outputs)
            raise
        self.intermediate_result_ = conn.table(inter_update_tbl)
        self.coefficients_ = conn.table(coef_tbl)
        self.model_ = [self.coefficients_, self.intermediate_result_]
        if execute_statement is not None:
            self.execute_statement = [execute_statement, self.execute_statement]
        return self

    @trace_sql
    def predict(self, data, key=None, features=None):
        r"""
        Predict dependent variable values based on a fitted model.

        Parameters
        ----------

        data : DataFrame

            Independent variable values to predict for.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID columns.

        Returns
        -------

        DataFrame

            Predicted values, structured as follows:

                - ID column: with same name and type as ``data`` 's ID column.
                - VALUE: type DOUBLE, representing predicted values.
        """

        if self.model_ is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")
        lr = LinearRegression()
        lr.pmml_ = None
        lr.model_ = self.model_[0]
        if self._disable_hana_execution:
            lr.disable_hana_execution()
        fitted_tbl = lr.predict(data, key, features)
        self.execute_statement = lr.execute_statement
        return fitted_tbl

    def score(self, data, key=None, features=None, label=None):
        r"""
        Returns the coefficient of determination R2 of the prediction.

        Parameters
        ----------

        data : DataFrame

            Data on which to assess model performance.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.

            If ``label`` is not provided, it defaults to the last column.

        Returns
        -------

        float

            Returns the coefficient of determination R2 of the prediction.
        """
        if self.model_ is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")
        lr = LinearRegression()
        lr.pmml_ = None
        lr.model_ = self.model_[0]
        score = lr.score(data, key, features, label)
        return score

class LogisticRegression(PALBase):#pylint:disable=too-many-instance-attributes
    r"""
    Logistic regression model that handles binary-class and multi-class
    classification problems.

    Parameters
    ----------

    multi_class : bool, optional

        If True, perform multi-class classification. Otherwise, there must be only two classes.

        Defaults to False.

    max_iter : int, optional

        Maximum number of iterations taken for the solvers to converge.
        If convergence is not reached after this number, an error will be generated.

        When ``solver`` is 'newton' or 'lbfgs', the convex optimizer may return suboptimal results after the maximum number of iterations.
        When ``solver`` is 'cyclical', if convergence is not reached after the maximum number of passes over training data, an error will be generated.

        - multi-class: Defaults to 100.
        - binary-class: Defaults to 100000 when ``solver`` is 'cyclical',
          1000 when ``solver`` is 'proximal', otherwise 100.

    pmml_export : {'no', 'single-row', 'multi-row'}, optional

        Controls whether to output a PMML representation of the model, and how to format the PMML.
        Case-insensitive.

        **multi-class**

            - 'no' or not provided: No PMML model.
            - 'multi-row': Exports logistic regression model in PMML.

        **binary-class**

            - 'no' or not provided: No PMML model.
            - 'single-row': Exports a PMML model in a maximum of one row. Fails if the model doesn't fit in one row.
            - 'multi-row': Exports a PMML model, splitting it across multiple rows if it doesn't fit in one.

        In multi-class, both PMML and JSON format model can be exported.
        JSON format is preferred if both formats are to be exported.

        Defaults to 'no'.

    categorical_variable : str or list of str, optional(deprecated)

        Specifies INTEGER column(s) in the data that should be treated category variable.

    standardize : bool, optional

        If true, standardize the data to have zero mean and unit
        variance.

        Defaults to True.

    stat_inf : bool, optional

        If true, proceed with statistical inference.

        Defaults to False.

    solver : {'auto', 'newton', 'cyclical', 'lbfgs', 'stochastic', 'proximal'}, optional

        Optimization algorithm.

        - 'auto' : automatically determined by system based on input data and parameters.
        - 'newton': Newton iteration method, can only solve ridge regression problems.
        - 'cyclical': Cyclical coordinate descent method to fit elastic net regularized logistic regression.
        - 'lbfgs': LBFGS method(recommended when having many independent variables, can only solve ridge regression
          problems when ``multi_class`` is True).
        - 'stochastic': Stochastic gradient descent method(recommended when dealing with very large dataset),
          can only solve ridge regression problems.
        - 'proximal': Proximal gradient descent method to fit elastic net regularized logistic regression.

        When ``multi_class`` is True, only 'auto', 'lbfgs' and 'cyclical' are valid solvers.

        Defaults to 'auto'.

        .. Note ::

          If it happens that the enet regularization term contains LASSO penalty,
          while a solver that can only solve ridge regression problems is specified,
          then the specified solver will be ignored(hence default value is used).
          The users can check the statistical table for the solver that has been adopted finally.

    enet_alpha : float, optional

        The elastic net mixing parameter.
        The valid value range is between 0 and 1 inclusively(0: Ridge penalty, 1: LASSO penalty).

        Defaults to 1.0.

    enet_lambda : float, optional

        Penalized weight. The value should be equal to or greater than 0.

        Defaults to 0.0.

    tol : float, optional

        Convergence threshold for exiting iterations.

        Defaults to 1.0e-7 when ``solver`` is cyclical, 1.0e-6 otherwise.

    epsilon : float, optional

        Determines the accuracy with which the solution is to
        be found.

        When ``solver`` is 'lbfgs', the condition is: :math:`\|g\|` < ``epsilon`` * max {1, :math:`\|x\|`},
        where g is gradient of objective function, x is solve of current iteration, and :math:`\|\cdot\|` denotes the L2 norm;

        When ``solver`` is 'newton', the condition is: :math:`\|x- x'\|` < ``epsilon`` * sqrt(n),
        where x is the solve of current iteration, x' is the previous iteration,
        and n is the number of features.

        Only valid when ``multi_class`` is False and the ``solver`` is 'newton' or 'lbfgs'.

        Defaults to 1.0e-6 when ``solver`` is 'newton', 1.0e-5 when ``solver`` is 'lbfgs'.

    thread_ratio : float, optional

        Controls the proportion of available threads to use for fit() method.

        The value range is from 0 to 1, where 0 indicates a single thread, and 1 indicates up to all available threads.

        Values between 0 and 1 will use that percentage of available threads.

        Values outside this range tell PAL to heuristically determine the number of threads to use.

        Defaults to 1.0.

    max_pass_number : int, optional

        The maximum number of passes over the data.

        Only valid when ``multi_class`` is False and (actual) ``solver`` is 'stochastic'.

        Defaults to 1.

    sgd_batch_number : int, optional

        The batch number of Stochastic gradient descent.

        Only valid when ``multi_class`` is False and (actual) ``solver`` is 'stochastic'.

        Defaults to 1.

    precompute : bool, optional

        Whether to pre-compute the Gram matrix.

        Only valid when ``multi_class`` is False and (actual) ``solver`` is 'cyclical'.

        Defaults to True.

    handle_missing : bool, optional

        - True : handle missing values.
        - False : do not handle missing values.

        Only valid when ``multi_class`` is False.

        Defaults to True.

    categorical_variable : str or list of str, optional

        Specifies INTEGER column(s) in the data that should be treated as categorical.

        By default, string is categorical, while int and double are numerical.

    lbfgs_m : int, optional

        Number of previous updates to keep.

        Only applicable when ``multi_class`` is False and ``solver`` is 'lbfgs'.

        Defaults to 6.

    resampling_method : str, optional

        Specifies the resampling method for model evaluation or parameter selection.

        Valid resampling methods are listed as follows: 'cv', 'cv_sha', 'cv_hyperband',
        'stratified_cv', 'stratified_cv_sha', 'stratified_cv_hyperband',
        'bootstrap', 'bootstrap_sha', 'bootstrap_hyperband', 'stratified_bootstrap',
        'stratified_bootstrap_sha', 'stratified_bootstrap_hyperband'.

        Resampling methods with suffix 'sha' or 'hyperband' are only applicable to
        parameter selection, and currently these methods cannot be specified when
        ``multi_class`` is not True.

        If no value specified, neither model evaluation nor parameter selection is activated.

    metric : {'accuracy', 'f1_score', 'auc', 'nll'}, optional(deprecated)

        The evaluation metric used for model evaluation/parameter selection.

        Deprecated, please use ``evaluation_metric`` instead.

    evaluation_metric : {'accuracy', 'f1_score', 'auc', 'nll'}, optional

        The evaluation metric used for model evaluation/parameter selection.

        Must be specified together with ``resampling_method`` to activate
        model-evaluation/parameter-selection.

    fold_num : int, optional

        The number of folds for cross-validation.

        Mandatory and valid only when ``resampling_method`` is cross-validation
        based(contains 'cv' in part, e.g. 'cv', 'stratified_cv_sha').

    repeat_times : int, optional

        The number of repeat times for resampling.

        Defaults to 1.

    search_strategy : {'grid', 'random'}, optional

        The search method for parameter selection.

    random_search_times : int, optional

        The number of times to randomly select candidate parameters for selection.

        Mandatory and valid when ``search_strategy`` is 'random'.

    random_state : int, optional

        The seed for random generation. 0 indicates using system time as seed.

        Defaults to 0.

    progress_indicator_id : str, optional

        The ID of progress indicator for model evaluation/parameter selection.

        Progress indicator deactivated if no value provided.

    param_values : dict or list of tuples, optional

        Specifies values of specific parameters to be selected.

        Valid only when ``resampling_method`` and ``search_strategy`` are specified.

        Specific parameters can be `enet_lambda`, `enet_alpha`.

        No default value.

    param_range : dict or list of tuples, optional

        Specifies range of specific parameters to be selected.

        Valid only when ``resampling_method`` and ``search_strategy`` are specified.

        Specific parameters can be `enet_lambda`, `enet_alpha`.

        No default value.

    class_map0 : str, optional (deprecated)

        Categorical label to map to 0.

        ``class_map0`` is mandatory when ``label`` column type is VARCHAR or NVARCHAR

        Only valid when ``multi_class`` is False during binary class fit and score.

    class_map1 : str, optional (deprecated)

        Categorical label to map to 1.

        ``class_map1`` is mandatory when ``label`` column type is VARCHAR or NVARCHAR during binary class fit and score.

        Only valid when ``multi_class`` is False.

    json_export : bool, optional

        - False : Does not export multiple Logistic Regression model in JSON.
        - True : Exports multiple Logistic Regression model in JSON.

        Only valid when multi-class is True.

        Currently either PMML or JSON format model can be exported.
        JSON format is preferred if both formats are to be exported.

        Defaults to False.

    resource : str, optional
        Specifies the resource type used in successive-halving and hyperband algorithm for parameter selection:

          - 'max_iter'
          - 'max_pass_number'

        Mandatory and valid only when ``resampling_method`` is specified with suffix 'sha' or 'hyperband'.

        If ``multi_class`` is set as True, then currently only 'max_iter' is valid;
        otherwise if ``multi_class`` is False, then

          - 'max_pass_number' is valid only when the ``actual`` solver is 'stochastic'
          - 'max_iter' is valid for other solvers

    max_resource : int, optional
        Maximum allowed resource budget for single hyper-parameter candidate, must be greater than 0.

        Mandatory and valid only wen ``resource`` is set.

    min_resource_rate : float, optional
        Specifies the minimum required resource budget compared to maximum resource
        for single hyper-parameter candidate. Valid value should be greater than or equal to 0,
        but less than 1.

        Valid only when ``resource`` is set.

        Defaults to 0.

    reduction_rate : float, optional
        Specifies the reduction rate of available size of hyper-parameter candidates.
        For each round, the available parameter candidate size will be divided by value of this parameter.
        Thus valid value for this parameter must be greater than 1.0

        Valid only when ``resource`` is set.

        Defaults to 3.0.

    aggressive_elimination : bool, optional
        Specifies whether to perform aggressive elimination behavior for successive-halving algorithm or not.

        When set to True, it will eliminate more parameter candidates than expected(defined via ``reduction_rate``).
        This can enhance the run-time performance but could result in sub-optimal hyper-parameter candidate.

        Valid only when ``resampling_method`` is specified with suffix 'sha'.

        Defaults to False.

    ps_verbose : bool, optional
        Specifies whether to output optimal hyper-parameter and all evaluation statistics of related
        hyper-parameter candidates in attribute `statistics_` or not.

        Defaults to True.

    Attributes
    ----------

    coef_ : DataFrame

        Values of the coefficients.

    result_ : DataFrame

        Model content.

    optim_param_ : DataFrame

        The optimal parameter set selected via cross-validation.
        Empty if cross-validation is not activated.

    stat_ : DataFrame

        Statistics info for the trained model, structured as follows:

            - 1st column: 'STAT_NAME', NVARCHAR(256)
            - 2nd column: 'STAT_VALUE', NVARCHAR(1000)

    pmml_ : DataFrame

        PMML model. Set to None if no PMML model was requested.
        In multi-class logistic regression, Please use `semistructured_result_` shown below to
        get the model in PMMl or JSON format.

    semistructured_result_ : DataFrame

        A multi-class logistic regression model in PMML or JSON format.

    Examples
    --------

    Training data:

    >>> df.collect()
       V1     V2  V3  CATEGORY
    0   B  2.620   0         1
    1   B  2.875   0         1
    2   A  2.320   1         1
    3   A  3.215   2         0
    4   B  3.440   3         0
    5   B  3.460   0         0
    6   A  3.570   1         0
    7   B  3.190   2         0
    8   A  3.150   3         0
    9   B  3.440   0         0
    10  B  3.440   1         0
    11  A  4.070   3         0
    12  A  3.730   1         0
    13  B  3.780   2         0
    14  B  5.250   2         0
    15  A  5.424   3         0
    16  A  5.345   0         0
    17  B  2.200   1         1
    18  B  1.615   2         1
    19  A  1.835   0         1
    20  B  2.465   3         0
    21  A  3.520   1         0
    22  A  3.435   0         0
    23  B  3.840   2         0
    24  B  3.845   3         0
    25  A  1.935   1         1
    26  B  2.140   0         1
    27  B  1.513   1         1
    28  A  3.170   3         1
    29  B  2.770   0         1
    30  B  3.570   0         1
    31  A  2.780   3         1

    Create LogisticRegression instance and call fit:

    >>> lr = linear_model.LogisticRegression(solver='newton',
    ...                                      thread_ratio=0.1, max_iter=1000,
    ...                                      pmml_export='single-row',
    ...                                      stat_inf=True, tol=0.000001)
    >>> lr.fit(data=df, features=['V1', 'V2', 'V3'],
    ...        label='CATEGORY', categorical_variable=['V3'])
    >>> lr.coef_.collect()
                                           VARIABLE_NAME  COEFFICIENT
    0                                  __PAL_INTERCEPT__    17.044785
    1                                 V1__PAL_DELIMIT__A     0.000000
    2                                 V1__PAL_DELIMIT__B    -1.464903
    3                                                 V2    -4.819740
    4                                 V3__PAL_DELIMIT__0     0.000000
    5                                 V3__PAL_DELIMIT__1    -2.794139
    6                                 V3__PAL_DELIMIT__2    -4.807858
    7                                 V3__PAL_DELIMIT__3    -2.780918
    8  {"CONTENT":"{\"impute_model\":{\"column_statis...          NaN
    >>> pred_df.collect()
        ID V1     V2  V3
    0    0  B  2.620   0
    1    1  B  2.875   0
    2    2  A  2.320   1
    3    3  A  3.215   2
    4    4  B  3.440   3
    5    5  B  3.460   0
    6    6  A  3.570   1
    7    7  B  3.190   2
    8    8  A  3.150   3
    9    9  B  3.440   0
    10  10  B  3.440   1
    11  11  A  4.070   3
    12  12  A  3.730   1
    13  13  B  3.780   2
    14  14  B  5.250   2
    15  15  A  5.424   3
    16  16  A  5.345   0
    17  17  B  2.200   1


    Call predict():

    >>> result = lgr.predict(data=pred_df,
    ...                      key='ID',
    ...                      categorical_variable=['V3'],
    ...                      thread_ratio=0.1)
    >>> result.collect()
        ID CLASS   PROBABILITY
    0    0     1  9.503618e-01
    1    1     1  8.485210e-01
    2    2     1  9.555861e-01
    3    3     0  3.701858e-02
    4    4     0  2.229129e-02
    5    5     0  2.503962e-01
    6    6     0  4.945832e-02
    7    7     0  9.922085e-03
    8    8     0  2.852859e-01
    9    9     0  2.689207e-01
    10  10     0  2.200498e-02
    11  11     0  4.713726e-03
    12  12     0  2.349803e-02
    13  13     0  5.830425e-04
    14  14     0  4.886177e-07
    15  15     0  6.938072e-06
    16  16     0  1.637820e-04
    17  17     1  8.986435e-01

    Input data for score():

    >>> df_score.collect()
        ID V1     V2  V3  CATEGORY
    0    0  B  2.620   0         1
    1    1  B  2.875   0         1
    2    2  A  2.320   1         1
    3    3  A  3.215   2         0
    4    4  B  3.440   3         0
    5    5  B  3.460   0         0
    6    6  A  3.570   1         1
    7    7  B  3.190   2         0
    8    8  A  3.150   3         0
    9    9  B  3.440   0         0
    10  10  B  3.440   1         0
    11  11  A  4.070   3         0
    12  12  A  3.730   1         0
    13  13  B  3.780   2         0
    14  14  B  5.250   2         0
    15  15  A  5.424   3         0
    16  16  A  5.345   0         0
    17  17  B  2.200   1         1


    Call score():

    >>> lgr.score(data=df_score,
    ...           key='ID',
    ...           categorical_variable=['V3'],
    ...           thread_ratio=0.1)
    0.944444
    """
    solver_map = {'auto':-1, 'newton':0, 'cyclical':2, 'lbfgs':3, 'stochastic':4, 'proximal':6}
    multi_solver_map = {'auto': None, 'lbfgs': 0, 'cyclical': 1}
    pmml_map_multi = {'no': 0, 'multi-row': 1}
    pmml_map_binary = {'no': 0, 'single-row': 1, 'multi-row': 2}
    valid_metric_map = {'accuracy':'ACCURACY', 'f1_score':'F1_SCORE', 'auc':'AUC', 'nll':'NLL'}
    resource_map = {'max_iter': 'MAX_ITERATION', 'max_pass_number': 'MAX_PASS_NUMBER',
                    'automatic': 'MAX_ITERATION'}
    values_list = {"enet_alpha": "ENET_ALPHA", "enet_lambda": "ENET_LAMBDA"}
    resampling_method_list = ['cv', 'cv_sha', 'cv_hyperband',
                              'stratified_cv', 'stratified_cv_sha',
                              'stratified_cv_hyperband',
                              'bootstrap', 'bootstrap_sha',
                              'bootstrap_hyperband',
                              'stratified_bootstrap',
                              'stratified_bootstrap_sha',
                              'stratified_bootstrap_hyperband']
    #pylint:disable=too-many-arguments, too-many-branches, too-many-statements
    def __init__(self,
                 multi_class=False,
                 max_iter=None,
                 pmml_export=None,
                 categorical_variable=None,
                 standardize=True,
                 stat_inf=False,
                 solver=None,
                 enet_alpha=None,
                 enet_lambda=None,
                 tol=None,
                 epsilon=None,
                 thread_ratio=None,
                 max_pass_number=None,
                 sgd_batch_number=None,
                 precompute=None,#adding new parameters
                 handle_missing=None,
                 resampling_method=None,
                 metric=None,
                 evaluation_metric=None,
                 fold_num=None,
                 repeat_times=None,
                 search_strategy=None,
                 random_search_times=None,
                 random_state=None,
                 timeout=None,
                 lbfgs_m=None,
                 class_map0=None,
                 class_map1=None,
                 progress_indicator_id=None,
                 param_values=None,
                 param_range=None,
                 json_export=None,
                 resource=None,
                 max_resource=None,
                 min_resource_rate=None,
                 reduction_rate=None,
                 aggressive_elimination=None,
                 ps_verbose=None):
        #pylint:disable=too-many-locals
        super(LogisticRegression, self).__init__()
        setattr(self, 'hanaml_parameters', pal_param_register())
        self.pal_funcname = 'PAL_LOGISTIC_REGRESSION'
        self.op_name = 'M_LOGR_Classifier'
        self.multi_class = self._arg('multi_class', multi_class, bool)
        self.max_iter = self._arg('max_iter', max_iter, int)
        if self.multi_class:
            pmml_map = self.pmml_map_multi
            solver_map = self.multi_solver_map
            self.pal_funcname = 'PAL_MULTICLASS_LOGISTIC_REGRESSION'
        else:
            pmml_map = self.pmml_map_binary
            solver_map = self.solver_map
            #solver = 'newton' if solver is None else solver#maybe something wrong here
        self.pmml_export = self._arg('pmml_export', pmml_export, pmml_map)
        self.json_export = self._arg('json_export', json_export, bool)
        if isinstance(categorical_variable, str):
            categorical_variable = [categorical_variable]
        self.categorical_variable = self._arg('categorical_variable', categorical_variable,
                                              ListOfStrings)
        self.standardize = self._arg('standardize', standardize, bool)
        self.stat_inf = self._arg('stat_inf', stat_inf, bool)
        binary_params = {'epsilon': epsilon, 'max_pass_number': max_pass_number,
                         'sgd_batch_number': sgd_batch_number, 'lbfgs_m': lbfgs_m,
                         'class_map0': class_map0, 'class_map1': class_map1}
        self._check_params_for_binary(binary_params)
        self.solver = self._arg('solver', solver, solver_map)
        self.enet_alpha = self._arg('enet_alpha', enet_alpha, float)
        self.enet_lambda = self._arg('enet_lambda', enet_lambda, float)
        enet_alpha = 1.0 if enet_alpha is None else enet_alpha
        enet_lambda = 0.0 if enet_lambda is None else enet_lambda
        self.tol = self._arg('tol', tol, float)#Corresponds to EXIT_THRESHOLD
        self.epsilon = self._arg('epsilon', epsilon, float)
        self.thread_ratio = self._arg('thread_ratio', thread_ratio, float)
        self.max_pass_number = self._arg('max_pass_number', max_pass_number, int)
        self.sgd_batch_number = self._arg('sgd_batch_number', sgd_batch_number, int)
        self.precompute = self._arg('precompute', precompute, bool)
        self.handle_missing = self._arg('handle_missing', handle_missing, bool)
        self.resampling_method = self._arg('resampling_method', resampling_method, str)
        if self.resampling_method is not None:
            self.resampling_method = self.resampling_method.lower()
            if self.resampling_method not in self.resampling_method_list:
                msg = ("Resampling method '{}' is not supported ".format(self.resampling_method) +
                       "for model evaluation or parameter selection.")
                logger.error(msg)
                raise ValueError(msg)
        self.metric = self._arg('metric', metric, self.valid_metric_map)
        self.evaluation_metric = self._arg('evaluation_metric', evaluation_metric,
                                           self.valid_metric_map)
        self.fold_num = self._arg('fold_num', fold_num, int,
                                  required = 'cv' in str(self.resampling_method).lower())
        self.repeat_times = self._arg('repeat_times', repeat_times, int)
        self.search_strategy = self._arg('search_stategy', search_strategy, str)
        if self.search_strategy is not None:
            if self.search_strategy not in ('grid', 'random'):
                msg = ("Search strategy '{}' is not available for ".format(self.search_strategy)+
                       "parameter selection.")
                logger.error(msg)
                raise ValueError(msg)
        if 'hyperband' in str(self.resampling_method):
            self.search_strategy = 'random'
        self.random_search_times = self._arg('random_search_times', random_search_times, int)
        self.random_state = self._arg('random_state', random_state, int)
        self.timeout = self._arg('timeout', timeout, int)
        self.lbfgs_m = self._arg('lbfgs_m', lbfgs_m, int)
        self.class_map0 = self._arg('class_map0', class_map0, str)
        self.class_map1 = self._arg('class_map1', class_map1, str)
        self.progress_indicator_id = self._arg('progress_indicator_id', progress_indicator_id, str)
        if isinstance(param_range, dict):
            param_range = [(x, param_range[x]) for x in param_range]
        if isinstance(param_values, dict):
            param_values = [(x, param_values[x]) for x in param_values]
        self.param_range = self._arg('param_range', param_range, ListOfTuples)
        self.param_values = self._arg('param_values', param_values, ListOfTuples)
        if self.search_strategy is None:
            if self.param_values is not None:
                msg = ("`param_values` can only be specified "+
                       "when `search_strategy` is enabled.")
                logger.error(msg)
                raise ValueError(msg)
            if self.param_range is not None:
                msg = ("`param_range` can only be specified "+
                       "when `search_strategy` is enabled.")
                logger.error(msg)
                raise ValueError(msg)
        if self.search_strategy is not None:
            set_param_list = []
            if self.enet_lambda is not None:
                set_param_list.append("enet_lambda")
            if self.enet_alpha is not None:
                set_param_list.append("enet_alpha")
            if self.param_values is not None:
                for x in self.param_values:#pylint:disable=invalid-name
                    if len(x) != 2:#pylint:disable=bad-option-value
                        msg = ("Each tuple that specifies the values of a parameter should"+
                               " contain exactly 2 elements: 1st is parameter name,"+
                               " 2nd is a list of valid values.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] not in self.values_list:
                        msg = ("Specifying the values of `{}` for ".format(x[0])+
                               "parameter selection is invalid.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] in set_param_list:
                        msg = ("Parameter `{}` is invalid for ".format(x[0])+
                               "re-specification in parameter selection.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if not (isinstance(x[1], list) and all(isinstance(t, (int, float)) for t in x[1])):#pylint:disable=line-too-long
                        msg = "Valid values of `{}` must be a list of numerical values.".format(x[0])
                        logger.error(msg)
                        raise TypeError(msg)
                    set_param_list.append(x[0])
            if self.param_range is not None:
                if "enet_lambda" in [x[0] for x in self.param_range]:
                    enet_lambda = 1.0#only physically
                elif "enet_alpha" in [x[0] for x in self.param_range]:
                    enet_lambda = 1.0#only physically
                rsz = [3] if self.search_strategy == 'grid' else [2, 3]
                for x in self.param_range:#pylint:disable=invalid-name
                    if len(x) != 2:#pylint:disable=bad-option-value
                        msg = ("Each tuple that specifies the range of a parameter should contain"+
                               " exactly 2 elements: 1st is parameter name, 2nd is value range.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] not in self.values_list:
                        msg = ("Specifying the values of `{}` for ".format(x[0])+
                               "parameter selection is invalid.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if x[0] in set_param_list:
                        msg = ("Parameter `{}` is invalid for ".format(x[0])+
                               "re-specification in parameter selection.")
                        logger.error(msg)
                        raise ValueError(msg)
                    if not (isinstance(x[1], list) and len(x[1]) in rsz and all(isinstance(t, (int, float)) for t in x[1])):#pylint:disable=line-too-long
                        msg = ("The provided `{}` is either not ".format(x[0])+
                               "a list of numerical values, or it contains wrong number of values.")
                        logger.error(msg)
                        raise TypeError(msg)
        lasso_flag = enet_alpha * enet_lambda
        if self.multi_class is not True:
            if solver in ['newton', 'stochastic'] and lasso_flag:
                self.solver = None
        self.resource, self.max_resource, self.reduction_rate = None, None, None
        self.aggressive_elimination, self.ps_verbose, self.min_resource_rate = None, None, None
        if self.resampling_method is not None and any(x in self.resampling_method for x in ['sha', 'hyper']):
            self.resource = self._arg('resource', resource,
                                      dict(max_iter='MAX_ITERATION') if self.multi_class else self.resource_map,
                                      required = True)
            if self.solver != 4 and self.resource == 'MAX_PASS_NUMBER':
                msg = "'max_pass_number' is not a valid resource name under current choice of solver."
                logger.error(msg)
                raise ValueError(msg)
            elif self.solver == 4 and self.resource == 'MAX_ITERATION':
                msg = "'max_iter' is not a valid resource name under stochastic solver."
                logger.error(msg)
                raise ValueError(msg)
            if self.solver in [None, -1] and self.resource == 'MAX_PASS_NUMBER':
                self.resource = 'MAX_ITERATION'
            self.max_resource = self._arg('max_resource', max_resource, int,
                                          required = self.resource is not None)
            self.min_resource_rate = self._arg('min_resource_rate',
                                               min_resource_rate, float)
            self.reduction_rate = self._arg('reduction_rate', reduction_rate, float)
            self.aggressive_elimination = self._arg('aggressive_elimination',
                                                    aggressive_elimination,
                                                    bool)
            self.ps_verbose = self._arg('ps_verbose', ps_verbose, bool)
        self.label_type = None

    #pylint:disable=too-many-locals, too-many-statements, invalid-name
    @trace_sql
    def fit(self,
            data,
            key=None,
            features=None,
            label=None,
            categorical_variable=None,
            class_map0=None,
            class_map1=None):
        r"""
        Fit the LR model when given training dataset.

        Parameters
        ----------

        data : DataFrame

            DataFrame containing the data.

        key : str, optional

            Name of the ID column.

            If ``key`` is not provided, then:

            - if ``data`` is indexed by a single column, then ``key`` defaults
              to that index column;

            - otherwise, it is assumed that ``data`` contains no ID column.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID,
            non-label columns.

        label : str, optional

            Name of the label column.

            If ``label`` is not provided, it defaults to the last column.

        categorical_variable : str or list of str, optional

            Specifies INTEGER column(s) that should be treated as categorical.

            Otherwise All INTEGER columns are treated as numerical.

        class_map0 : str, optional

            Categorical label to map to 0.

            ``class_map0`` is mandatory when ``label`` column type is VARCHAR or NVARCHAR during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.

        class_map1 : str, optional

            Categorical label to map to 1.

            ``class_map1`` is mandatory when ``label`` column type is VARCHAR or NVARCHAR during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.


        Returns
        -------
        LogisticRegression

            A fitted object.
        """
        setattr(self, 'hanaml_fit_params', pal_param_register())
        conn = data.connection_context
        require_pal_usable(conn)
        key = self._arg('key', key, str)
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        class_map0 = self._arg('class_map0', class_map0, str)
        class_map1 = self._arg('class_map1', class_map1, str)
        if class_map0 is not None:
            self.class_map0 = class_map0
        if class_map1 is not None:
            self.class_map1 = class_map1
        if not self._disable_hana_execution:
            cols = data.columns
            if key is not None:
                cols.remove(key)
            if label is None:
                label = cols[-1]
            self.label_type = data.dtypes([label])[0][1]
            cols.remove(label)
            if features is None:
                features = cols
            if not self.multi_class:
                self._check_label_sql_type(data, label)
            used_cols = [col for col in itertools.chain([key], features, [label])
                        if col is not None]
            data_ = data[used_cols]
        else:
            data_ = data

        if isinstance(categorical_variable, str):
            categorical_variable = [categorical_variable]
        categorical_variable = self._arg('categorical_variable', categorical_variable, ListOfStrings)
        if categorical_variable is not None:
            self.categorical_variable = categorical_variable

        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        outputs = ['#LR_{}_TBL_{}_{}'.format(name, self.id, unique_id)
                   for name in ['RESULT', 'PMML', 'STAT', 'OPTIM']]
        result_tbl, pmml_tbl, stat_tbl, optim_tbl = outputs
        param_rows = [('MAX_ITERATION', self.max_iter, None, None),
                      ('PMML_EXPORT', self.pmml_export, None, None),
                      ('HAS_ID', key is not None, None, None),
                      ('STANDARDIZE', self.standardize, None, None),
                      ('STAT_INF', self.stat_inf, None, None),
                      ('ENET_ALPHA', None, self.enet_alpha, None),
                      ('ENET_LAMBDA', None, self.enet_lambda, None),
                      ('EXIT_THRESHOLD', None, self.tol, None),
                      ('METHOD', self.solver, None, None),
                      ('RESAMPLING_METHOD', None, None, self.resampling_method),
                      ('EVALUATION_METRIC', None, None,
                       self.metric if self.evaluation_metric is None else self.evaluation_metric),
                      ('FOLD_NUM', self.fold_num, None, None),
                      ('REPEAT_TIMES', self.repeat_times, None, None),
                      ('PARAM_SEARCH_STRATEGY', None, None, self.search_strategy),
                      ('RANDOM_SEARCH_TIMES', self.random_search_times, None, None),
                      ('SEED', self.random_state, None, None),
                      ('TIMEOUT', self.timeout, None, None),
                      ('THREAD_RATIO', None, self.thread_ratio, None),
                      ('PROGRESS_INDICATOR_ID', None, None, self.progress_indicator_id),
                      ('RESOURCE', None, None, self.resource),
                      ('MAX_RESOURCE', self.max_resource, None, None),
                      ('MIN_RESOURCE_RATE', None, self.min_resource_rate, None),
                      ('REDUCTION_RATE', None, self.reduction_rate, None),
                      ('AGGRESSIVE_ELIMINATION', self.aggressive_elimination,
                       None, None),
                      ('PS_VERBOSE', self.ps_verbose, None, None)]
        if self.param_values is not None:
            for x in self.param_values:#pylint:disable=invalid-name
                values = str(x[1]).replace('[', '{').replace(']', '}')
                param_rows.extend([(self.values_list[x[0]]+"_VALUES",
                                    None, None, values)])
        if self.param_range is not None:
            for x in self.param_range:#pylint:disable=invalid-name
                range_ = str(x[1])
                if len(x[1]) == 2 and self.search_strategy == 'random':
                    range_ = range_.replace(',', ',,')
                param_rows.extend([(self.values_list[x[0]]+"_RANGE",
                                    None, None, range_)])
        if self.categorical_variable is not None:
            param_rows.extend([('CATEGORICAL_VARIABLE', None, None, col)
                               for col in self.categorical_variable])
        if self.multi_class:
            proc_name = 'PAL_MULTICLASS_LOGISTIC_REGRESSION'
            coef_list = ['VARIABLE_NAME', 'CLASS', 'COEFFICIENT']
            param_rows.extend([('JSON_EXPORT', self.json_export, None, None)])
        else:
            proc_name = "PAL_LOGISTIC_REGRESSION"
            coef_list = ['VARIABLE_NAME', 'COEFFICIENT']
            param_rows.extend([('EPSILON', None, self.epsilon, None),
                               ('MAX_PASS_NUMBER', self.max_pass_number, None, None),
                               ('SGD_BATCH_NUMBER', self.sgd_batch_number, None, None),
                               ('PRECOMPUTE', self.precompute, None, None),
                               ('HANDLE_MISSING', self.handle_missing, None, None),
                               ('LBFGS_M', self.lbfgs_m, None, None)])
            if not self._disable_hana_execution:
                if self.label_type in ('VARCHAR', 'NVARCHAR'):
                    param_rows.extend([('CLASS_MAP1', None, None, self.class_map1),
                                       ('CLASS_MAP0', None, None, self.class_map0)])
            else:
                param_rows.extend([('CLASS_MAP1', None, None, self.class_map1),
                                   ('CLASS_MAP0', None, None, self.class_map0)])
        try:
            self._call_pal_auto(conn,
                                proc_name,
                                data_,
                                ParameterTable().with_data(param_rows),
                                result_tbl,
                                pmml_tbl,
                                stat_tbl,
                                optim_tbl)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, result_tbl)
            try_drop(conn, pmml_tbl)
            try_drop(conn, stat_tbl)
            try_drop(conn, optim_tbl)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, result_tbl)
            try_drop(conn, pmml_tbl)
            try_drop(conn, stat_tbl)
            try_drop(conn, optim_tbl)
            raise
        #pylint:disable=attribute-defined-outside-init
        self.result_ = conn.table(result_tbl)
        if not self._disable_hana_execution:
            self.coef_ = self.result_.select(coef_list)
        self.pmml_ = conn.table(pmml_tbl) if self.pmml_export else None
        if self.multi_class:
            self.semistructured_result_ = self.pmml_
        self.optim_param_ = conn.table(optim_tbl)
        self.stat_ = conn.table(stat_tbl)
        self.model_ = self.result_
        return self

    @trace_sql
    def predict(self,
                data,
                key=None,
                features=None,
                categorical_variable=None,
                thread_ratio=None,
                class_map0=None,
                class_map1=None,
                verbose=False,
                ignore_unknown_category=None):
        #pylint:disable=too-many-locals
        r"""
        Predict with the dataset using the trained model.

        Parameters
        ----------

        data : DataFrame

            DataFrame containing the data.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID columns.

        verbose : bool, optional

            If True, output scoring probabilities for each class.

            It is only applicable for multi-class case.

            Defaults to False.

        categorical_variable : str or list of str, optional (deprecated)

            Specifies INTEGER column(s) that should be treated as categorical.

            Otherwise all integer columns are treated as numerical.

            Mandatory if training data of the prediction model contains such
            data columns.

        thread_ratio : float, optional

            Controls the proportion of available threads to use.

            The value range is from 0 to 1, where 0 means only using 1 thread, and 1 means using at most all the currently available threads.

            Values outside this range tell pal to heuristically determine the number of threads to use.

            Defaults to 0.

        class_map0 : str, optional

            Categorical label to map to 0.

            ``class_map0`` is mandatory when ``label`` column type is varchar or nvarchar during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.

        class_map1 : str, optional

            Categorical label to map to 1.

            ``class_map1`` is mandatory when ``label`` column type is varchar or nvarchar during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.

        ignore_unknown_category : bool, optional
            Specifies whether or not to ignore unknown category value.

              - False : Report error if unknown category value is found.
              - True : Ignore unknown category value if there is any.

            Valid only for multi-class logistic regression.

            Defaults to True.

        Returns
        -------

        DataFrame
            Predicted result, structured as follows:

            - Column 1: ID
            - Column 2: Predicted class label
            - Column 3: PROBABILITY, type DOUBLE

              - for multi-class: probability of being predicted as the predicted class.
              - for binary-class: probability of being predicted as the positive class.

        """
        conn = data.connection_context

        if getattr(self, 'pmml_', None) is not None:
            model = self.pmml_
        elif getattr(self, 'model_') is not None:
            model = self.model_
        else:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")
        index = data.index
        key = self._arg('key', key, str, required=not isinstance(index, str))
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        verbose = self._arg('verbose', verbose, bool)
        thread_ratio = self._arg('thread_ratio', thread_ratio, float)
        ignore_unknown_category = self._arg('ignore_unknown_category',
                                            ignore_unknown_category,
                                            bool)
        unique_id = str(uuid.uuid1()).replace('-', '_').upper()

        cols = data.columns
        cols.remove(key)
        if features is None:
            features = cols
        data_ = data[[key] + features]

        result_tbl = '#LR_PREDICT_RESULT_TBL_{}_{}'.format(self.id, unique_id)
        if self.multi_class:
            param_array = [('VERBOSE_OUTPUT', verbose, None, None)]
            proc_name = 'PAL_MULTICLASS_LOGISTIC_REGRESSION_PREDICT'
        else:
            param_array = [('THREAD_RATIO', None, thread_ratio, None),
                           ('IGNORE_UNKNOWN_CATEGORY', ignore_unknown_category,
                            None, None)]
            if categorical_variable is not None:
                param_array.extend([('CATEGORICAL_VARIABLE', None, None, variable)
                                    for variable in categorical_variable])
            if self.categorical_variable is not None:
                param_array.extend([('CATEGORICAL_VARIABLE', None, None, variable)
                                    for variable in self.categorical_variable])
            if class_map0 is not None:
                param_array.extend([('CLASS_MAP0', None, None, class_map0),
                                    ('CLASS_MAP1', None, None, class_map1)])
            elif self.class_map0 is not None:
                param_array.extend([('CLASS_MAP0', None, None, self.class_map0),
                                    ('CLASS_MAP1', None, None, self.class_map1)])
            else:
                param_array.extend([('CLASS_MAP0', None, None, '0'),
                                    ('CLASS_MAP1', None, None, '1')])
            proc_name = 'PAL_LOGISTIC_REGRESSION_PREDICT'
        try:
            self._call_pal_auto(conn,
                                proc_name,
                                data_,
                                model,
                                ParameterTable().with_data(param_array),
                                result_tbl)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, result_tbl)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, result_tbl)
            raise
        result = conn.table(result_tbl)
        if not self._disable_hana_execution:
            if result.has('SCORE'):
                result = result.rename_columns({'SCORE': 'PROBABILITY'})
            result = result[[key, 'CLASS', 'PROBABILITY']]
        return result

    def score(self,
              data,
              key=None,
              features=None,
              label=None,
              categorical_variable=None,
              thread_ratio=None,
              class_map0=None,
              class_map1=None):
        r"""
        Return the mean accuracy on the given test data and labels.

        Parameters
        ----------

        data : DataFrame

            DataFrame containing the data.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID,
            non-label columns.

        label : str, optional

            Name of the label column.

            If ``label`` is not provided, it defaults to the last column.

        categorical_variable : str or list of str, optional (deprecated)

            Specifies INTEGER columns that should be treated as categorical, otherwise all integer columns are treated as numerical.

            Mandatory if training data of the prediction model contains such data columns.

        thread_ratio : float, optional

            Controls the proportion of available threads to use.

            The value range is from 0 to 1, where 0 means only using 1 thread, and 1 means using at most all the currently available threads.

            values outside this range tell pal to heuristically determine the number of threads to use.

            Defaults to 0.

        class_map0 : str, optional

            Categorical label to map to 0.

            ``class_map0`` is mandatory when ``label`` column type is varchar or nvarchar during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.

        class_map1 : str, optional

            Categorical label to map to 1.

            ``class_map1`` is mandatory when ``label`` column type is varchar or nvarchar during binary class fit and score.

            Only valid if ``multi_class`` is not set to True when initializing the class instance.

        Returns
        -------
        float

            Scalar accuracy value after comparing the predicted label
            and original label.
        """
        index = data.index
        key = self._arg('key', key, str, required=not isinstance(index, str))
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        if isinstance(categorical_variable, str):
            categorical_variable = [categorical_variable]
        categorical_variable = self._arg('categorical_variable',
                                         categorical_variable,
                                         ListOfStrings)
        thread_ratio = self._arg('thread_ratio', thread_ratio, float)
        cols = data.columns
        cols.remove(key)
        if label is None:
            label = cols[-1]
        cols.remove(label)
        if features is None:
            features = cols
        if not self.multi_class:
            self._check_label_sql_type(data, label)

        prediction = self.predict(data=data, key=key,
                                  features=features,
                                  categorical_variable=categorical_variable,
                                  thread_ratio=thread_ratio,
                                  class_map0=class_map0,
                                  class_map1=class_map1)
        prediction = prediction.select(key, 'CLASS').rename_columns(['ID_P', 'PREDICTION'])
        actual = data.select(key, label).rename_columns(['ID_A', 'ACTUAL'])
        joined = actual.join(prediction, 'ID_P=ID_A').select('ACTUAL', 'PREDICTION')
        return metrics.accuracy_score(joined,
                                      label_true='ACTUAL',
                                      label_pred='PREDICTION')

    def _check_label_sql_type(self, data, label):
        label_sql_type = parse_one_dtype(data.dtypes([label])[0])[1]
        if label_sql_type.startswith("NVARCHAR") or label_sql_type.startswith("VARCHAR"):
            if self.class_map0 is None or self.class_map1 is None:
                msg = ("class_map0 and class_map1 are mandatory when `label` column type " +
                       "is VARCHAR or NVARCHAR.")
                logger.error(msg)
                raise ValueError(msg)

    def _check_params_for_binary(self, params):
        for name in params:
            msg = 'Parameter {} is only applicable for binary classification.'.format(name)
            if params[name] is not None and self.multi_class:
                logger.error(msg)
                raise ValueError(msg)

    def create_model_state(self, model=None, function=None,
                           pal_funcname=None,
                           state_description=None, force=False):
        r"""
        Create PAL model state.

        Parameters
        ----------
        model : DataFrame, optional
            Specify the model for AFL state.

            Defaults to self.model\_.

        function : str, optional
            Specify the function in the unified API.

            A placeholder parameter, not effective for CRF.

        pal_funcname : int or str, optional
            PAL function name. Must be a valid PAL procedure that supports model state.

            Defaults to `self.pal_funcname`.

        state_description : str, optional
            Description of the state as model container.

            Defaults to None.

        force : bool, optional
            If True it will delete the existing state.

            Defaults to False.
        """
        super()._create_model_state(model, function, pal_funcname, state_description, force)

    def set_model_state(self, state):
        """
        Set the model state by state information.

        Parameters
        ----------
        state: DataFrame or dict
            If state is DataFrame, it has the following structure:

                - NAME: VARCHAR(100), it mush have STATE_ID, HINT, HOST and PORT.
                - VALUE: VARCHAR(1000), the values according to NAME.

            If state is dict, the key must have STATE_ID, HINT, HOST and PORT.
        """
        super()._set_model_state(state)

    def delete_model_state(self, state=None):
        """
        Delete PAL model state.

        Parameters
        ----------
        state : DataFrame, optional
            Specified the state.

            Defaults to self.state.
        """
        super()._delete_model_state(state)

class OnlineMultiLogisticRegression(PALBase):
    r"""
    This algorithm is the online version of Multi-Class Logistic Regression,
    while the Multi-Class Logistic Regression is offline/batch version.
    The difference is that during training phase, for the offline/batch version algorithm
    it requires all training data to be fed into the algorithm in one batch,
    then it tries its best to output one model to best fit the training data.
    This infers that the computer must have enough memory to store all data,
    and can obtain all data in one batch. Online version algorithm applies
    in scenario that either or all these two assumptions are not right.


    Parameters
    ----------
    class_label : a list of str
        Indicates the class label and should be at least two class labels.

    init_learning_rate : float
        The initial learning rate for learning rate schedule. Value should be larger than 0.

        Only valid when ``learning_rate_type`` is 'Inverse_time_decay', 'Exponential_decay', 'Polynomial_decay'.

    decay : float
        Specify the learning rate decay speed for learning rate schedule. Larger value indicates faster decay.
        Value should be larger than 0. When ``learning_rate_type`` is 'exponential_decay', value should be larger than 1.

        Only valid when ``learning_rate_type`` is 'Inverse_time_decay', 'Exponential_decay', 'Polynomial_decay'.

    drop_rate : int

        Specify the decay frequency. There are apparent effect when ``stair_case`` is True.
        Value should be larger than 0.

        Only valid when ``learning_rate_type`` is 'Inverse_time_decay', 'Exponential_decay', 'Polynomial_decay'.

    step_boundaries : list of int, optional

        Specify the step boundaries for regions where step size remains constant.
        The format of this parameter is a list of integers.

        The step value start from 0(no need to be specified), and
        the values should be in ascending order(e. g. [5, 8, 15, 23]).

        Empty value for this parameter is allowed.

        Only valid when ``learning_rate_type`` is 'Piecewise_constant_decay'.

    constant_values : list of float, optional

        Specifies the constant values for each region defined by ``step_boundaries``.
        The format of this parameter is a list of float numbers.

        There should always be one more value than ``step_boundaries``
        since `n` boundary points should give out `n+1` regions in total.

        Only valid when ``learning_rate_type`` is 'Piecewise_constant_decay'.

    enet_alpha : float, optional
        Elastic-Net mixing parameter.
        The valid range is [0, 1]. When it is 0, this means Ridge penalty;
        When it is 1, it is Lasso penalty.

        Only valid when ``enet_lambda`` is not 0.0.

        Defaults to 1.0.

    enet_lambda : float, optional
        Penalized constant. The value should be larger than or equal to 0.0.
        The higher the value, the stronger the regularization.
        When it equal to 0.0, there is no regularization.

        Defaults to 0.0.

    shuffle : bool, optonal
        Boolean value indicating whether need to shuffle the row order of observation data.
        False means keeping original order; True means performing shuffle operation.

        Defaults to False.

    shuffle_seed : int, optonal
        The seed is used to initialize the random generator to perform shuffle operation.
        The value of this parameter should be larger than or equal to 0.
        If need to reproduce the result when performing shuffle operation,
        please set this value to non-zero.
        Only valid when ``shuffle`` is True.

        Defaults to 0.

    weight_avg : bool, optonal
        Boolean value indicating whether need to perform average operator over output model.
        False means directly output model;
        True means perform average operator over output model.
        Currently only support Polyak Ruppert Average.

        Defaults to False.

    weight_avg_begin : int, optonal
        Specify the beginning step counter to perform the average operator over model.
        The value should be larger than or equal to 0. When current step counter is less than this parameter,
        just directly output model.Only valid when ``weight_avg`` is True.

        Defaults to 0.

    learning_rate_type : str, optonal
        Specify the learning rate type for SGD algorithm.

         - 'Inverse_time_decay'
         - 'Exponential_decay'
         - 'Polynomial_decay'
         - 'Piecewise_constant_decay'
         - 'AdaGrad'
         - 'AdaDelta'
         - 'RMSProp'

        Defaults to 'RMSProp'.

    general_learning_rate : float, optonal
        Specify the general learning rate used in AdaGrad and RMSProp.
        The value should be larger than 0.

        Only valid when ``learning_rate_type`` is 'AdaGrad', 'RMSProp'.

        Defaults to 0.001.

    stair_case : bool, optonal
        Boolean value indicate the drop way of step size. False means drop step size smoothly.

        Only valid when ``learning_rate_type`` is 'Inverse_time_decay', 'Exponential_decay'.

        Defaults to False.

    cycle : bool, optonal
        indicate whether need to cycle from the start when reaching specified end learning rate.
        False means do not cycle from the start; True means cycle from the start.

        Only valid when ``learning_rate_type`` is 'Polynomial_decay'.

        Defaults to False.

    epsilon : float, optonal
        This parameter has multiple purposes depending on the learn rate type.
        The value should be within (0, 1). When used in learn rate type 0 and 1, it represent the smallest allowable step size.
        When step size reach this value, it will no longer change.
        When used in ``learning_rate_type`` 'Polynomial_decay', it represent the end learn rate.
        When used in ``learning_rate_type`` 'AdaGrad', 'AdaDelta', 'RMSProp', it is used to avoid dividing by 0.

        Only valid when ``learning_rate_type`` is not 'Piecewise_constant_decay'.

        Defaults to 1E-8.

    window_size : float, optonal
        This parameter controls the moving window size of recent steps. The value should be in range (0, 1).
        Larger value means more steps are kept in track.

        Only valid when ``learning_rate_type`` is 'AdaDelta', 'RMSProp'.

        Defaults to 0.9.

    Attributes
    ----------
    coef_ : DataFrame
        Values of the coefficients.

    online_result_ : DataFrame
        Online Model content.

    Examples
    --------
    First, initialize an online multi logistic regression instance:

    >>> omlr = OnlineMultiLogisticRegression(class_label=['0','1','2'], enet_lambda=0.01,
                                             enet_alpha=0.2, weight_avg=True,
                                             weight_avg_begin=8, learning_rate_type = 'rmsprop',
                                             general_learning_rate=0.1,
                                             window_size=0.9, epsilon = 1e-6)

    Four rounds of data:

    >>> df_1.collect()
             X1        X2    Y
    0  1.160456 -0.079584  0.0
    1  1.216722 -1.315348  2.0
    2  1.018474 -0.600647  1.0
    3  0.884580  1.546115  1.0
    4  2.432160  0.425895  1.0
    5  1.573506 -0.019852  0.0
    6  1.285611 -2.004879  1.0
    7  0.478364 -1.791279  2.0

    >>> df_2.collect()
             X1        X2    Y
    0 -1.799803  1.225313  1.0
    1  0.552956 -2.134007  2.0
    2  0.750153 -1.332960  2.0
    3  2.024223 -1.406925  2.0
    4  1.204173 -1.395284  1.0
    5  1.745183  0.647891  0.0
    6  1.406053  0.180530  0.0
    7  1.880983 -1.627834  2.0

    >>> df_3.collect()
             X1        X2    Y
    0  1.860634 -2.474313  2.0
    1  0.710662 -3.317885  2.0
    2  1.153588  0.539949  0.0
    3  1.297490 -1.811933  2.0
    4  2.071784  0.351789  0.0
    5  1.552456  0.550787  0.0
    6  1.202615 -1.256570  2.0
    7 -2.348316  1.384935  1.0

    >>> df_4.collect()
             X1        X2    Y
    0 -2.132380  1.457749  1.0
    1  0.549665  0.174078  1.0
    2  1.422629  0.815358  0.0
    3  1.318544  0.062472  0.0
    4  0.501686 -1.286537  1.0
    5  1.541711  0.737517  1.0
    6  1.709486 -0.036971  0.0
    7  1.708367  0.761572  0.0

    Round 1, invoke partial_fit() for training the model with df_1:

    >>> omlr.partial_fit(self.df_1, label='Y', features=['X1', 'X2'])

    Output:

    >>> omlr.coef_.collect()
           VARIABLE_NAME CLASSLABEL  COEFFICIENT
    0  __PAL_INTERCEPT__          0    -0.245137
    1  __PAL_INTERCEPT__          1     0.112396
    2  __PAL_INTERCEPT__          2    -0.236284
    3                 X1          0    -0.189930
    4                 X1          1     0.218920
    5                 X1          2    -0.372500
    6                 X2          0     0.279547
    7                 X2          1     0.458214
    8                 X2          2    -0.185378


    >>> omlr.online_result_.collect()
       SEQUENCE                          UPDATED_SERIALIZED_RESULT
    0         0  {"SGD":{"data":{"avg_feature_coefficient":[0.0...

    Round 2, invoke partial_fit() for training the model with df_2:

    >>> omlr.partial_fit(self.df_2, label='Y', features=['X1', 'X2'])

    Output:

    >>> omlr.coef_.collect()
            VARIABLE_NAME CLASSLABEL  COEFFICIENT
    0  __PAL_INTERCEPT__          0    -0.359296
    1  __PAL_INTERCEPT__          1     0.163218
    2  __PAL_INTERCEPT__          2    -0.182423
    3                 X1          0    -0.045149
    4                 X1          1    -0.046508
    5                 X1          2    -0.122690
    6                 X2          0     0.420425
    7                 X2          1     0.594954
    8                 X2          2    -0.451050


    >>> omlr.online_result_.collect()
       SEQUENCE                          UPDATED_SERIALIZED_RESULT
    0         0  {"SGD":{"data":{"avg_feature_coefficient":[-0....

    Round 3, invoke partial_fit() for training the model with df_3:

    >>> omlr.partial_fit(self.df_3, label='Y', features=['X1', 'X2'])

    Output:

    >>> omlr.coef_.collect()
           VARIABLE_NAME CLASSLABEL  COEFFICIENT
    0  __PAL_INTERCEPT__          0    -0.225687
    1  __PAL_INTERCEPT__          1     0.031453
    2  __PAL_INTERCEPT__          2    -0.173944
    3                 X1          0     0.100580
    4                 X1          1    -0.208257
    5                 X1          2    -0.097395
    6                 X2          0     0.628975
    7                 X2          1     0.576544
    8                 X2          2    -0.582955

    >>> omlr.online_result_.collect()
       SEQUENCE                          UPDATED_SERIALIZED_RESULT
    0         0  {"SGD":{"data":{"avg_feature_coefficient":[0.1...

    Round 4, invoke partial_fit() for training the model with df_4:

    >>> omlr.partial_fit(self.df_4, label='Y', features=['X1', 'X2'])

    Output:

    >>> omlr.coef_.collect()
          VARIABLE_NAME CLASSLABEL  COEFFICIENT
    0  __PAL_INTERCEPT__          0    -0.204118
    1  __PAL_INTERCEPT__          1     0.071965
    2  __PAL_INTERCEPT__          2    -0.263698
    3                 X1          0     0.239740
    4                 X1          1    -0.326290
    5                 X1          2    -0.139859
    6                 X2          0     0.696389
    7                 X2          1     0.590014
    8                 X2          2    -0.643752


    >>> omlr.online_result_.collect()
       SEQUENCE                          UPDATED_SERIALIZED_RESULT
    0         0  {"SGD":{"data":{"avg_feature_coefficient":[0.2...

    Call predict() with df_predict:

    >>> df_predict.collect()
       ID   X1   X2
    0   1  1.2  0.7
    1   2  1.0 -2.0

    Invoke predict():

    >>> fitted = onlinelr.predict(df_predict, key='ID', features=['X1', 'X2'])
    >>> fitted.collect()
       ID CLASS  PROBABILITY
    0   1     0     0.539350
    1   2     2     0.830026

    """
    learning_rate_type_map = {'inverse_time_decay':0,
                              'exponential_decay':1,
                              'polynomial_decay':2,
                              'piecewise_constant_decay':3,
                              'adagrad':4,
                              'adadelta':5,
                              'rmsprop':6}

    def __init__(self,
                 class_label,
                 init_learning_rate=None,
                 decay=None,
                 drop_rate=None,
                 step_boundaries=None,
                 constant_values=None,
                 enet_alpha=None,
                 enet_lambda=None,
                 shuffle=None,
                 shuffle_seed=None,
                 weight_avg=None,
                 weight_avg_begin=None,
                 learning_rate_type=None,
                 general_learning_rate=None,
                 stair_case=None,
                 cycle=None,
                 epsilon=None,
                 window_size=None):
        setattr(self, 'hanaml_parameters', pal_param_register())
        super(OnlineMultiLogisticRegression, self).__init__()

        self.class_label = self._arg('class_label', class_label, ListOfStrings)
        self.init_learning_rate = self._arg('init_learning_rate', init_learning_rate, float)
        self.decay = self._arg('decay', decay, float)
        self.drop_rate = self._arg('drop_rate', drop_rate, int)
        self.step_boundaries = self._arg('step_boundaries', step_boundaries, list)
        self.constant_values = self._arg('constant_values', constant_values, list)
        self.enet_alpha = self._arg('enet_alpha', enet_alpha, float)
        self.enet_lambda = self._arg('enet_lambda', enet_lambda, float)
        self.shuffle = self._arg('shuffle', shuffle, bool)
        self.shuffle_seed = self._arg('shuffle_seed', shuffle_seed, float)
        self.weight_avg = self._arg('weight_avg', weight_avg, bool)
        self.weight_avg_begin = self._arg('weight_avg_begin', weight_avg_begin, int)
        self.learning_rate_type = self._arg('learning_rate_type', learning_rate_type, self.learning_rate_type_map)
        self.general_learning_rate = self._arg('general_learning_rate', general_learning_rate, float)
        self.stair_case = self._arg('stair_case', stair_case, bool)
        self.cycle = self._arg('cycle', cycle, bool)
        self.epsilon = self._arg('epsilon', epsilon, float)
        self.window_size = self._arg('window_size', window_size, float)

        if learning_rate_type is not None:
            # learning_rate_type is 'Inverse_time_decay', 'Exponential_decay', 'Polynomial_decay', decay,
            # init_learning_rate and drop_rate are mandatory.
            if self.learning_rate_type in (0, 1, 2) and ((decay is None) or (init_learning_rate is None) or (drop_rate is None)):
                msg = "If learning_rate_type is 'Inverse_time_decay', 'Exponential_decay', 'Polynomial_decay, decay, init_learning_rate and drop_rate are mandatory!"
                logger.error(msg)
                raise ValueError(msg)
            # learning_rate_type is 'Piecewise_constant_decay', step_boundaries, constant_values are mandatory.
            if self.learning_rate_type == 3 and ((step_boundaries is None) or (constant_values is None)):
                msg = "If learning_rate_type is 'Piecewise_constant_decay', step_boundaries and constant_values are mandatory!"
                logger.error(msg)
                raise ValueError(msg)

        # check step_boundaries
        if step_boundaries is not None:
            if not all(isinstance(t, (int, float)) for t in step_boundaries):
                msg = "Valid values of `step_boundaries` must be a list of numerical values!"
                logger.error(msg)
                raise TypeError(msg)
            self.step_boundaries = (', ').join(str(s) for s in step_boundaries)
        # check constant_values
        if constant_values is not None:
            if not all(isinstance(t, (int, float)) for t in constant_values):
                msg = "Valid values of `constant_values` must be a list of numerical values!"
                logger.error(msg)
                raise TypeError(msg)
            self.constant_values = (', ').join(str(c) for c in constant_values)

        self.model_ = None
        self.online_result_ = None
        self.coef_ = None

    @trace_sql
    def partial_fit(self,
                    data,
                    key=None,
                    features=None,
                    label=None,
                    thread_ratio=None,
                    progress_indicator_id=None,):
        r"""
        Online training based on each round of data.

        Parameters
        ----------

        data : DataFrame

            Training data.

        key : str, optional

            Name of the ID column.

            If ``key`` is not provided, then:

            - if ``data`` is indexed by a single column, then ``key`` defaults
              to that index column;
            - otherwise, it is assumed that ``data`` contains no ID column.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.

            If ``label`` is not provided, it defaults to the last column.

        thread_ratio : float, optional

            Controls the proportion of available threads to use.
            The value range is from 0 to 1, where 0 means only using 1 thread, and 1 means using at most all the currently available threads.
            Values outside this range tell PAL to heuristically determine the number of threads to use.

            Defaults to 0.0.

        progress_indicator_id : str, optional

            The ID of progress indicator for model evaluation/parameter selection.

            Progress indicator deactivated if no value provided.


        Returns
        -------

        A fitted object of OnlineMultiLogisticRegression.


        """
        setattr(self, 'hanaml_fit_params', pal_param_register())
        if data is None:
            msg = 'The data for fit cannot be None!'
            logger.error(msg)
            raise ValueError(msg)

        conn = data.connection_context
        require_pal_usable(conn)

        # init process, need to generate inter tbl in the first time
        execute_statement = None
        if self.model_ is None:
            unique_id = str(uuid.uuid1()).replace('-', '_').upper()
            result_tbl = '#PAL_Online_MLR_RESULT_TBL_{}_{}'.format(self.id, unique_id)
            param_rows = [('INITIAL_LEARN_RATE', None, self.init_learning_rate, None),
                          ('DECAY', None, self.decay, None),
                          ('DROP_RATE', self.drop_rate, None, None),
                          ('STEP_BOUNDARIES', None, None, self.step_boundaries),
                          ('CONSTANT_VALUES', None, None, self.constant_values),
                          ('ENET_LAMBDA', None, self.enet_lambda, None),
                          ('ENET_ALPHA', None, self.enet_alpha, None),
                          ('NEED_SHUFFLE', self.shuffle, None, None),
                          ('SHUFFLE_SEED', self.shuffle_seed, None, None),
                          ('NEED_WEIGHT_AVERAGE', self.weight_avg, None, None),
                          ('WEIGHT_AVERAGE_BEGIN', self.weight_avg_begin, None, None),
                          ('LEARN_RATE_TYPE', self.learning_rate_type, None, None),
                          ('GENERAL_LEARN_RATE', None, self.general_learning_rate, None),
                          ('STAIR_CASE', self.stair_case, None, None),
                          ('CYCLE', self.cycle, None, None),
                          ('EPSILON', None, self.epsilon, None),
                          ('WINDOW_SIZE', None, self.window_size, None)]

            if self.class_label is not None:
                param_rows.extend(('CLASS_LABEL', None, None, cl) for cl in self.class_label)

            try:
                self._call_pal_auto(conn,
                                    'PAL_INIT_ONLINE_MULTICLASS_LOGISTIC_REGRESSION',
                                    ParameterTable().with_data(param_rows),
                                    result_tbl)
            except dbapi.Error as db_err:
                logger.exception(str(db_err))
                try_drop(conn, result_tbl)
                raise
            except pyodbc.Error as db_err:
                logger.exception(str(db_err.args[1]))
                try_drop(conn, result_tbl)
                raise
            self.online_result_ = conn.table(result_tbl)
            execute_statement = self.execute_statement
        key = self._arg('key', key, str)
        index = data.index
        if isinstance(index, str):
            if key is not None and index != key:
                msg = "Discrepancy between the designated key column '{}' ".format(key) +\
                "and the designated index column '{}'.".format(index)
                logger.warning(msg)
        key = index if key is None else key
        features = self._arg('features', features, ListOfStrings)
        label = self._arg('label', label, str)
        self.thread_ratio = self._arg('thread_ratio', thread_ratio, float)
        self.progress_indicator_id = self._arg('progress_indicator_id', progress_indicator_id, str)

        cols = data.columns
        if key is not None:
            id_col = [key]
            cols.remove(key)
        else:
            id_col = []
        if label is None:
            label = cols[-1]
        cols.remove(label)
        if features is None:
            features = cols
        data_ = data[id_col + [label] + features]

        # create inter tbl based on self.model_[1] or self.online_result_ (for the first time)
        if self.model_ is not None:
            input_tbl = self.model_[1]
        else:
            input_tbl = self.online_result_

        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        outputs = ['COEF', 'ONLINE_UPDATE']
        outputs = ['#PAL_ONLINE_LINEAR_REGRESSION_{}_TBL_{}_{}'.format(name, self.id, unique_id)
                   for name in outputs]
        coef_tbl, online_update_tbl = outputs
        param_rows = [('HAS_ID', key is not None, None, None),
                      ('THREAD_RATIO', None, self.thread_ratio, None),
                      ('PROGRESS_INDICATOR_ID', None, None, progress_indicator_id)]

        try:
            self._call_pal_auto(conn,
                                'PAL_TRAIN_ONLINE_MULTICLASS_LOGISTIC_REGRESSION',
                                data_,
                                input_tbl,
                                ParameterTable().with_data(param_rows),
                                *outputs)
        except dbapi.Error as db_err:
            logger.exception(str(db_err))
            try_drop(conn, outputs)
            raise
        except pyodbc.Error as db_err:
            logger.exception(str(db_err.args[1]))
            try_drop(conn, outputs)
            raise
        self.online_result_ = conn.table(online_update_tbl)
        self.coef_ = conn.table(coef_tbl)
        self.model_ = [self.coef_, self.online_result_]
        if execute_statement is not None:
            self.execute_statement = [execute_statement, self.execute_statement]
        return self

    @trace_sql
    def predict(self, data, key=None, features=None):
        r"""
        Predict dependent variable values based on a fitted model.

        Parameters
        ----------

        data : DataFrame

            Independent variable values to predict for.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults to all non-ID columns.

        Returns
        -------

        DataFrame

            Predicted values, structured as follows:

                - ID column: with same name and type as ``data`` 's ID column.
                - VALUE: type DOUBLE, representing predicted values.

        """

        if self.model_ is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")
        mlr = LogisticRegression(multi_class=True)
        mlr.pmml_ = None
        mlr.model_ = self.model_[0]
        fitted_tbl = mlr.predict(data, key, features)
        return fitted_tbl

    def score(self, data, key=None, features=None, label=None):
        r"""
        Returns the coefficient of determination R2 of the prediction.

        Parameters
        ----------

        data : DataFrame

            Data on which to assess model performance.

        key : str, optional

            Name of the ID column.

            Mandatory if ``data`` is not indexed, or the index of ``data`` contains multiple columns.

            Defaults to the single index column of ``data`` if not provided.

        features : list of str, optional

            Names of the feature columns.

            If ``features`` is not provided, it defaults all non-ID,
            non-label columns.

        label : str, optional

            Name of the dependent variable.

            If ``label`` is not provided, it defaults to the last column.

        Returns
        -------

        float

            Returns the coefficient of determination R2 of the prediction.
        """
        if self.model_ is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")
        mlr = LogisticRegression(multi_class=True)
        mlr.pmml_ = None
        mlr.model_ = self.model_[0]
        score = mlr.score(data, key, features, label)
        return score
