import os
from typing import Any, Callable, List, Optional

import cv2  # type: ignore
import numpy as np

from olympict.files.o_image import OlympImage
from olympict.files.o_video import OlympVid


class VideoSaver:
    def __init__(self, output_name: str, fps: int = 30):
        self.writer: cv2.writer
        self.empty: bool = True
        self.fps = fps
        self.output_path = output_name

    def new_writer(self, w: int, h: int):
        self.writer = cv2.VideoWriter(
            self.output_path, cv2.VideoWriter_fourcc(*"mp4v"), self.fps, (w, h)
        )
        self.empty = False

    def add_frame(self, frame: cv2.Mat):
        if self.empty:
            self.new_writer(*frame.shape[:2][::-1])
        self.writer.write(frame.astype(np.uint8))

    def finish(self):
        self.writer.release()


class PipelineVideoSaver:
    def __init__(
        self, img_to_path_function: Callable[[OlympImage], str], fps: int = 25
    ):
        self.vs: Optional[VideoSaver] = None
        self.fps = fps
        self.img_to_path_function = img_to_path_function
        self.last_path: str
        self.metadata: List[Any] = []

    def _ensure_folder(self, path: str):
        folder = os.path.dirname(path)
        os.makedirs(folder, exist_ok=True)

    def add_frame(self, file: OlympImage) -> None:
        self.vs.add_frame(file.img)
        self.metadata.append(file.metadata)

    def process_file(self, file: OlympImage) -> Optional[OlympVid]:
        path = self.img_to_path_function(file)
        self._ensure_folder(path)
        if self.vs is None:
            self.vs = VideoSaver(path, self.fps)
            self.add_frame(file)
        elif self.vs.output_path == path:
            self.add_frame(file)
        else:
            self.vs.finish()
            self.vs = VideoSaver(path, self.fps)
            self.add_frame(file)
            output_vid = OlympVid(path=self.last_path, metadata=self.metadata)
            self.metadata = []
            return output_vid
        self.last_path = path
        return None

    def finish(self):
        if self.vs is not None:
            self.vs.finish()
