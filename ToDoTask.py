import schedule
import time
from plyer import notification
def display_menu():
    print(" ")
    print("List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("4. Exit")
    


def add_task(task, task_list):
    task_list.append(task)
    
    times=input("Enter Remainder Time: ")
   
    print("Task added successfully!")
    
    print(" ")
    send_notification()

def view_tasks(task_list):
   
    print("Tasks in the To-Do List:")
    
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")


def mark_task_as_done(task_list):
    view_tasks(task_list)
   
    task_number = int(input("Enter the task number to mark as done: "))
    
    if 1 <= task_number <= len(task_list):
        del task_list[task_number - 1]
        print("Task marked as done successfully!")
       
    else:
        print("Invalid task number.")
        


def main():
    tasks = []  # List to store tasks

    while True:
        display_menu()
        print(" ")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
           
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
         
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

def send_notification():
    notification.notify(
        title='Reminder',
        message='Do your work now!',
        app_name='My App',
    )
schedule.every().day.at(times).do(send_notification)

while True:
    schedule.run_pending()
    time.sleep(1)


