from typing import Callable, List, Tuple

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, LineAbsolute


class LineAbsoluteOperation:
    def __init__(
        self,
        line_function: Callable[[OlympImage], List[Tuple[LineAbsolute, Color]]],
    ):
        self.line_function = line_function

    def draw_absolute_lines(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for line, color in self.line_function(o):
            o.img = ImTools.draw_line(o.img, line, color)

        return o
