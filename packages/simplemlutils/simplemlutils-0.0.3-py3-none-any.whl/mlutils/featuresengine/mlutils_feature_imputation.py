from typing import List, Union
from sklearn.impute import SimpleImputer


IMPUTATION_STRATEGIES = ['mean', 'constant', 'mode', 'end-of-tail']

def impute_data(data: Union[List[int], List[float]],
                strategy: str, **options) -> Union[List[int], List[float]]:
    """Impute the given data. Three strategies are supported
    - mean that uses sklearn.SimpleImputer
    - constant that uses sklearn.SimpleImputer
    - end-of-tail that uses feature_engine.EndOfTailImputer

    Parameters
    ----------
    data
    strategy

    Returns
    -------

    an instance of List[int] or List[float] depending on the input
    """

    if strategy not in IMPUTATION_STRATEGIES:
        raise ValueError(f"strategy={strategy} not in {IMPUTATION_STRATEGIES}")

    if strategy == 'end-of-tail':
        return tail_imputation(data, **options)

    strategy_ = strategy

    if strategy == 'mode':
        strategy_ = "most_frequent"

    return SimpleImputer(strategy=strategy_, **options).fit_transform(data)

def tail_imputation(data: Union[List[int], List[float]], **options) -> Union[List[int], List[float]]:
    """Performs tail-imputation of the given data using
    feature_engine.EndTailImputer. **options can provide the
    optional argument imputation_method in order to be passed to
    the constructor of the  EndTailImputer.
    Valid imputation_method values are
    - gaussian
    - iqr
    - max

    The default value is gaussian.
    Check: https://feature-engine.trainindata.com/en/latest/api_doc/imputation/EndTailImputer.html
    for more information on the arguments you can use

    Parameters
    ----------
    data: The data to impute
    options

    Returns
    -------

    """
    from feature_engine.imputation import EndTailImputer

    _VALID_IMPUTATION_METHOD = ['gaussian']

    if 'imputation_method' in options and options['imputation_method'] not in _VALID_IMPUTATION_METHOD:
        raise ValueError(f"imputation_method={options['imputation_method']} not in {_VALID_IMPUTATION_METHOD}")

    return EndTailImputer(**options).fit_transform(data)
