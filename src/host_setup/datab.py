import sqlite3
from sqlite3 import Error
import os
from datetime import datetime


DATAB_DEF = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    processing bool NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""


class DataB:
    def __init__(self, db_file):
        self.path = db_file
        self.conn = self.create_connection(db_file)

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
         specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    @property
    def get_start_time(self):
        # datetime object containing current date and time
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def create_new_table(self):
        """ create a table from the create_table_sql statement
        :return:
        """
        try:
            self.cursor.execute(DATAB_DEF)
        except Error as e:
            print(e)

    def create_new_task(self, name, priority=0, status_id=0):
        """
        Create a new task for tracking. this is a helper around _create_task
        :param name : str
        :param priority : int
        :param status_id : int
        :return: id : int
        """
        task = (name, priority, status_id, self.get_start_time, "-")
        self.create_task(task)

    def create_task(self, task):
        """
        Create a new task
        :param task:
        :return:
        """

        sql = """ INSERT INTO tasks(name,priority,status_id,begin_date,end_date)
                VALUES(?,?,?,?,?) """
        self.cursor.execute(sql, task)
        self.commit()
        return self.cursor.lastrowid

    def update_task(self, task):
        """
        update priority, begin_date, and end date of a task
        :param task:
        """
        sql = """ UPDATE tasks
                SET name = ? ,
                    priority = ? ,
                    status_id = ? ,
                    processing = ? ,
                    begin_date = ? ,
                    end_date = ?
                WHERE id = ?"""
        self.cursor.execute(sql, task)
        self.conn.commit()

    def update_task_param(self, param, val, task_id):
        """
        update priority, begin_date, and end date of a task
        :param task:
        """
        sql = f""" UPDATE tasks
                SET {param} = ?
                WHERE id = ?"""
        self.cursor.execute(sql, (val, task_id))
        self.conn.commit()

    def select_all_tasks(self):
        """
        Query all rows in the tasks table
        :return:
        """
        self.cursor.execute("SELECT * FROM tasks")

        return self.cursor.fetchall()

    def select_task_by_param(self, param, term):
        """
        Query tasks by priority
        :param priority:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM tasks WHERE {param}=?", (term,))

        return cur.fetchall()

    def get_task_status(self, name):
        task = self.select_all_tasks("name", name)

        if len(task) == 0:
            print("this video hasn't be started")
            return 0
        elif len(task) == 1:
            if task[0][4]:
                return -1

            else:
                return task[0][3]
        else:
            # TODO find something smart to do
            print(task)
            print("there's a problem we should kill one")
            return task[0][3]

    def select_task_status(self, param, term):
        """
        Query tasks 
        :param priority:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM tasks WHERE {param}=?", (term,))

        return self.cursor.fetchall()

    def delete_task(self, id):
        """
        Delete a task by task id
        :param id: id of the task
        :return:
        """
        sql = "DELETE FROM tasks WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def delete_all_tasks(self):
        """
        Delete all rows in the tasks table
        :return:
        """
        sql = "DELETE FROM tasks"
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_database(self):
        """
        Delete the base .db file
        :return:
        """
        self.conn.close()
        os.remove(self.path)
