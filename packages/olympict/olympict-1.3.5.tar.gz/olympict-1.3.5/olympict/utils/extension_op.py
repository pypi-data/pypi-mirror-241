import os

from olympict.files.o_image import OlympImage
from olympict.types import ImgFormat


class ExtensionOperation:
    def __init__(self, format: ImgFormat) -> None:
        self.format = format

    def change_format(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        base, _ = os.path.splitext(o.path)

        fmt = f".{self.format}" if "." != self.format[0] else self.format

        o.path = base + fmt

        return o
