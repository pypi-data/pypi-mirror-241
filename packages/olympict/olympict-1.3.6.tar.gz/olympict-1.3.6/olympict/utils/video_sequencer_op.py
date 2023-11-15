from typing import Any, Generator, Tuple, cast

import cv2

from olympict.files.o_image import OlympImage
from olympict.files.o_video import OlympVid
from olympict.types import Img


class VideoSequencer:
    def __init__(self) -> None:
        pass

    def generator(self, o: "OlympVid") -> Generator[OlympImage, None, None]:
        capture: Any = cv2.VideoCapture(o.path)
        res, frame = cast(Tuple[bool, Img], capture.read())
        idx = 0
        while res:
            new_path = f"{o.path}_{idx}.png"
            yield OlympImage.from_buffer(
                frame,
                new_path,
                metadata={
                    "video_path": o.path,
                    "video_frame": idx,
                    **(o.metadata[idx] if len(o.metadata) > idx else {}),
                },
            )
            res, frame = cast(Tuple[bool, Img], capture.read())
            idx += 1
        capture.release()
        return
