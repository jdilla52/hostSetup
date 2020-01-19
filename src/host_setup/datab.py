import sqlite3
from sqlite3 import Error

DATAB_DEF = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""

class DataB:
    def __init__ (self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn
    
    
    def create_new_table(self):
        """ create a table from the create_table_sql statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(DATAB_DEF)
        except Error as e:
            print(e)

    def create_task(self, task):
        """
        Create a new task
        :param task:
        :return:
        """
    
        sql = ''' INSERT INTO tasks(name,priority,status_id,begin_date,end_date)
                VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid

    def update_task(self, task):
        """
        update priority, begin_date, and end date of a task
        :param task:
        :return: project id
        """
        sql = ''' UPDATE tasks
                SET priority = ? ,
                    begin_date = ? ,
                    end_date = ?
                WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, task)
        self.conn.commit()

    def delete_task(self, id):
        """
        Delete a task by task id
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()
    
    
    def delete_all_tasks(self):
        """
        Delete all rows in the tasks table
        :return:
        """
        sql = 'DELETE FROM tasks'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def select_all_tasks(self):
        """
        Query all rows in the tasks table
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks")
    
        return cur.fetchall()
    
    def select_task_by_priority(self, priority):
        """
        Query tasks by priority
        :param priority:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    
        return cur.fetchall()