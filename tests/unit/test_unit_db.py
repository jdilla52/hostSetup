import os 
from host_setup.datab import DataB
import pytest

def test_create_connection(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    print(path)
    DataB(path)
    assert os.path.exists(path)

def test_create_new_table(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(path)
    db.create_new_table()

def test_create_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    task_1 = ('Analyze the requirements of the app', 1, 1, '2015-01-01', '2015-01-02')
    task_2 = ('Analyze the requirements of the app',0, 0, '2015-01-01', '2015-01-02')

    db = DataB(path)
    db.create_task(task_1)
    db.create_task(task_2)

def test_select_all_tasks(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    DataB(path).select_all_tasks()

def test_select_task_by_priority(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(path)
    db.select_task_by_priority(0)

def test_delete_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(path)
    db.delete_task(0)

def test_delete_all_task(test_data_dir):
    path = os.path.join(test_data_dir, "output/db.db")
    db = DataB(path)
    db.delete_all_tasks()