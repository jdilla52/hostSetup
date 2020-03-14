import os
from pathlib import Path
from host_setup.datab import DataB

from host_setup.process import Process

DATABASELOCATION = "./b"


class ScanDir:
    def __init__(self, path: str, api=DATABASELOCATION):
        self.path = path
        self.api = DataB(api)
        self.scan_dir()

    def scan_dir(self):
        print(self.path)
        # perform these in a lazy or non-blocking manner
        for dir in os.scandir(self.path):
            print(dir)
            Process(dir, self.api)
