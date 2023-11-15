from typing import Callable

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, Img


class SegmentationOperation:
    def __init__(
        self, segmentation_function: Callable[[OlympImage], Img], color: Color
    ):
        self.segmentation_function = segmentation_function
        self.color = color

    def draw_segmentation(
        self,
        o: OlympImage,
    ) -> OlympImage:
        segmap = self.segmentation_function(o)
        o.img = ImTools.draw_segmentation_map(o.img, segmap, self.color)
        return o
