from __future__ import annotations
from typing import Any, Union
import client.renderer as cliRen

class instance:
    parent: Union[instance, cliRen.renderer]
    children: list[instance] = []

    def __setitem__(self, key: str, value: Any):
        self.__setattr__(key, value);

    def __getitem__(self, key: str):
        return self.__getattribute__(key);

    def __setattr__(self, prop: str, value: Any) -> None:
        if (prop == 'parent'):
            cliRen.gameLoop.getRenderer().setParent(self, value)
        else:
            super().__setattr__(prop, value)

    def __getattribute__(self, prop: str):
        return super().__getattribute__(prop);

    def update(self, dt: float):
        pass