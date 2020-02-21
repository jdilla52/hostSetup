import os
from host_setup.actions import find_downloads
import pytest


def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    print(path)
    find_downloads(path)
    assert test_data_dir
