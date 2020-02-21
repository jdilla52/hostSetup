import os
from host_setup.datab import DataB
from host_setup.process import state_manager
import pytest


def test_create_connection(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(path)


def test_state_manager(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/movie2")
    db_path = os.path.join(test_data_dir, "test.db")
    db = DataB(db_path)
    db.create_new_table()

    @state_manager(db)
    def dumb_def(hello):
        print(hello)
        print()

    dumb_def("sdfsdf")
    # db.delete_database()
