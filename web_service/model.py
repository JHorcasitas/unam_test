from typing import Literal
from abc import ABC, abstractmethod


class ClassifierModel(ABC):
    @abstractmethod
    def predict(self) -> Literal["cat", "dog"]:
        ...


class CnnClassifier(ClassifierModel):
    def __init__(self, image: str) -> None:
        self._image = image

    def predict(self) -> Literal["cat", "dog"]:
        return "cat"
