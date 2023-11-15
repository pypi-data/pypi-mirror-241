import cv2

from olympict.files.o_image import OlympImage


class DebugWindow:
    def __init__(self, name: str) -> None:
        self.name = name

    def show(self, o: "OlympImage") -> "OlympImage":
        cv2.imshow(self.name, o.img)
        _ = cv2.waitKey(1)
        return o
