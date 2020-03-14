import os
from pathlib import Path
from host_setup.datab import DataB
from host_setup.decorators import logger
from host_setup.process import Process

class ScanDir:
    def __init__(self, path: str, api=os.getenv['BASEPLEXDB']):
        self.path = path
        self.api = DataB(api)
        self.scan_dir()

    @logger
    def scan_dir(self):
        # perform these in a lazy or non-blocking manner
        for dir in os.scandir(self.path):
            self.gen_process(dir, self.api)
    
    @staticmethod
    @logger
    def gen_process(dir, api):
        return Process(dir, api)