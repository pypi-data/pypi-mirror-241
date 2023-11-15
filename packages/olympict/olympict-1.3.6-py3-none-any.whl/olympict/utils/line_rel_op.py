from typing import Callable, List, Tuple

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, LineRelative


class LineRelativeOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[LineRelative, Color]]],
    ):
        self.line_function = polygon_function

    def draw_relative_lines(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for line, color in self.line_function(o):
            o.img = ImTools.draw_relative_line(o.img, line, color)

        return o
