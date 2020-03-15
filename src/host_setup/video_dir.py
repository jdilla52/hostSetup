from pathlib import Path
from glob import glob
from typing import List
import os

EXCLUDE = ["vpn"]
VALID_VIDEO = [".mp4", ".avi"]
VALID_OTHER = [".srt"]


class VideoDir:
    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)

    def __repr__(self):
        return f"\n{self.__class__.__name__} \n path: {self.path} \n name: {self.name}"

    @staticmethod
    def _get_files(path: str, file_types: List[str]) -> List[str]:
        return [p for p in Path(path).rglob("*") if p.suffix in file_types]

    @property
    def r_path(self):
        return str(self.path)

    @property
    def valid_video(self):
        """checks for a valid video file in a given directory
        Returns:
            valid -- a true or false representing if a video file is present
        """
        potentials = self.video_files
        print(potentials)

        if len(potentials) > 0:
            return True
        else:
            return False  # build helpers into class

    @property
    def video_files(self):
        return self._get_files(self.path, VALID_VIDEO)

    @property
    def subtitles(self):
        return self._get_files(self.path, VALID_OTHER)
