"""module resnet_model_loader. Factory class to load PyTorch
ResNet model

"""

import torch
from typing import Any, Callable, Union
import torch.nn as nn
from torchvision import models
from pathlib import Path

from mlutils.models.models_enum import ModelEnum


class ResNetModelLoader(object):

    @staticmethod
    def build_from_config(config: dict):
        return ResNetModelLoader.build(model_type=config['model_type'],
                                       device=config['device'],
                                       pretrained=config['with_pretrained'],
                                       model_adaptor=config['model_adaptor'],
                                       freeze_model_params=config['freeze_model_parameters'],
                                       weights=config['weights'] if 'weights' in config else None)

    @staticmethod
    def load_from_config(config: dict):
        return ResNetModelLoader.load(model_type=config['model_type'],
                                      model_path=config['model_path'],
                                      model_adaptor=config['model_adaptor'],
                                      device=config['device'],
                                      freeze_model_params=config['freeze_model_parameters'],
                                      pretrained=config['with_pretrained'],
                                      weights=config['weights'] if 'weights' in config else None)

    @staticmethod
    def build(model_type: Union[ModelEnum | str], device: str = 'cpu',
              pretrained: bool = True, weights: Any = None,
              model_adaptor: Callable = None,
              freeze_model_params: bool = True) -> nn.Module:

        if isinstance(model_type, str):
            model_type = ModelEnum.from_str(model=model_type)

        if model_type == ModelEnum.RESNET_18:

            if pretrained and weights is None:
                model_ft = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
            elif pretrained and weights is not None:
                model_ft = models.resnet18(weights=weights)
            else:
                model_ft = models.resnet18(weights=None)
        elif model_type == ModelEnum.RESNET_50:
            if pretrained and weights is None:
                model_ft = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
            elif pretrained and weights is not None:
                model_ft = models.resnet50(weights=weights)
            else:
                model_ft = models.resnet50(weights=None)
        elif model_type == ModelEnum.RESNET_101:
            if pretrained and weights is None:
                model_ft = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
            elif pretrained and weights is not None:
                model_ft = models.resnet101(weights=weights)
            else:
                model_ft = models.resnet101(weights=None)
        else:
            raise ValueError(f"Model type {model_type} not in [RESNET_18, RESNET_50, RESNET_101]")

        if freeze_model_params:
            for param in model_ft.parameters():
                param.requires_grad = False

        if model_adaptor is not None:
            model_ft = model_adaptor(model_ft)

        model_ft.to(device=device)
        return model_ft

    @staticmethod
    def load(model_type: ModelEnum,
             model_path: Path,
             model_adaptor: Callable = None,
             device: str = 'cpu',
             freeze_model_params: bool = True,
             pretrained: bool = True, weights: Any = None) -> nn.Module:

        model_ft = ResNetModelLoader.build(model_type=model_type,
                                           model_adaptor=model_adaptor,
                                           device=device,
                                           freeze_model_params=freeze_model_params,
                                           pretrained=pretrained,
                                           weights=weights)

        model_ft.load_state_dict(torch.load(model_path, map_location=torch.device(device)))
        return model_ft
