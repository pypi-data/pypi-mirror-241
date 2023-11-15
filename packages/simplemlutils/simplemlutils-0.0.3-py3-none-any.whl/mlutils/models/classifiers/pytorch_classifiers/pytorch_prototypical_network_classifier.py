"""module pytorch_prototypical_network_classifier. Models a prototypical
network classifier using PyTorch.
The implementation is taken from https://github.com/sicara/easy-few-shot-learning
"""

import torch
from torch import Tensor
import torch.nn as nn
from typing import Union, Any, Callable, Dict
from pathlib import Path

from mlutils.models.classifiers.pytorch_classifiers.pytorch_few_shot_classifier import PyTorchFewShotClassifier
from mlutils.models.models_enum import ModelEnum
from mlutils.models.classifiers.pytorch_classifiers.resnet_model_loader import ResNetModelLoader


class PyTorchPrototypicalNetworkClassifier(PyTorchFewShotClassifier):
    """
    Jake Snell, Kevin Swersky, and Richard S. Zemel.
    "Prototypical networks for few-shot learning." (2017)
    https://arxiv.org/abs/1703.05175

    Prototypical networks extract feature vectors for both support and query images. Then it
    computes the mean of support features for each class (called prototypes), and predict
    classification scores for query images based on their Euclidean distance to the prototypes.
    """

    @classmethod
    def build(cls,*, backbone_type: Union[ModelEnum, str],
              use_softmax: bool,
              device: Union[str, torch.device],
              pretrained: bool,
              freeze_model_params: bool,
              weights: Any = None,
              model_adaptor: Callable = None) -> "PyTorchPrototypicalNetworkClassifier":
        """Builds an instance of PyTorchPrototypicalNetworkClassifier class

        Parameters
        ----------
        backbone_type: The type of the backbone network to use
        use_softmax: Whether softmax should be used at the output
        device: To what device the model should be transferred
        pretrained: Whether the backbone should be pretrained
        freeze_model_params: Whether the backbone model parameters should be frozen
        weights: Any weights to use for initializing the backbone model
        model_adaptor: How to adapt the backbone model

        Returns
        -------

        An instance of PyTorchPrototypicalNetworkClassifier
        """

        backbone_net = ResNetModelLoader.build(model_type=backbone_type,
                                               device=device,
                                               pretrained=pretrained,
                                               freeze_model_params=freeze_model_params,
                                               weights=weights,
                                               model_adaptor=model_adaptor).to(device)

        return PyTorchPrototypicalNetworkClassifier(backbone=backbone_net,
                                                    use_softmax=use_softmax,
                                                    device=device).to(device)

    @classmethod
    def load(cls, *, model_path: Path,
             backbone_type: Union[ModelEnum, str],
              use_softmax: bool,
              device: Union[str, torch.device],
              pretrained: bool,
              freeze_model_params: bool,
              weights: Any = None,
              model_adaptor: Callable = None) -> "PyTorchPrototypicalNetworkClassifier":
        """Builds an instance of PyTorchPrototypicalNetworkClassifier class
        from the specified Path

        Parameters
        ----------
        model_path: The path to load the state of the model
        backbone_type: The type of the backbone network to use
        use_softmax: Whether softmax should be used at the output
        device: To what device the model should be transferred
        pretrained: Whether the backbone should be pretrained
        freeze_model_params: Whether the backbone model parameters should be frozen
        weights: Any weights to use for initializing the backbone model
        model_adaptor: How to adapt the backbone model
        model_adaptor

        Returns
        -------

        An instance of PyTorchPrototypicalNetworkClassifier
        """

        model = PyTorchPrototypicalNetworkClassifier.build(backbone_type=backbone_type,
                                                           use_softmax=use_softmax,
                                                           device=device,
                                                           pretrained=pretrained,
                                                           freeze_model_params=freeze_model_params,
                                                           weights=weights,
                                                           model_adaptor=model_adaptor).to(device)

        model.load_state_dict(torch.load(model_path,
                                         map_location=torch.device(device)))
        model.to(device)
        return model

    @classmethod
    def load_with_state_dict(clf, *, model_state: Dict,
                             backbone_type: Union[ModelEnum, str],
                             use_softmax: bool,
                             device: Union[str, torch.device],
                             pretrained: bool,
                             freeze_model_params: bool,
                             weights: Any = None,
                             model_adaptor: Callable = None) -> "PyTorchPrototypicalNetworkClassifier":
        """

        Parameters
        ----------
        model_state
        backbone_type
        use_softmax
        device
        pretrained
        freeze_model_params
        weights
        model_adaptor

        Returns
        -------

        """
        model = PyTorchPrototypicalNetworkClassifier.build(backbone_type=backbone_type,
                                                           use_softmax=use_softmax,
                                                           device=device,
                                                           pretrained=pretrained,
                                                           freeze_model_params=freeze_model_params,
                                                           weights=weights,
                                                           model_adaptor=model_adaptor).to(device)

        model.load_state_dict(model_state)
        model.to(device)
        return model


    def __init__(self, backbone: nn.Module, use_softmax: bool = False, device: str="cpu"):
        """
        Raises:
            ValueError: if the backbone is not a feature extractor,
            i.e. if the output for a given image is not a 1-dim tensor.
        """
        super(PyTorchPrototypicalNetworkClassifier, self).__init__(backbone=backbone,
                                                                   use_softmax=use_softmax,
                                                                   device=device)

        if len(self.backbone_output_shape) != 1:
            raise ValueError(
                "Illegal backbone for Prototypical Networks. "
                "Expected output for an image is a 1-dim tensor."
            )

        # prototypical networks need to Flatten their output
        self.flatten_layer = nn.Flatten()

    def process_support_set(
        self,
        support_images: Tensor,
        support_labels: Tensor,
    ):
        """
        Overrides process_support_set of FewShotClassifier.
        Extract feature vectors from the support set and store class prototypes.

        Args:
            support_images: images of the support set
            support_labels: labels of support set images
        """

        support_features = self.backbone.forward(support_images)
        support_features = self.flatten_layer(support_features)
        support_features = support_features.cpu()
        self.prototypes = PyTorchFewShotClassifier.compute_prototypes(support_features, support_labels)
        self.prototypes = self.prototypes.to(self.device)

    def forward(self, query_images: Tensor,) -> Tensor:
        """Overrides forward method of FewShotClassifier.
        Predict query labels based on their distance to class prototypes in the feature space.
        Classification scores are the negative of euclidean distances.

        Parameters
        ----------
        query_images: images of the query set

        Returns
        -------

         A prediction of classification scores for query images
        """

        # Extract the features of support and query images
        z_query = self.backbone.forward(query_images)

        # flatten the result
        z_query = self.flatten_layer(z_query)

        # Compute the euclidean distance from queries to prototypes
        dists = torch.cdist(z_query, self.prototypes)

        # Use it to compute classification scores
        scores = -dists

        return self.softmax_if_specified(scores)

    @staticmethod
    def is_transductive() -> bool:
        return False
