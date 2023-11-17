import os

from olympict.files.o_image import OlympImage


class FolderSaver:
    def __init__(self, folder: str = ".") -> None:
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def save_to_folder(self, o: "OlympImage") -> "OlympImage":
        o.change_folder_path(self.folder)
        o.save()
        return o

    def save(self, o: "OlympImage") -> "OlympImage":
        o.save()
        return o
