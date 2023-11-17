import os

from olympict.files.o_video import OlympVid


class FolderOperation:
    def __init__(self, folder: str) -> None:
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def change_folder_path(self, o: OlympVid) -> OlympVid:
        o.change_folder_path(self.folder)
        return o
