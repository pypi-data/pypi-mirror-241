from typing import Callable, Optional, Sequence

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import BBoxHF


class BBoxHFPainter:
    def __init__(
        self,
        path_fn: Callable[[OlympImage], Sequence[BBoxHF]],
        font_scale: float,
    ):
        self.path_fn = path_fn
        self.font_scale = font_scale

    def draw_relatives(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for x1, y1, x2, y2, class_name, class_id, score, _ in self.path_fn(o):
            if score is None:
                score = 0
            color = ImTools.get_random_color(class_id)
            o.img = ImTools.draw_relative_bbox(
                o.img, (x1, y1, x2, y2, class_name, score), color, self.font_scale
            )
        return o

    @staticmethod
    def bbox_pipe_drawer(
        bbox_function: Optional[Callable[[OlympImage], Sequence[BBoxHF]]] = None,
        font_scale: float = ImTools.font_scale,
    ) -> Callable[[OlympImage], OlympImage]:
        if bbox_function is None:
            bbox_function = ImTools.default_bbox_path

        bp = BBoxHFPainter(bbox_function, font_scale)
        return bp.draw_relatives
