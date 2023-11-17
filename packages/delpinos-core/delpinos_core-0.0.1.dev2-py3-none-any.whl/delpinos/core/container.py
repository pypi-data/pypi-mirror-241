# -*- coding: utf-8 -*-
# pylint: disable=C0103

from typing import Any, Dict, List

from delpinos.core.container_abstract import ContainerAbstract


class Container(ContainerAbstract):
    __: Dict[str, Any]

    def __init__(self, **kwargs):
        self.__ = kwargs
        self.setup()
        self.validate()

    def build(self, **__) -> "Container":
        return self

    def setup(self):
        return

    def validate(self):
        return

    def config(self) -> Dict[str, Any]:
        return {
            k: v
            for k, v in self.__.items()
            if not (k[0:3] == "___" and k[-3:] == "___")
        }

    def kwargs(self) -> Dict[str, Any]:
        return self.__

    def required_value_isinstance(self, value: Any, tp: type | None = None, name: str = "value"):
        if tp and not isinstance(value, tp):
            raise TypeError(
                f"{name} is required valid instance of {tp.__module__}.{tp.__name__}"
            )

    def set(self, key: str, value: Any = None, tp: type | None = None) -> "Container":
        self.required_value_isinstance(value, tp, str(key))
        self.__[key] = value
        return self

    def get(self, key: str, tp: type | None = None, default: Any = None) -> Any:
        if key in self.__:
            return self.__.get(key)
        value = self.__get_from_keys(keys=key.split("."), default=default)
        self.set(key, value, tp)
        return value

    def __get_from_keys(self, keys: List[str], default: Any = None) -> Any:
        def check_get(value) -> Any:
            return hasattr(value, "get") and callable(getattr(value, "get"))
        if not keys:
            return default
        value = self.kwargs()
        for key in keys:
            if check_get(value):
                try:
                    if not check_get(value):
                        return default
                    value = getattr(value, "get")(key)
                except Exception:
                    return default
        return value

    def get_from_keys(self, *keys):
        value = None
        for key in keys:
            if key in self.__:
                value = value or self.__.get(key)
            if value is None:
                continue
            if isinstance(value, str) and len(value) == 0:
                continue
            break
        return value
