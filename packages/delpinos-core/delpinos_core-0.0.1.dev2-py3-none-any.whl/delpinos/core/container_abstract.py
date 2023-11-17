# -*- coding: utf-8 -*-
# pylint: disable=C0103

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class ContainerAbstract(ABC):
    @abstractmethod
    def build(self, **__) -> "ContainerAbstract":
        raise NotImplementedError()

    @abstractmethod
    def setup(self):
        raise NotImplementedError()

    @abstractmethod
    def validate(self):
        raise NotImplementedError()

    @abstractmethod
    def config(self) -> Dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    def kwargs(self) -> Dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    def required_value_isinstance(self, value: Any, tp: type | None = None, name: str = "value"):
        raise NotImplementedError()

    @abstractmethod
    def set(self, key: str, value: Any = None, tp: type | None = None) -> "ContainerAbstract":
        raise NotImplementedError()

    @abstractmethod
    def get(self, key: str, tp: type | None = None, default: Any = None) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def get_from_keys(self, *keys):
        raise NotImplementedError()
