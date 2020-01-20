import os
from pathlib import Path
from host_setup.datab import DataB
from pathlib import Path
from glob import glob
from typing import List

EXCLUDE = ["vpn"]
VALID_VIDEO = [".mp4", ".avi"]
VALID_OTHER = [".srt"]


def get_files(path: str, file_types: List[str]) -> List[str]:
    return [p for p in Path(path).rglob("*") if p.suffix in file_types]


class AttemptInsert:
    def __init__(self, path: str, api: object):
        print(path)
        self.path = path
        self.api = api
        self.valid = self.check_for_video(path)
        self.status = self.get_status()

    @staticmethod
    def check_for_video(path: str):
        """checks for a valid video file in a given directory
        
        Arguments:
            path {str} -- a path where you would like to    
        
        Returns:
            valid -- a true or false representing if a video file is present
        """
        potentials = get_files(path, VALID_VIDEO)

        if len(potentials) > 0:
            return True
        else:
            return False

    def get_status(self):
        """get the status of a given
        """
        task = self.api.select_task_by_param("name", self.path)

        if len(task) == 0:
            print("this video hasn't be started")
            return 0
        elif len(task) == 1:
            return task[0][3]
        else:
            # TODO find something smart to do
            print("there's a problem we should kill one")

    def actions(self):
        return {
            0: self.create_entry,
            1: self.convert_video,
            2: self.rclone,
            3: self.delete,
        }

    def create_entry(self, path, api):
        "if there is no video in sqlite"
        if self.check_for_video(path):
            self.api.create_new_task(path)

    @staticmethod
    def convert_video(path, api):
        # TODO Try to run fmpgg at several settings to convert data
        # "ffmpeg -i $file -c:v libx264 -crf 19 -hide_banner -loglevel panic -preset fast $newFile"
        print(path)

    @staticmethod
    def rclone(path, api):
        # "$RCLONE move --include "*.{mp4,srt}" --delete-empty-src-dirs $FILES wasab:wasab"
        pass

    @staticmethod
    def delete(path, api):
        os.remove(path)


def find_downloads(path, api):
    # Set the directory you want to start from

    for sub_dir in os.listdir(path):
        if sub_dir not in EXCLUDE:
            given_dir = os.path.join(path, sub_dir)
            AttemptInsert(given_dir, api)
