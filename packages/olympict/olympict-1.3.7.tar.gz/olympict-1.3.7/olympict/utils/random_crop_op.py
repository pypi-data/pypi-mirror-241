from random import randint

from olympict.files.o_image import OlympImage
from olympict.types import Size


class RandomCropOperation:
    def __init__(
        self,
        output_size: Size,
    ) -> None:
        self.output_size = output_size

    def task(self, o: OlympImage) -> OlympImage:
        h, w, _ = o.img.shape
        t_w, t_h = self.output_size

        off_x: int = randint(0, w - t_w - 1)
        off_y: int = randint(0, h - t_h - 1)

        o.img = o.img[off_y : off_y + t_h, off_x : off_x + t_w, :]
        return o
