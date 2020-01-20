import os
from host_setup.actions import find_downloads
import pytest
from host_setup.datab import DataB


def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    db_path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path)

    find_downloads(path, db)
    # assert test_data_dir
