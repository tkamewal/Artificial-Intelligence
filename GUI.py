import datetime
import schedule
import time
from plyer import notification
import tkinter as tk
from tkinter import messagebox
from threading import Thread

tasks_text = None  # Global variable for tasks_text

# Function to send notification and remove completed tasks from the list in GUI
def send_notification_gui(task_list, task):
    for task_info in task_list:
        if not task_info["completed"] and task_info["task"] == task:
            notification.notify(
                title='Reminder',
                message=f"Reminder: {task_info['task']}",
                app_name='To-Do List App',
            )
            task_info["completed"] = True
            messagebox.showinfo("Reminder", f"Reminder sent for task: {task_info['task']}")

# GUI main function
def main_gui():
    global tasks_text  # Declare tasks_text as global variable
    tasks = []  # List to store tasks

    def add_task_gui():
        task = entry_task.get()
        time_str = entry_time.get()

        try:
            reminder_time = datetime.datetime.strptime(time_str, "%H:%M").time()

            # Get current time
            current_time = datetime.datetime.now().time()

            # Calculate time difference between current time and reminder time
            time_diff = datetime.datetime.combine(datetime.date.today(), reminder_time) - datetime.datetime.combine(
                datetime.date.today(), current_time)

            # Schedule the task after the time difference in seconds
            schedule.every(time_diff.seconds).seconds.do(lambda: send_notification_gui(tasks, task))

            messagebox.showinfo("Success", f"Task '{task}' added successfully with reminder at {reminder_time.strftime('%H:%M')}")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")

    def view_tasks_gui():
        tasks_text.delete(1.0, tk.END)
        for index, task_info in enumerate(tasks, start=1):
            task = task_info["task"]
            status = "Completed" if task_info["completed"] else "Pending"
            tasks_text.insert(tk.END, f"{index}. {task} - {status}\n")

    def mark_task_completed_gui():
        try:
            task_index = int(entry_task_index.get()) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                messagebox.showinfo("Success", f"Task '{tasks[task_index]['task']}' marked as completed.")
            else:
                messagebox.showerror("Error", "Invalid task number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid task number.")

    root = tk.Tk()
    root.title("To-Do List App")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label_task = tk.Label(frame, text="Enter Task:")
    label_task.grid(row=0, column=0, sticky="w")
    entry_task = tk.Entry(frame)
    entry_task.grid(row=0, column=1, padx=5, pady=5)

    label_time = tk.Label(frame, text="Enter Time (HH:MM):")
    label_time.grid(row=1, column=0, sticky="w")
    entry_time = tk.Entry(frame)
    entry_time.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(frame, text="Add Task", command=add_task_gui)
    add_button.grid(row=2, column=0, columnspan=2, pady=10)

    tasks_text = tk.Text(frame, height=10, width=40)
    tasks_text.grid(row=3, column=0, columnspan=2, pady=10)

    label_task_index = tk.Label(frame, text="Enter Task Number to Mark as Completed:")
    label_task_index.grid(row=4, column=0, sticky="w")
    entry_task_index = tk.Entry(frame)
    entry_task_index.grid(row=4, column=1, padx=5, pady=5)

    mark_completed_button = tk.Button(frame, text="Mark Task as Completed", command=mark_task_completed_gui)
    mark_completed_button.grid(row=5, column=0, columnspan=2, pady=10)

    view_button = tk.Button(frame, text="View Tasks", command=view_tasks_gui)
    view_button.grid(row=6, column=0, columnspan=2, pady=10)

    root.mainloop()

# Run the GUI main function
if __name__ == "__main__":
    main_gui()
      