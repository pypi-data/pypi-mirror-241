from typing import Callable

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Img


class HeatmapOperation:
    def __init__(self, heatmap_function: Callable[[OlympImage], Img]):
        self.heatmap_function = heatmap_function

    def draw_heatmap(
        self,
        o: OlympImage,
    ) -> OlympImage:
        outputs = self.heatmap_function(o)
        o.img = ImTools.draw_heatmap(o.img, outputs)
        return o
