import os
from host_setup.scan_dir import ScanDir
from host_setup.datab import DataB
from host_setup.env import Env
import pytest

def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    db_path = os.path.join(test_data_dir, "output/functional_db.db")

    #create a new table
    Env()
    print(os.environ["PLEXDB"])
    scan = ScanDir(path)
    scan.api.delete_database()
