from typing import List, Dict
from dataclasses import dataclass, field


@dataclass(init=True, repr=True)
class ClassifierPerformance(object):
    accuracy: float = 0.0
    predictions: List[int] = field(default_factory=list)
    ground_truth: List[int] = field(default_factory=list)
    confusion_matrix: Dict = field(default_factory=dict)
