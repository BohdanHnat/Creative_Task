from add_task import add_task_details
from complete_tasks import complete_selected
import sign_in_create_account, view_tasks

task_categories = ["Home", "Work", "School"]
task_list = [[True, "Description_1", "Due_date_1", "Home"],
             [False, "Description_2", "Due_date_2", "Home"],
             [True, "Description_3", "Due_date_3", "Work"],
             [True, "Description_4", "Due_date_4", "Work"],
             [False, "Description_5", "Due_date_5", "School"],
             [False, "Description_6", "Due_date_6", "School"]]

def option_choice(option):
    match option:
        case 'A':
            add_task_details()
        case 'C':
            complete_selected()
        case 'DA':
            # Checkbox view
            view_tasks.display_all_tasks()
        case 'DCA':
            # Categorized View
            print(f"This is a list of existing task categories: {task_categories}")
            while True:
                category = input("Please enter a task category: ")

                if category not in task_categories:
                    print("You entered a non-existent category")
                else:
                    break
            view_tasks.display_tasks_by_category(category)
        case 'DCO':
            # Show Completed Tasks
            view_tasks.display_completed_tasks()
        case 'S':
            print("Successfully signed out.")
            print('')
            sign_in_create_account.signed_in = False
            sign_in_create_account.sign_into_account()

def main():
    while True:
        print('Welcome to the homepage')
        print('')
        print('A -- Add Task')
        print('C -- Complete Task')
        print('DA -- Display All Tasks')
        print('DCA -- Display Tasks By Category')
        print('DCO -- Display Completed Tasks')
        print('S -- Sign Out')

        option = str(input('Input: '))

        try:
            option_choice(option)
        except ValueError:
            print("Please Enter Valid Number")