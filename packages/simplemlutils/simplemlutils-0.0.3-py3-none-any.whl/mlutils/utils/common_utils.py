import numpy as np
import torch
import random

def set_seed(seed: int) -> None:
    """Set the seed for various
    underlying components

    Parameters
    ----------
    seed: The seed to use

    Returns
    -------
    None
    """

    # Disable cudnn to maximize reproducibility
    torch.cuda.cudnn_enabled = False
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True