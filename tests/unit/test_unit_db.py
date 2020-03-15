import os
from host_setup.datab import DataB
import pytest


def test_create_connection(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    assert os.path.exists(path)


def test_create_new_table(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.create_new_table()

def test_create_new_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.create_new_task("test" , "./sdg")
    db.create_new_task("test2", "./sdg")
    db.create_new_task("test3", "./sdg")
    db.create_new_task("test4", "./sdg")

    tasks = db.select_all_tasks()
    print(len(tasks))
    assert len(tasks) == 4


def test_select_all_tasks(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    tasks = db.select_all_tasks()
    assert len(tasks) == 4


def test_select_task_by_param(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    tasks = db.select_task_by_param("priority", 0)
    assert len(tasks) == 4


def test_select_task_by_name(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    tasks = db.select_task_by_param("priority", 0)
    assert len(tasks) == 4


def test_update_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    task_data = ("bbb", "sdf", 0, 2, 0, "2015-01-01", "2015-01-02", 0)
    db.update_task(task_data)


def test_update_param(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.update_task_param("status", 2, 0)


def test_update_task_by_name(test_data_dir):

    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.update_task_by_name("status", 2, "test")

# def test_get_task_status(test_data_dir):
#     path = os.path.join(test_data_dir, "output/db.db")
#     db = DataB(db_path=path)
#     db.create_new_task("status test", "sdff")
#     db.update_task_by_name("status", 2, "status test")
#     status = db.get_task_status("status test")
#     assert status == 2

def test_get_task_param(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.create_new_task("status test", "sdff")
    db.update_task_by_name("status", 2, "status test")
    status = db.get_task_param("status", "status test")
    assert status == 2

def test_delete_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    cur_len = len(db.select_all_tasks())
    db.delete_task(1)
    new_len = len(db.select_all_tasks())
    assert (cur_len - new_len) == 1


def test_delete_all_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.delete_all_tasks()
    assert len(db.select_all_tasks()) == 0


def test_delete_db(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(db_path=path)
    db.delete_database()
    assert not os.path.exists(path)
