import homepage, main

# Adds tasks
def create_task(desc: str, due: int, cat: str):
    homepage.task_list.append([False, desc, due, cat])

    print("Your task has been successfully added to the list of existing tasks")

def add_task_details():
    print("You are on task creation menu!")
    description = input("Please enter task description: ")

    while True:
        try:
            due_date = int(input("Please enter task due date (days): "))
            break
        except ValueError:
            print("Your input should be a whole number")

    print(f"This is a list of existing task categories: {homepage.task_categories}")

    while True:
        category = input("Please enter a task category: ")

        if category not in homepage.task_categories:
            print("You entered a non-existent category")
        else:
            break

    create_task(description, due_date, category)
'''
# Displays tasks
def display_tasks():
    print()
    if not Homepage.task_list:
        print("No tasks available")
        return

    print("Tasks:")
    for i in range(len(Homepage.task_list)):
        try:
            status = "[X]" if Main.completed[i] else "[ ]"
        except:
            status = "[ ]"
        print(f"{status} {i + 1}: {Homepage.task_list[i]['description']}")
        print(f" Due: {Homepage.task_list[i]['due']}")
        print(f" Category: {Homepage.task_list[i]['category']}\n")
'''
'''
# Marks a task as completed
def mark_completed(task_number):
    print()
    if 1 <= task_number <= len(Homepage.task_list):
        Main.completed[task_number - 1] = True
        print("Marked as completed")
    else:
        print("Invalid")
'''
'''
def __main__():
    while True:
        print()
        print("Options: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("q. Quit")

        choice = input("Choose an option: ")

        match choice:
            case '1':
                add_tasks()
            case '2':
                display_tasks()
            case '3':
                try:
                    print()
                    task_num = int(input("Enter task number to mark as completed: "))
                    mark_completed(task_num)
                except ValueError:
                    print("Invalid")
            case 'q':
                break
            case _:
                print("Invalid")
'''