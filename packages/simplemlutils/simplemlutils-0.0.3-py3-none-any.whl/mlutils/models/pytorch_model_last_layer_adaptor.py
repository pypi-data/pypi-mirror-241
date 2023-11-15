import torch.nn as nn
class AddLinearLayerAdaptor(object):
    """Add a linear layer to the given model. The layer can either
    be the LAST_LAYER in the network in which case this class adds a linear
    with dimensions (num_ftrs, num_ftrs) or by indicating the size of the output of the layer

    """

    def __init__(self, params: dict):
        self.params = params

    def add_linear_layer(self, model_ft: nn.Module) -> nn.Module:

        if 'out' not in self.params:
            raise ValueError("The self.params is missing the 'out' keyword. "
                             "This should specify either 'LAST_LAYER' or the size of the"
                             "output of the layer")

        num_ftrs = model_ft.fc.in_features
        if self.params['out'] == 'LAST_LAYER':
            model_ft.fc = nn.Linear(num_ftrs, num_ftrs)
        else:
            model_ft.fc = nn.Linear(num_ftrs, self.params['out'])
        return model_ft

    def __call__(self, model_ft: nn.Module) -> nn.Module:
        return self.add_linear_layer(model_ft=model_ft)