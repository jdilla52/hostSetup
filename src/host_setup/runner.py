import os
from pathlib import Path
from host_setup.datab import DataB
from host_setup.decorators import logger
from host_setup.process import Process
from host_setup.media.media_target import MediaTarget
from host_setup.media.tv import TV
from host_setup.media.video import Video
from typing import List


class Runner:
    def __init__(
        self, settings: List[MediaTarget],
    ):
        self.run_typs = settings.run_typs
        self.api = DataB()
        self.process_typs()

    @staticmethod
    def gen_local_media(settings: MediaTarget, local_path: str):
        new_type = {"Video": Video, "TV": TV}.get(settings.typ)
        local_media = new_type(**settings.__dict__)
        local_media.path = local_path
        return local_media

    def process_typs(self):
        # roll through each major type of file
        for typ in self.run_typs:
            # roll through each directory pointed to in typ
            for dir in os.scandir(typ.path):
                Process(self.gen_local_media(typ, dir), self.api)
