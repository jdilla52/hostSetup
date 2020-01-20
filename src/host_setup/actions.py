import os
from pathlib import Path
from host_setup.datab import DataB
from pathlib import Path
from glob import glob

EXCLUDE = ["vpn"]
VALID_VIDEO = [".mp4", ".avi"]
VALID_OTHER = [".srt"]


class AttemptInsert:
    def __init__(self, path, api):
        print(path)
        self.path = path
        self.api = api
        self.video = self.check_for_video(path)
        self.name = self.get_status()

    @staticmethod
    def check_for_video(path):
        potentials = [p for p in Path(path).rglob("*") if p.suffix in VALID_VIDEO]
        if len(potentials) == 1:
            return potentials[0]
        elif len(potentials) > 1:
            # search file sizes and get largest - or maybe use all of them
            return potentials[0]
        else:
            return None

    # @property
    # def get_name():
    #     print(self.video)

    def get_status(self):
        valid = self.api.select_task_by_param("name", str(self.video))
        print(valid)


def insert_file(name):
    name = name


def find_downloads(path, api):
    # Set the directory you want to start from
    for sub_dir in os.listdir(path):
        if sub_dir not in EXCLUDE:
            pathn = os.path.join(path, sub_dir)
            ai = AttemptInsert(path, api)
