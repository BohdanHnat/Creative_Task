import homepage

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
