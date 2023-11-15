"""module mlutils_feature_transform. Simple
utilities to transform arrays of data

"""
from typing import List, Union
from sklearn.preprocessing import (PowerTransformer,
                                   StandardScaler,
                                   RobustScaler,
                                   MinMaxScaler,
                                   KBinsDiscretizer)



SCALING_STRATEGIES = ['min-max', 'z-score', 'robust']
BINNING_STRATEGIES = ['uniform', 'quantile', 'kmeans']

def box_cox_data_transform(data: Union[List[int], List[float]], **options) -> Union[List[int], List[float]]:
    """Transform the data using the Box-Cox transform.
    The Box-Cox transform only works on strictly positive data.
    The implementation uses the sklearn.preprocessing.PowerTransformer.
    Check https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html
    for the available options

    Parameters
    ----------
    data

    Returns
    -------

    """
    transformer = PowerTransformer(method='box-cox', **options)
    return transformer.fit_transform(data)


def data_scaling(data: Union[List[int], List[float]], strategy: str,
                 **options) -> Union[List[int], List[float]]:
    """

    Parameters
    ----------
    data: The data to be scaled
    strategy: The strategy to use in order to scale the data
    options

    Returns
    -------

    """

    if strategy not in SCALING_STRATEGIES:
        raise ValueError(f"strategy {strategy} not in {SCALING_STRATEGIES}")

    if strategy == "min-max":

        if 'feature_range' not in options:
            raise ValueError("feature_range must be given when strategy='min-max'")

        scaler = MinMaxScaler(feature_range=options["feature_range"])
    elif strategy == "z-score":
        scaler = StandardScaler(**options)
    elif strategy == "robust":
        scaler = RobustScaler(**options)
    else:
        raise ValueError(f"strategy {strategy} not in {SCALING_STRATEGIES}")

    return scaler.fit_transform(data)


def data_binning(data: Union[List[int], List[float]],
                 strategy: str, n_bins: int, **options) -> Union[List[int], List[float]]:


    if strategy not in BINNING_STRATEGIES:
        raise ValueError(f"strategy {strategy} not in {BINNING_STRATEGIES}")

    binner = KBinsDiscretizer(n_bins=n_bins, strategy=strategy, **options )
    return binner.fit_transform(data)
