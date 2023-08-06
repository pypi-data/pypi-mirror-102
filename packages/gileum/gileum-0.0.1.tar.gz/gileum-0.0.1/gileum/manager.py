from __future__ import annotations
from copy import deepcopy
from threading import RLock
from typing import (
    Dict,
    Type,
    TypeVar,
)

from .gileum import BaseGileum


Gileum_t = TypeVar("Gileum_t", bound=BaseGileum)


class GileumManager:

    def __init__(self) -> None:
        self.__glms: Dict[str, BaseGileum] = {}

    def _set_glm(self, glm: BaseGileum) -> None:
        if not isinstance(glm, BaseGileum):
            raise TypeError

        if not hasattr(glm, "glm_name"):
            raise AttributeError

        if glm.glm_name in self.__glms:
            return

        self.__glms[glm.glm_name] = glm

    def get_glm(self, name: str, typ: Type[Gileum_t]) -> Gileum_t:
        if name not in self.__glms:
            raise KeyError

        glm = self.__glms.get(name)
        if not isinstance(glm, typ):
            raise TypeError

        return glm

    @property
    def glms(self) -> Dict[str, BaseGileum]:
        return deepcopy(self.__glms)


class SyncGileumManager(GileumManager):

    def __init__(self) -> None:
        super().__init__()

        self.__lock = RLock()

    def _set_glm(self, glm: BaseGileum) -> None:
        with self.__lock:
            super()._set_glm(glm)

    def get_glm(self, name: str, typ: Type[Gileum_t]) -> Gileum_t:
        with self.__lock:
            res = super().get_glm(name, typ)
        return res

    @property
    def glms(self) -> Dict[str, BaseGileum]:
        with self.__lock:
            res = super().glms
        return res


class GileumManagerAlreadySetError(Exception):
    pass


__glm_man__ = None
GileumManager_t = TypeVar("GileumManager_t", bound=GileumManager)


def init_glm_manager(manager: GileumManager_t) -> GileumManager_t:
    global __glm_man__

    # NOTE
    #   __glm_man__ must be a single object within runtime. There are some
    #   reasons for it:
    #
    #   1.  GileumManager object will be in the global scope regardless of
    #       implementation because, in most cases, setting information should
    #       be shared with all objects at runtime. It means the GileumManager
    #       object has its state within the global scope.
    #   2.  If __glm_man__ were resetable, then some objects referencing
    #       __glm_man__ would face the situation that sometimes __glm_man__
    #       had certain gileum, and sometimes __glm_man__ didn't have the one.

    if __glm_man__ is not None:
        raise GileumManagerAlreadySetError

    if not isinstance(manager, GileumManager):
        raise TypeError

    __glm_man__ = manager
    return __glm_man__


def get_glm_manager() -> GileumManager:
    global __glm_man__

    if __glm_man__ is None:
        __glm_man__ = GileumManager()
    return __glm_man__


# NOTE
#   This function is for testing. See the NOTE in `init_glm_manager` to
#   know the reasons for it.
def _reset_glm_manager() -> None:
    global __glm_man__
    __glm_man__ = None
