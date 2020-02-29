import pymysql
from secrets import *

def show_task(c):   # print all open tasks and their ids in order of ids
    select_stmt = """
        SELECT id, task FROM tasks WHERE done != 1 ORDER BY id;
    """
    c.execute(select_stmt)
    print(c.fetchall())

def mark_as_done(c, task_id):
    # update the done field in the table for given id
    c.execute("""
    UPDATE TASKS
    SET done == 1
    WHERE id = %s, task_id
    """)

def add_new_task(c, task_name):
    # insert a new record to the task db (with name)
    c.execute("""
    
    """)

#   1 Connect generalically to MySQL and create the todo_app database
db = pymysql.connect(host, user, password, "")  #  ne conectam generic , facem un cursor
with db.cursor() as c:
    c._defer_warnings = True
    c.execute("CREATE SCHEMA IF NOT EXISTS `todo_app` DEFAULT CHARACTER SET utf8;") # cream database todo_app
db.close()

#   2 Connect to newly created database todo_app
db = pymysql.connect(host, user, password, "todo_app")

#   3 Create tasks table
create_stmt = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    task TEXT NOT NULL,
    done BOOLEAN    # (TINYINT)
    );
"""

with db.cursor() as c:
    c.execute(create_stmt)
    # In a loop:
    # ○ ask user what to do using input()
    # ○ show task list
    # ○ mark task as done
    # ○ add new task
    # ○ exit application
while True:
    print("""
    Menu:
    1 - show task list
    2 - mark task as done
    3 - add new task
    4 - exit application
    """)
    option = int(input("Enter your choice: "))
    if option not in [1, 2, 3, 4]:
        continue    # daca optiunea nu este una din cele 4 , iti arata din nou meniul
    if option == 1:
        show_task(c)
    elif option == 2:
        # TODO: ask for id
        task_id = int(input("Enter the id: "))
        mark_as_done(c, task_id)
    elif option == 3:
        # TODO: ask for name
        add_new_task(c, task_name)
    elif option == 4:
        break
    #call function based on user option

db.close()
