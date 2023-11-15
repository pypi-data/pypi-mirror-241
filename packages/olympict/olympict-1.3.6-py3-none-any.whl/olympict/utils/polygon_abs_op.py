from typing import Callable, List, Tuple

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, PolygonAbsolute


class PolygonAbsoluteOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonAbsolute, Color]]],
    ):
        self.polygon_function = polygon_function

    def draw_absolute_polygons(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for polygon, color in self.polygon_function(o):
            o.img = ImTools.draw_polygon(o.img, polygon, color)
        return o
