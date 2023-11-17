from typing import Any, Callable

from olympict.files.o_image import OlympImage


class PathOperation:
    def __init__(self, func: Callable[[str], str]) -> None:
        self.func = func

    def task(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        o.path = self.func(o.path)
        return o


def filter_none_packets(p: Any) -> bool:
    return p is not None
