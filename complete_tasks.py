# from homepage import task_list

def get_task_list():
    from homepage import task_list  # Import only when needed
    return task_list

# Runs through chores list and asks whether or not the chore is done
def complete_selected():
    task_list = get_task_list()

    print("Uncompleted Tasks:")

    for i in range(len(task_list)):
        if not task_list[i][0]:
            print(f" Task Number: {i + 1}")
            print(f" Description: {task_list[i][1]}")
            print(f" Due: {task_list[i][2]}")
            print(f" Category: {task_list[i][3]}\n")

            task_check = str(input('Complete this task? (Y / N): '))

            if task_check == 'Y':
                task_list[i][0] = True

            print("Selected Task has been completed")
