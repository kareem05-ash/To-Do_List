# This is a program implements a to-do list to moderate tasks
# --------------------- Author --------------------- #
# Name: Kareem Ashraf Mostafa
# E-Mail: kareem.ash05@gmail.com
# Phone: +201002321067 / +201154398353
# ---------------- Program Features ---------------- #
# Add new task
# Finish a specific task acording to its index
# Finish all tasks
# Unfinishe a specific task according to its index
# Unfinish all tasks
# Delete a specific task acording to its index
# Edit a specific task according to its index
# Show a specific task acording to its index
# Show the current task list 
# Swap two tasks (Configurable Priority)
# Auto save to (tasks.txt)
# Automatick loading tasks from (tasks.txt)
# Add a NOTE to an existing task

#               Not added yet
# 2 Counters: first one for finished tasks, second one for unfinished tasks
# Add status: to show number of finished tasks vs unfinished tasks out of number of all tasks
# Categorize shown tasks: finished & unfinished


print("Hello, World!")
tasks = []  # Task List
not_finished_status = "Not Finished"
finished_status = "Finished"

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
Write (add_note)    if you want to add a NOTE to an existing task
Write (edit_note)   if you want to edit the NOTE of an existing task
Write (finish)      if you want to finish a task 
Write (finish_all)  if you want to finish all tasks
Write (unfinish)    if you want to unfinish a task 
Write (unfinish_all)if you want to unfinish all tasks
Write (delete)      if you want to delete a specific task 
Write (edit)        if you want to edit a specific task 
Write (swap)        if you want to swap 2 tasks
Write (rst)         if you want to reset task file (tasks.txt)
""").strip().lower()
        if choice in ("show", "add", "delete", "finish", "unfinish", "show_task", "edit", "swap", "exit", "rst", "finish_all", "unfinish_all", "add_note", "edit_note"): 
            valid_choice = True
            print(f"Your Choice: {choice}")
        else: 
            print("Invalid operation. Please, try again")
    return choice

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Add a new task Function
def add():
    task = [(input("Enter Task Name: "))]
    task.append((input("Enter Task Due Date: ")))
    task.append(not_finished_status)
    while True:
        decision = input("Do you want to add a NOTE for this task? (y/n): ")
        if decision == 'y': 
            task.append(input("Enter NOTE: "))
            break
        elif decision == 'n': 
            task.append("NONE")
            break
        else:
            print("Sorry, please enter a valid choice!")
    tasks.append(task)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Show all tasks Funtion
def show():
    if not tasks:
        print("There are no assigned tasks.\nChoose method (add) to asign tasks first.")
    else:
        count = 1
        for task in tasks: 
            print(f"\n----------- Task({count}) -----------")
            print(f"Name: {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
            print(f"NOTE: {task[3]}")
            count += 1

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Show a specific task Funciton
def show_task(): 
    while True:
        task_number = valid_number("Enter the task(to be shown) mumber: ")  # asking a valid number from the user
        if task_number <= int(len(tasks)):
            task = tasks[task_number - 1]
            print(f"\n----------- Task({task_number}) -----------")
            print(f"Name: {task[0]}")
            print(f"Due Date: {task[1]}")
            print(f"Status: {task[2]}")
            print(f"NOTE: {task[3]}")
            break
        else:
            valid_task_number = False
            print(f"Sorry, the entered task number({task_number}) is in-valid. Try {len(tasks)} or less.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# Delete a specific task Function
def delete():  
    while True:
        deleted_task_number = valid_number("Enter the task(to be deleted) number: ")
        if deleted_task_number <= len(tasks):
            print(f"The deleted task: {tasks.pop(deleted_task_number - 1)}")
            with(open("tasks.txt", "w")) as file:
                file.truncate(0)
            save_tasks()
            break
        else: 
            print(f"Sorry, the entered task number({deleted_task_number}) is in-valid. Try {len(tasks)} or less.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Finish a specific task Funciton
def finish(): 
    while True:
        finished_task_number = valid_number("Enter the task(to be finished) number: ")
        if finished_task_number <= len(tasks):
            if tasks[finished_task_number - 1][2] == finished_status:
                print(f"Task({finished_task_number}) is already finished: {tasks[finished_task_number - 1]}")
            else:
                tasks[finished_task_number - 1][2] = finished_status
                print(f"The finished task: {tasks[finished_task_number - 1]}, length = {len(tasks[finished_task_number - 1])}")
            break
        else:
            print(f"Sorry, the entered task number({finished_task_number}) is in-valid. Try {len(tasks)} or less.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Unfinishe a specific task Funciton
def unfinish(): 
    while True: 
        unfinished_task_number = valid_number("Enter the task(to be unfinished) number: ")
        if unfinished_task_number <= len(tasks): 
            if tasks[unfinished_task_number - 1][2] == not_finished_status:
                print(f"Task({unfinished_task_number}) is already unfinished: {tasks[unfinished_task_number - 1]}")
            else:
                tasks[unfinished_task_number - 1][2] = not_finished_status
                print(f"The unfinished task: {tasks[unfinished_task_number - 1]}")
            break
        else: 
            print(f"Sorry, the entered number ({unfinished_task_number}) is in-valid. Try {len(tasks)} or less")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Edit a specific task Function
def edit():
    while True:
        edited_task_number = valid_number("Enter the task(to be edited) number: ")
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
            while True:
                decision = input("Do you want to add a NOTE for this task? (y/n): ")
                if decision == 'y': 
                    task[3] = (input("Enter NOTE: "))
                    break
                elif decision == 'n': 
                    task[3] = "NONE"
                    break
                else:
                    print("Sorry, please enter a vlaid choice!")
            break
        else: 
            print(f"Sorry, the entered task number({edited_task_number}) is in-valid. Try {len(tasks)} or less.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Swap 2 tasks Funciton
def swap():
    while True: 
        first_task_number = valid_number("Enter the first task(to be swapped) number: ")
        second_task_number = valid_number("Enter the second task(to be swapped) number: ")
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Save tasks into external file Funciotn
def save_tasks(): 
    with open("tasks.txt", "w") as file: 
        for task in tasks: 
            task_line = "|".join(task)
            file.write(f"{task_line}\n")
    print("Tasks saved successfully to (tasks.txt)")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load tasks from tasks.txt Function
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if not line:  # Skip empty lines
                    continue
                task = line.split("|")
                tasks.append(task)
        print("Tasks loaded successfully from (tasks.txt)")
    except FileNotFoundError:  # Changed from FileExistsError to FileNotFoundError
        print("No existing tasks file found. Starting with empty task list.")
    except Exception as e:
        print(f"Error loading tasks: {e}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reset task file Function
def rst():
    try:
        with(open("tasks.txt", "w")) as file:
            file.truncate(0)
            print("Reset tasks.txt: Done")
            global tasks
            tasks = []
    except FileNotFoundError: 
        print("No existing tasks file found. Starting with empty task list.")
    except Exception as e:
        print(f"Error resetting task file: {e}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Finish all tasks Function
def finish_all():
    for task_num in range(len(tasks)):
        tasks[task_num-1][2] = finished_status
    print("All tasks has been finished")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Unfinish all tasks Function
def unfinish_all():
    for task_num in range(len(tasks)):
        tasks[task_num-1][2] = not_finished_status
    print("All tasks has been unfinished")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Valid number from the user Function
def valid_number(msg):
    while True:
        number = input(f"{msg}")
        if number.isdigit():
            number = int(number)
            return number
        else:   
            print("Sorry, please enter a valid number!")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Add NOTE Function
def add_note():
    task_number = valid_number("Enter the task(to be noted) number: ")
    if tasks[task_number - 1][3] != "NONE":
        print(f"This task is already noted with: {tasks[task_number - 1][3]}")
        while True:
            decision = input("Do you want to edit the NOTE? (y/n): ")
            if decision == 'y': 
                tasks[task_number - 1][3] = input("Enter the NOTE: ")
                break
            elif decision == 'n': 
                break
            else:
                print("Sorry, please enter a valid choice!")
    else:
        tasks[task_number - 1][3] = input("Enter the NOTE: ")
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Edit NOTE Function
def edit_note():
    task_number = valid_number("Enter the task(to edit its NOTE) number: ")
    if tasks[task_number - 1][3] == "NONE":
        while True:
            decision = print("This task hasn't NOTE to be edited. Do you want to add a NOTE? (y/n) ")
            if decision == 'y':
                tasks[task_number - 1][3] = input("Enter the NOTE: ")
                break
            elif decision == 'n': 
                tasks[task_number - 1][3] = "NONE"
                break
            else:
                print("Sorry, please enter a valid choice!")
    else:
        print(f"Past NOTE: {tasks[task_number - 1][3]}")
        tasks[task_number - 1][3] = input("Enter the new NOTE: ")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        save_tasks()
    elif choice == "finish": 
        finish()
        save_tasks()
    elif choice == "unfinish": 
        unfinish()
        save_tasks()
    elif choice == "delete": 
        delete()
    elif choice == "edit": 
        edit()
        save_tasks()
    elif choice == "swap": 
        swap()
        save_tasks()
    elif choice == "rst": 
        rst()
    elif choice == "finish_all":
        finish_all()
        save_tasks()
    elif choice == "unfinish_all":
        unfinish_all()
        save_tasks()
    elif choice == "add_note":
        add_note()
        save_tasks()
    elif choice == "edit_note": 
        edit_note()
        save_tasks()
    elif choice == "exit":
        break
    else:
        print(f"XXXXXXX Error XXXXXXX: Invalid Choice = {choice}")
print("Goodbuy!")