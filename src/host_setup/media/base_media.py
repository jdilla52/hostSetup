from abc import ABC, abstractmethod, abstractstaticmethod, abstractproperty
from typing import List
from pathlib import Path
from glob import glob
import os
from host_setup.media.media_target import MediaTarget


class BaseMedia(ABC):
    def __init__(self, data: MediaTarget):
        self.path = data.path
        self.target_typ = data.target
        self.convert_typs = data.to_convert
        self.other_typs = data.valid_other

    def __repr__(self):
        return f"\n{self.__class__.__name__} \n  name: {self.name} \n path: {self.path} \n target_typ : {self.target_typ} \n convert_typs : {self.convert_typs} \n other_typs : {self.other_typs}"

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
