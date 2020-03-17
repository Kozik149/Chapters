from create_db import Tasks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import hashlib
import argparse

engine = create_engine('sqlite:///sky.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class MethodsForDB:
    def __init__(self):
        parser = argparse.ArgumentParser()
        self.method = parser.add_argument('method')
        self.hash_arg = parser.add_argument('task_hash', nargs='?')
        self.name_arg = parser.add_argument('-n', '--name', required=False, help='Set name of task.')
        self.description_arg = parser.add_argument('-de', '--description', required=False,
                                                   help='Set description of task.')
        self.deadline_arg = parser.add_argument('-d', '--deadline', required=False, help='Set deadline of task.')
        self.all_arg = parser.add_argument('-a', '--all', required=False, help='Show all tasks.', action='store_true')
        self.today_arg = parser.add_argument('-t', '--today', required=False, help='Show tasks from today.',
                                             action='store_true')
        self.args = parser.parse_args()

    def add_task(self, name=None, description=None, deadline=None):
        if deadline is None:
            deadline = datetime.datetime.now()
        else:
            string = str(deadline).split('-')
            deadline = datetime.date(int(string[0]), int(string[1]), int(string[2]))  # year, month, day
        connect = str(name) + str(description) + str(deadline)
        hash_value = hashlib.md5(connect.encode())
        task = Tasks(name=name, deadline=deadline, description=description, task_hash=hash_value.hexdigest())
        session.add(task)
        session.commit()

    def update_task(self, t_hash):
        query = session.query(Tasks).filter_by(task_hash=t_hash).first()
        if self.args.name:
            query.name = self.args.name
        if self.args.description:
            query.description = self.args.description
        if self.args.deadline:
            string = str(self.args.deadline).split('-')
            query.deadline = datetime.date(int(string[0]), int(string[1]), int(string[2]))
        session.commit()

    def remove_task(self, t_hash):
        query = session.query(Tasks).filter_by(task_hash=t_hash).first()
        session.delete(query)
        session.commit()

    def list_tasks(self):
        tasks = session.query(Tasks).all()
        for task in tasks:
            print(task.name, task.deadline, task.description, task.task_hash)

    def today_tasks(self):
        tasks = session.query(Tasks).filter(Tasks.deadline == datetime.datetime.now().date())
        for task in tasks:
            print(task.name, task.description, task.deadline, task.task_hash)

    def todo_function(self):
        if self.args.method == 'add':
            self.add_task(name=self.args.name, description=self.args.description, deadline=self.args.deadline)
        elif self.args.method == 'update':
            self.update_task(self.args.task_hash)
        elif self.args.method == 'list' and self.args.all:
            self.list_tasks()
        elif self.args.method == 'remove':
            self.remove_task(self.args.task_hash)
        elif self.args.method == 'list' and self.args.today:
            self.today_tasks()


if __name__ == '__main__':
    methods = MethodsForDB()
    methods.todo_function()
