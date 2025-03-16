# from homepage import task_list

def get_task_list():
    from homepage import task_list  # Import only when needed
    return task_list

def display_all_tasks():
    task_list = get_task_list()

    if not task_list:
        print("No tasks available")
        return

    print("Tasks:")
    for i in range(len(task_list)):

        print(f" Task Number: {i + 1}")
        print(f" Task Status: {"[X]" if task_list[i][0] else "[ ]"}")
        print(f" Description: {task_list[i][1]}")
        print(f" Due: {task_list[i][2]}")
        print(f" Category: {task_list[i][3]}\n")

def display_tasks_by_category(category):
    task_list = get_task_list()

    flat_list = [task_detail for task in task_list for task_detail in task]

    if category not in flat_list:
        print(f"No tasks with {category} available")
        return

    print(f"{category} Category Tasks:")
    for i in range(len(task_list)):
        if task_list[i][3] == category:
            print(f" Task Number: {i + 1}")
            print(f" Task Status: {"[X]" if task_list[i][0] else "[ ]"}")
            print(f" Description: {task_list[i][1]}")
            print(f" Due: {task_list[i][2]}")

def display_completed_tasks():
    task_list = get_task_list()

    if not task_list:
        print("No completed tasks available")
        return

    print("Completed Tasks:")
    for i in range(len(task_list)):
        if task_list[i][0]:
            print(f" Task Number: {i + 1}")
            print(f" Description: {task_list[i][1]}")
            print(f" Due: {task_list[i][2]}")
            print(f" Category: {task_list[i][3]}\n")