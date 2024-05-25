import datetime
import schedule
import time
from plyer import notification
from threading import Thread

# Function to display the menu
def display_menu():
    print(" ")
    print("List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

# Function to add a task and set a reminder time
def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append({"task": task, "completed": False})
    time_str = input("Enter Reminder Time (in HH:MM format): ")

    try:
        reminder_time = datetime.datetime.strptime(time_str, "%H:%M").time()

        # Get current time
        current_time = datetime.datetime.now().time()

        # Calculate time difference between current time and reminder time
        time_diff = datetime.datetime.combine(datetime.date.today(), reminder_time) - datetime.datetime.combine(datetime.date.today(), current_time)

        # Schedule the task after the time difference in seconds
        schedule.every(time_diff.seconds).seconds.do(send_notification, task_list)

        print("Task added successfully with reminder at", reminder_time.strftime("%H:%M"))
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Function to view tasks in the list
def view_tasks(task_list):
    print("Tasks in the To-Do List:")
    for index, task_info in enumerate(task_list, start=1):
        task = task_info["task"]
        status = "Completed" if task_info["completed"] else "Pending"
        print(f"{index}. {task} - {status}")

# Function to mark a task as completed
def mark_task_completed(task_list):
    view_tasks(task_list)
    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index]["completed"] = True
            print(f"Task '{task_list[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to send notification and remove completed tasks from the list
def send_notification(task_list):
    for task_info in task_list:
        if not task_info["completed"]:
            notification.notify(
                title='Reminder',
                message=f"Reminder: {task_info['task']}",
                app_name='To-Do List App',
            )
            task_info["completed"] = True
            print(f"Reminder sent for task: {task_info['task']}")
    # Remove completed tasks from the list
    task_list[:] = [task_info for task_info in task_list if not task_info["completed"]]

# Scheduler function
def scheduler(task_list):
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function
def main():
    tasks = []  # List to store tasks

    # Start the scheduler
    scheduler_thread = Thread(target=scheduler, args=(tasks,))
    scheduler_thread.start()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()