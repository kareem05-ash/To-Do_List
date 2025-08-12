# This is a program implements a to-do list to moderate tasks
# --------------------- Author --------------------- #
# Name: Kareem Ashraf Mostafa
# E-Mail: kareem.ash05@gmail.com
# Phone: +201002321067 / +201154398353
# ---------------- Program Features ---------------- #
# Add new task
# Finish a specific task acording to its index
# Delete a specific task acording to its index
# Show a specific task acording to its index
# Show the current task list with status (finished or not finished)


# Tasks List
tasks = []

# User Interface
print("Hello, World!")
# User Interface Funtion
def user_interface():
    valid_choice = False
    while valid_choice == False: 
        choice = input("""Choose Operation
If you want to show your tasks, write (show)
If you want to show a specific task, write (show_task)
If you want to add a task, write (add)
If you want to finish a task, write (finish)
If you want to delete a specific task, write (delete)\n""").lower()
        if choice in ("show", "add", "delete", "finish", "show_task"): 
            valid_choice = True
            print(f"Your Choice: {choice}")
        else: 
            print("Invalid operation. Please, try again")
    return choice


# Functions
# Add a new task Function
def add():
    task = [(input("Enter the task: "))]
    task.append((input("Enter the dead line: ")))
    task.append("Not Finished")
    tasks.append(task)
    
# Show all tasks Funtion
def show():
    if not tasks:
        print("There is no any task assigned.\nChoose method (add) to asign tasks first.")
    else:
        print()     # print new line
        count = 1
        for task in tasks: 
            print(f"Task({count}): {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"status: {task[2]}")
            count += 1
            print()     # print new line

# Show a specific task Funciton
def show_task(): 
    valid_task_number = False
    while not valid_task_number:
        task_number = int(input("Enter the task(to be shown) mumber: "))
        if task_number <= len(tasks):
            valid_task_number = True
            task = tasks[task_number - 1]
            print(f"Task({task_number}): {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
        else:
            valid_task_number = False
            print(f"Sorry, the entered task number({task_number}) is in-valid. Try {len(tasks)} or less.")

# Delete a specific task Function
def delete():  
    valid_task_number = False
    while not valid_task_number:
        deleted_task_number = int(input("Enter the task(to be deleted) number: "))
        if deleted_task_number <= len(tasks):
            valid_task_number = True
            print(f"The deleted task: {tasks.pop(deleted_task_number - 1)}")
        else: 
            valid_task_number = False
            print(f"Sorry, the entered task number({deleted_task_number}) is in-valid. Try {len(tasks)} or less.")


# Finish a specific task Funciton
def finish(): 
    valid_task_number = False
    while not valid_task_number:
        finished_task_number = int(input("Enter the task(to be finished) number: "))
        if finished_task_number <= len(tasks):
            valid_task_number = True
            if tasks[finished_task_number - 1][2] == "Finished":
                print(f"Task({finished_task_number}) is already finished: {tasks[finished_task_number - 1]}")
            else:
                tasks[finished_task_number - 1][2] = "Finished"
                print(f"The finished task: {tasks[finished_task_number - 1]}")
        else:
            valid_task_number = False
            print(f"Sorry, the entered task number({finished_task_number}) is in-valid. Try {len(tasks)} or less.")


# Programe Implementation
exit = 0
while not exit: 
    choice =user_interface()
    if choice == "show": 
        show()
    elif choice == "show_task": 
        show_task()
    elif choice == "add": 
        add()
    elif choice == "finish": 
        finish()
    elif choice == "delete": 
        delete()
    else:
        print(f"XXXXXXX Error XXXXXXX: Invalid Choice = {choice}")
    exit = int(input("If you want to exit the program, write (1). Else, write (0): "))
print("Good, Buy!")