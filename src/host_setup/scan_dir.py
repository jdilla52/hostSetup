import os
from pathlib import Path
from host_setup.datab import DataB
from host_setup.decorators import logger
from host_setup.process import Process


class ScanDir:
    def __init__(
        self, video_dir: str,
    ):
        self.video_dir = video_dir
        self.api = DataB()
        self.scan_dir()

    # @logger
    def scan_dir(self):
        # perform these in a lazy or non-blocking manner
        for dir in os.scandir(self.video_dir):
            self.gen_process(dir, self.api)

    @staticmethod
    # @logger
    def gen_process(dir, api):
        return Process(dir, api)
