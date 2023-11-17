from typing import Callable, Optional, Sequence

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import BBoxAbsolute


class BBoxAbsolutePainter:
    def __init__(
        self,
        path_fn: Optional[Callable[[OlympImage], Sequence[BBoxAbsolute]]] = None,
        font_scale: float = 1.0,
    ):
        self.path_fn = BBoxAbsolutePainter.default_path if path_fn is None else path_fn
        self.font_scale = font_scale

    def default_path(self, o: "OlympImage") -> Sequence[BBoxAbsolute]:
        return o.metadata["pred_bboxes"]

    def draw_absolute(self, o: "OlympImage") -> "OlympImage":
        for x1, y1, x2, y2, class_name, score in self.path_fn(o):
            if score is None:
                score = 0
            class_id = abs(hash(class_name)) % (10**4)
            color = ImTools.get_random_color(class_id)
            o.img = ImTools.draw_bbox(
                o.img, (x1, y1, x2, y2, class_name, score), color, self.font_scale
            )

        return o
