from abc import abstractmethod
from typing import Tuple
import copy
import torch
from torch import nn, Tensor



class PyTorchFewShotClassifier(nn.Module):
    """
    Abstract class providing methods usable by all few-shot classification algorithms
    """

    @staticmethod
    def compute_prototypes(support_features: Tensor,
                           support_labels: Tensor) -> Tensor:
        """ Compute class prototypes from support features and labels

        Parameters
        ----------
        support_features: for each instance in the support set, its feature vector
        support_labels: for each instance in the support set, its label

        Returns
        -------

        For each label of the support set, the average feature vector of instances with this label
        """

        n_way = len(torch.unique(support_labels))
        # Prototype i is the mean of all
        # instances of features corresponding to labels == i
        return torch.cat(
            [
                support_features[torch.nonzero(support_labels == label)].mean(0)
                for label in range(n_way)
            ]
        )

    @staticmethod
    def compute_backbone_output_shape(backbone: nn.Module) -> Tuple[int]:
        """
        Compute the dimension of the feature space defined by a feature extractor.
        Args:
            backbone: feature extractor

        Returns:
            shape of the feature vector computed by the feature extractor for an instance

        """
        input_images = torch.ones((4, 3, 32, 32))
        # Use a copy of the backbone on CPU, to avoid device conflict
        output = copy.deepcopy(backbone).cpu()(input_images)
        return tuple(output.shape[1:])

    def __init__(self, backbone: nn.Module, use_softmax: bool = False,
                 device: str = "cpu"):
        """
        Initialize the Few-Shot Classifier
        Args:
            backbone: the feature extractor used by the method. Must output a tensor of the
                appropriate shape (depending on the method)
            use_softmax: whether to return predictions as soft probabilities
        """
        super().__init__()

        self.backbone: nn.Module = backbone
        self.backbone_output_shape = PyTorchFewShotClassifier.compute_backbone_output_shape(backbone)
        self.feature_dimension = self.backbone_output_shape[0]

        self.use_softmax = use_softmax

        self.prototypes = None
        self.support_features = None
        self.support_labels = None
        self.device: str = device

    @abstractmethod
    def forward(
        self,
        query_images: Tensor,
    ) -> Tensor:
        """
        Predict classification labels.

        Args:
            query_images: images of the query set
        Returns:
            a prediction of classification scores for query images
        """
        raise NotImplementedError(
            "All few-shot algorithms must implement a forward method."
        )

    @abstractmethod
    def process_support_set(
        self,
        support_images: Tensor,
        support_labels: Tensor,
    ):
        """
        Harness information from the support set, so that query labels can later be predicted using
        a forward call

        Args:
            support_images: images of the support set
            support_labels: labels of support set images
        """
        raise NotImplementedError(
            "All few-shot algorithms must implement a process_support_set method."
        )

    @staticmethod
    def is_transductive() -> bool:
        raise NotImplementedError(
            "All few-shot algorithms must implement a is_transductive method."
        )

    def softmax_if_specified(self, output: Tensor) -> Tensor:
        """
        If the option is chosen when the classifier is initialized, we perform a softmax on the
        output in order to return soft probabilities.
        Args:
            output: output of the forward method

        Returns:
            output as it was, or output as soft probabilities
        """
        return output.softmax(-1) if self.use_softmax else output

    def l2_distance_to_prototypes(self, samples: Tensor) -> Tensor:
        """
        Compute prediction logits from their euclidean distance to support set prototypes.
        Args:
            samples: features of the items to classify

        Returns:
            prediction logits
        """
        return -torch.cdist(samples, self.prototypes)

    def cosine_distance_to_prototypes(self, samples) -> Tensor:
        """
        Compute prediction logits from their cosine distance to support set prototypes.
        Args:
            samples: features of the items to classify

        Returns:
            prediction logits
        """
        return (
            nn.functional.normalize(samples, dim=1)
            @ nn.functional.normalize(self.prototypes, dim=1).T
        )

    def store_support_set_data(
        self,
        support_images: Tensor,
        support_labels: Tensor,
    ):
        """
        Extract support features, compute prototypes,
            and store support labels, features, and prototypes
        Args:
            support_images: images of the support set
            support_labels: labels of support set images
        """
        self.support_labels = support_labels
        self.support_features = self.backbone(support_images)
        self.prototypes = PyTorchFewShotClassifier.compute_prototypes(self.support_features, support_labels)
