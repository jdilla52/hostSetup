from dataclasses import dataclass
from typing import List


@dataclass
class MediaTarget:
    typ: str
    path: str
    target_typ: str
    convert_typs: List[str]
    other_typs: List[str] = None
