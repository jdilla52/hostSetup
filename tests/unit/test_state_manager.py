import os
from host_setup.datab import DataB
from host_setup.media.tv import TV
from host_setup.process import state_manager, logger
import pytest


def test_state_manager(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/movie2")
    db_path = os.path.join(test_data_dir, "output/decorators.db")
    db = DataB(db_path)
    db.create_new_table()
    db.create_new_task("hello", "sss")

    @state_manager
    def dumb_def(video, api):
        print("hello")

    j = TV("sdf",
        path,
        ".mp4",
        ["s",""])
    dumb_def(j, db)

    
def test_logging(test_data_dir):
    @logger
    def dumb_def(hello):
        print(hello)
        print()

    dumb_def("sdfsdf")

def test_delete_db(test_data_dir):
    path = os.path.join(test_data_dir, "output/decorators.db")
    db = DataB(path)
    db.delete_database()
    assert not os.path.exists(path)