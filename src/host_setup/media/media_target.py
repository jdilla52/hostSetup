from dataclasses import dataclass
from typing import List

@dataclass
class MediaTarget:
    target : str
    to_convert : List[str]
    valid_other : List[str] = None

    def all_valid(self):
        return [self.target, *self.valid_other]