import os
from host_setup.runner import Runner
from host_setup.datab import DataB
from host_setup.env import Env
from host_setup.settings import Settings
import pytest


def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "input.toml")
    db_path = os.path.join(test_data_dir, "output/functional_db.db")

    # create a new table
    Env()

    print(os.environ["PLEXDB"])
    scan = Runner(Settings(path))
    scan.api.delete_database()
