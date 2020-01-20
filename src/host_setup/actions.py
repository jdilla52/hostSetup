import os
from pathlib import Path
from host_setup.datab import DataB
from pathlib import Path
from glob import glob
from typing import List

EXCLUDE = ["vpn"]
VALID_VIDEO = [".mp4", ".avi"]
VALID_OTHER = [".srt"]


class AttemptInsert:
    def __init__(self, path: str, api: object):
        print(path)
        self.path = path
        self.api = api
        self.valid = self.check_for_video(path)
        self.status = self.attempt_insert()

    def check_for_video(self, path: str):
        """checks for a valid video file in a given directory
        
        Arguments:
            path {str} -- a path where you would like to    
        
        Returns:
            valid -- a true or false representing if a video file is present
        """
        potentials = self.get_files(path, VALID_VIDEO)

        if len(potentials) > 0:
            return True
        else:
            return False

    @staticmethod
    def get_files(path: str, file_types: List[str]) -> List[str]:
        return [p for p in Path(path).rglob("*") if p.suffix in file_types]

    def attempt_insert(self):
        """if there is a valid video file check if 
        """
        if self.valid:
            valid = self.api.select_task_by_param("name", self.path)
            print(valid)
            if len(valid) == 0:
                print("this video hasn't be started")
                self.api.create_new_task(self.path)
                return 0
            elif len(valid) == 1:
                task = self.api.select_task_by_param("name", self.path)
                print(task)
                return task[0][3]
            else:
                # TODO find something smart to do
                print("there's a problem we should kill one")


def find_downloads(path, api):
    # Set the directory you want to start from
    for sub_dir in os.listdir(path):
        if sub_dir not in EXCLUDE:
            given_dir = os.path.join(path, sub_dir)
            AttemptInsert(given_dir, api)
