from typing import List
import torch
import numpy as np


def sliding_average(value_list: List[float],
                    window: int) -> float:

    """Computes the average of the latest instances in a list

    Parameters
    ----------
    value_list: input list of floats (can't be empty)
    window: number of instances to take into account. If value is 0 or greater than
            the length of value_list, all instances will be taken into account

    Returns
    -------
    The mean of the last window instances in value_list
    """

    if len(value_list) == 0:
        raise ValueError("Cannot perform sliding average on an empty list.")
    return np.asarray(value_list[-window:]).mean()


def weighted_sum(x: torch.Tensor, y: torch.Tensor, w: float) -> torch.Tensor:
    """Returns a weighted sum of the two tensors i.e.
    out = w*x + (1 - w)*y

    Parameters
    ----------
    x: Tensor
    y: Tensor
    w: Weight to use

    Returns
    -------
    w*x + (1.0-w)*y
    """
    return w*x + (1.0-w)*y
