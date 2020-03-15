from abc import ABC, abstractmethod, abstractstaticmethod, abstractproperty
from typing import List
from pathlib import Path
from glob import glob
import os
from host_setup.media.media_target import MediaTarget

class BaseMedia(ABC):
    def __init__(self, path:str, settings:MediaTarget):
        self.path = path
        self.settings = settings

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def process_media(self):
        pass

    @property
    def name(self):
        return os.path.basename(self.path)

    @property
    def r_path(self):
        return str(self.path)
    
    @staticmethod
    def _get_files(path: str, file_types: List[str]) -> List[str]:
        return [p for p in Path(path).rglob("*") if p.suffix in file_types]

