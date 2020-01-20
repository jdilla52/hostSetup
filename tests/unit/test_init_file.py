import os
from host_setup.actions import find_downloads, AttemptInsert
import pytest
from host_setup.datab import DataB


def test_find_downloads(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    db_path = os.path.join(test_data_dir, "test.db")
    db = DataB(db_path)
    db.create_new_table()
    find_downloads(path, db)
    # assert tables.valid is True
    # db.commit()
    # db.delete_database()


def test_attempt_insert(test_data_dir):
    path = os.path.join(test_data_dir, "downloads/")
    db_path = os.path.join(test_data_dir, "test.db")
    db = DataB(db_path)
    db.create_new_table()
    ai = AttemptInsert(path, db)
    assert ai.valid is True
    db.commit()
    db.delete_database()
