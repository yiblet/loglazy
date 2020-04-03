from typing import Callable, Generic, TypeVar

R = TypeVar('R')


class Interp(Generic[R]):
    _interpolate: Callable[[], R]

    def __init__(self, interpolate: Callable[[], R]):
        self._interpolate = interpolate
        self._result = None
        self._has_result = False

    def get_result(self) -> R:
        if self._has_result:
            return self._result
        self._result = self._interpolate()
        return self._result

    def __repr__(self) -> str:
        return repr(self.get_result())

    def __str__(self) -> str:
        return str(self.get_result())
