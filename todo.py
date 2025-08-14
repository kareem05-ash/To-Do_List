# This is a program implements a to-do list to moderate tasks
# --------------------- Author --------------------- #
# Name: Kareem Ashraf Mostafa
# E-Mail: kareem.ash05@gmail.com
# Phone: +201002321067 / +201154398353
# ---------------- Program Features ---------------- #
# Add new task
# Finish a specific task acording to its index
# Unfinishe a specific task according to its index
# Delete a specific task acording to its index
# Edit a specific task according to its index
# Show a specific task acording to its index
# Show the current task list 
# Swap two tasks (Configurable Priority)
# Save changes to an external file (tasks.txt)
# Load task list from the file (tasks.txt)


print("Hello, World!")
tasks = []  # Task List
not_finished_status = "Not Finished"

finished_status = "Finished"

# User Interface Funtion
def user_interface():
    valid_choice = False
    while not valid_choice: 
        choice = input("""
-------------------- Choose Operation --------------------
Write (exit)        if you want to exit from the program
Write (show)        if you want to show your tasks 
Write (show_task)   if you want to show a specific task 
Write (add)         if you want to add a task 
Write (finish)      if you want to finish a task 
Write (unfinish)    if you want to unfinish a task 
Write (delete)      if you want to delete a specific task 
Write (edit)        if you want to edit a specific task 
Write (swap)        if you want to swap 2 tasks
Write (save)        if you want to save task list to file (tasks.txt)
Write (load)        if you want to load task list from file (tasks.txt)
""").lower()
        if choice in ("show", "add", "delete", "finish", "unfinish", "show_task", "edit", "swap", "exit", "save", "load"): 
            valid_choice = True
            print(f"Your Choice: {choice}")
        else: 
            print("Invalid operation. Please, try again")
    return choice


# Functions
# Add a new task Function
def add():
    task = [(input("Enter Task Name: "))]
    task.append((input("Enter Task Due Date: ")))
    task.append(not_finished_status)
    decision = input("Do you want to add a NOTE for this task? (y/n): ")
    if decision == 'y': 
        task.append(input("Enter NOTE: "))
    else: 
        task.append("NONE")
    tasks.append(task)

# Show all tasks Funtion
def show():
    if not tasks:
        print("There are no assigned tasks.\nChoose method (add) to asign tasks first.")
    else:
        print()     # print new line
        count = 1
        for task in tasks: 
            print(f"----------- Task({count}) -----------")
            print(f"Name: {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
            print(f"NOTE: {task[3]}")
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
            print()     # print new line
            print(f"----------- Task({task_number}) -----------")
            print(f"Name: {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
            print(f"NOTE: {task[3]}")
            print()     # print new line
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
            if tasks[finished_task_number - 1][2] == finished_status:
                print(f"Task({finished_task_number}) is already finished: {tasks[finished_task_number - 1]}")
            else:
                tasks[finished_task_number - 1][2] = finished_status
                print(f"The finished task: {tasks[finished_task_number - 1]}")
        else:
            valid_task_number = False
            print(f"Sorry, the entered task number({finished_task_number}) is in-valid. Try {len(tasks)} or less.")

# Unfinishe a specific task Funciton
def unfinish(): 
    while True: 
        unfinished_task_number = int(input("Enter the task(to be unfinished) number: "))
        if unfinished_task_number <= len(tasks): 
            if tasks[unfinished_task_number - 1][2] == not_finished_status:
                print(f"Task({unfinished_task_number}) is already unfinished: {tasks[unfinished_task_number - 1]}")
            else:
                tasks[unfinished_task_number - 1][2] = not_finished_status
                print(f"The unfinished task: {tasks[unfinished_task_number - 1]}")
            break
        else: 
            print(f"Sorry, the entered number ({unfinished_task_number}) is in-valid. Try {len(tasks)} or less")

# Edit a specific task Function
def edit():
    while True:
        edited_task_number = int(input("Enter the task(to be edited) number: "))
        if edited_task_number <= len(tasks): 
            print("The task to be edited:")
            task = tasks[edited_task_number - 1]
            print(f"Task({edited_task_number}): {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
            print(f"NOTE: {task[3]}\n")
            task[0] = input("Edit Task Name: ")
            task[1] = input("Edit Task Due Date: ")
            task[2] = not_finished_status
            task[3] = input("Edit Task NOTE: ")
            break
        else: 
            print(f"Sorry, the entered task number({edited_task_number}) is in-valid. Try {len(tasks)} or less.")

# Swap 2 tasks Funciton
def swap():
    while True: 
        first_task_number = int(input("Enter the first task(to be swapped) number: "))
        second_task_number = int(input("Enter the second task(to be swapped) number: "))
        if first_task_number == second_task_number: 
            print(f"Sorry, you've entered the same number for both. task({first_task_number}), task({second_task_number}). Try different 2 numbers up to {len(tasks)}")
        elif first_task_number <= len(tasks) and second_task_number <= len(tasks): 
            # temporary list stores the first task
            temp = tasks[first_task_number - 1]     
            # swapping
            tasks[first_task_number - 1] = tasks[second_task_number - 1]
            tasks[second_task_number - 1] = temp
            print("Swapping's done successfully")
            break
        else: 
            print(f"Sorry, the entered task bumbers ({first_task_number}), ({second_task_number}) are in-valid. Try {len(tasks)} or less")


# Save tasks into external file Funciotn
def save_tasks(): 
    with open("tasks.txt", "w") as file: 
        for task in tasks: 
            task_line = "|".join(task)
            file.write(f"{task_line}\n")
    print("Tasks saved successfully to (tasks.txt)")


# Load task list from (tasks.txt) Function
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file: 
                task = line.split("|")
                tasks.append(task)
        print("Tasks loaded successfully from (tasks.txt)")
    except FileExistsError:
        print("No existing tasks file found. Starting with empty task list.")
    except Exception as e:
        print(f"Error loading tasks: {e}")



# Main Programe Implementation
load_tasks() # load task list with the saved tasks in (tasks.txt)
while True: 
    choice =user_interface()
    if choice == "show": 
        show()
    elif choice == "show_task": 
        show_task()
    elif choice == "add": 
        add()
    elif choice == "finish": 
        finish()
    elif choice == "unfinish": 
        unfinish()
    elif choice == "delete": 
        delete()
    elif choice == "edit": 
        edit()
    elif choice == "swap": 
        swap()
    elif choice == "save":
        save_tasks()
    elif choice == "load": 
        load_tasks()
    elif choice == "exit":
        break
    else:
        print(f"XXXXXXX Error XXXXXXX: Invalid Choice = {choice}")
print("Goodbuy!")