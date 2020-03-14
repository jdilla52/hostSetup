import os
from host_setup.actions import ScanDir
from host_setup.datab import DataB
import pytest

def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    db_path = os.path.join(test_data_dir, "output/functional_db.db")

    #create a new table
    db = DataB(db_path)
    db.create_new_table()
    db.close()

    scan = ScanDir(path, api=db_path)
    assert test_data_dir

    scan.api.delete_database()
