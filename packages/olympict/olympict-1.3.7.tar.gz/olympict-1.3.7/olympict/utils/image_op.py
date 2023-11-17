from typing import Callable

from olympict.files.o_image import OlympImage
from olympict.types import Img


class ImageOperation:
    def __init__(self, func: Callable[[Img], Img]) -> None:
        self.func = func

    def task(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        o.img = self.func(o.img)
        return o
