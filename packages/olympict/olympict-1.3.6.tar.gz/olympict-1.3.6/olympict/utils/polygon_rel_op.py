from typing import Callable, List, Tuple

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, PolygonRelative


class PolygonRelativeOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonRelative, Color]]],
    ):
        self.polygon_function = polygon_function

    def draw_relative_polygons(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for polygon, color in self.polygon_function(o):
            o.img = ImTools.draw_relative_polygon(o.img, polygon, color)
        return o
