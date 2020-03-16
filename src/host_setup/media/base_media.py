from abc import ABC, abstractmethod, abstractstaticmethod, abstractproperty
from typing import List
from pathlib import Path
from glob import glob
import os
from host_setup.media.media_target import MediaTarget


class BaseMedia(ABC):
    def __init__(
        self,
        typ: str,
        path: str,
        target_typ: str,
        convert_typs: List[str],
        other_typs: List[str] = None,
    ):
        self.typ = typ
        self.path = path
        self.target_typ = target_typ
        self.convert_typs = convert_typs
        self.other_typs = other_typs

    def __repr__(self):
        return f"""{self.__class__.__name__}
         name: {self.name}  
         path: {self.path}  
         target_typ : {self.target_typ}  
         convert_typs : {self.convert_typs}  
         other_typs : {self.other_typs}"""

    @abstractmethod
    def process_media(self):
        pass

    @property
    def name(self):
        return os.path.basename(self.path)

    @property
    def valid_types(self):
        return [self.target_typ, *self.other_typs]

    @property
    def r_path(self):
        return str(self.path)

    @property
    def needs_convert(self):
        to_convert = self.to_convert_files
        valid = self.target_file
        if len(to_convert) == 0 and valid != 0:
            return False
        else:
            return True

    @property
    def to_convert_files(self):
        return self._get_files(self.path, self.convert_typs)

    @property
    def target_file(self):
        return self._get_files(self.path, self.target_typ)

    @property
    def is_valid(self):
        return len(self._get_files(self.path, self.valid_types))

    @staticmethod
    def _get_files(path: str, file_types: List[str]) -> List[str]:
        return [p for p in Path(path).rglob("*") if p.suffix in file_types]
