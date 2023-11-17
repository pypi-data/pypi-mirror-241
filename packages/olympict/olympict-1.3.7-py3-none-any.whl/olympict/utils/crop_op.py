from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color


class CropOperation:
    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        right: int = 0,
        bottom: int = 0,
        pad_color: Color = (0, 0, 0),
    ) -> None:
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.pad_color = pad_color

    def task(self, o: OlympImage) -> OlympImage:
        o.img = ImTools.crop_image(
            o.img,
            top=self.top,
            left=self.left,
            bottom=self.bottom,
            right=self.right,
            pad_color=self.pad_color,
        )
        return o
