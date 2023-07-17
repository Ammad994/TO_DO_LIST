# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        # Mark the task as completed
        self.completed = True

    def mark_as_incomplete(self):
        # Mark the task as incomplete
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        # Create a new Task object and add it to the list of tasks
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            # Remove the task at the specified index from the list
            del self.tasks[index]

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            # Mark the task at the specified index as completed
            self.tasks[index].mark_as_completed()

    def mark_task_as_incomplete(self, index):
        if 0 <= index < len(self.tasks):
            # Mark the task at the specified index as incomplete
            self.tasks[index].mark_as_incomplete()

    def edit_task_description(self, index, new_description):
        if 0 <= index < len(self.tasks):
            # Update the description of the task at the specified index
            self.tasks[index].description = new_description

    def sort_tasks(self, key):
        if key == 'status':
            # Sort tasks based on completion status (completed tasks first)
            self.tasks.sort(key=lambda x: x.completed)
        elif key == 'description':
            # Sort tasks based on description (alphabetical order)
            self.tasks.sort(key=lambda x: x.description.lower())

    def clear_all_tasks(self):
        # Clear all tasks from the todo list
        self.tasks = []

    def save(self, filename):
        # Save tasks to a file
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task.description + '\n')

    def load(self, filename):
        self.tasks = []
        try:
            # Load tasks from a file
            with open(filename, 'r') as file:
                for line in file:
                    description = line.strip()
                    task = Task(description)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

class TodoListGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Todo List Manager")

        self.todo_list = TodoList()
        self.todo_list.load('todo.txt')

        # Create the task listbox
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(padx=10, pady=10)

        # Create the add task frame and widgets
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(padx=10, pady=5)
        self.add_entry = tk.Entry(self.add_frame, width=50)
        self.add_entry.pack(side=tk.LEFT)
        self.add_button = tk.Button(self.add_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Create the remove task button
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        # Create the mark complete button
        self.mark_complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_task_as_completed)
        self.mark_complete_button.pack(pady=5)

        # Create the mark incomplete button
        self.mark_incomplete_button = tk.Button(self.root, text="Mark Incomplete", command=self.mark_task_as_incomplete)
        self.mark_incomplete_button.pack(pady=5)

        # Create the edit task frame and widgets
        self.edit_frame = tk.Frame(self.root)
        self.edit_frame.pack(padx=10, pady=5)
        self.edit_entry = tk.Entry(self.edit_frame, width=50)
        self.edit_entry.pack(side=tk.LEFT)
        self.edit_button = tk.Button(self.edit_frame, text="Edit Task", command=self.edit_task_description)
        self.edit_button.pack(side=tk.LEFT)

        # Create the sort task frame and widgets
        self.sort_frame = tk.Frame(self.root)
        self.sort_frame.pack(padx=10, pady=5)
        self.sort_label = tk.Label(self.sort_frame, text="Sort by:")
        self.sort_label.pack(side=tk.LEFT)
        self.sort_option = tk.StringVar()
        self.sort_option.set("status")
        self.sort_dropdown = tk.OptionMenu(self.sort_frame, self.sort_option, "status", "description")
        self.sort_dropdown.pack(side=tk.LEFT)
        self.sort_button = tk.Button(self.sort_frame, text="Sort Tasks", command=self.sort_tasks)
        self.sort_button.pack(side=tk.LEFT)

        # Create the clear all tasks button
        self.clear_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_button.pack(pady=5)

        # Create the save tasks button
        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        # Set the close event handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Refresh the task listbox
        self.refresh_task_listbox()

    def add_task(self):
        # Get the task description from the entry widget
        task_description = self.add_entry.get()
        if task_description:
            # Add the task to the todo list
            self.todo_list.add_task(task_description)
            # Refresh the task listbox
            self.refresh_task_listbox()
            # Clear the entry widget
            self.add_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task description.")

    def remove_task(self):
        # Get the selected task index from the listbox
        selected_index = self.task_listbox.curselection()
        if selected_index:
            # Remove the task from the todo list
            self.todo_list.remove_task(selected_index[0])
            # Refresh the task listbox
            self.refresh_task_listbox()
        else:
            messagebox.showerror("Error", "Please select a task to remove.")

    def mark_task_as_completed(self):
        # Get the selected task index from the listbox
        selected_index = self.task_listbox.curselection()
        if selected_index:
            # Mark the task as completed
            self.todo_list.mark_task_as_completed(selected_index[0])
            # Refresh the task listbox
            self.refresh_task_listbox()
        else:
            messagebox.showerror("Error", "Please select a task to mark as completed.")

    def mark_task_as_incomplete(self):
        # Get the selected task index from the listbox
        selected_index = self.task_listbox.curselection()
        if selected_index:
            # Mark the task as incomplete
            self.todo_list.mark_task_as_incomplete(selected_index[0])
            # Refresh the task listbox
            self.refresh_task_listbox()
        else:
            messagebox.showerror("Error", "Please select a task to mark as incomplete.")

    def edit_task_description(self):
        # Getthe selected task index from the listbox
        selected_index = self.task_listbox.curselection()
        # Get the new description from the entry widget
        new_description = self.edit_entry.get()
        if selected_index and new_description:
            # Edit the task description
            self.todo_list.edit_task_description(selected_index[0], new_description)
            # Refresh the task listbox
            self.refresh_task_listbox()
            # Clear the entry widget
            self.edit_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please select a task and enter a new description.")

    def sort_tasks(self):
        # Get the selected sort option from the dropdown menu
        sort_key = self.sort_option.get()
        # Sort the tasks based on the selected sort key
        self.todo_list.sort_tasks(sort_key)
        # Refresh the task listbox
        self.refresh_task_listbox()

    def clear_all_tasks(self):
        # Display a confirmation dialog
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirm:
            # Clear all tasks from the todo list
            self.todo_list.clear_all_tasks()
            # Refresh the task listbox
            self.refresh_task_listbox()

    def save_tasks(self):
        # Save tasks to a file
        self.todo_list.save('todo.txt')
        messagebox.showinfo("Information", "Tasks saved successfully.")

    def refresh_task_listbox(self):
        # Clear the task listbox
        self.task_listbox.delete(0, tk.END)
        # Add tasks to the task listbox
        for task in self.todo_list.tasks:
            status = "[X]" if task.completed else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task.description}")

    def on_close(self):
        # Display a confirmation dialog
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
        if confirm:
            # Save tasks before closing the application
            self.todo_list.save('todo.txt')
            # Close the GUI window
            self.root.destroy()

    def run(self):
        # Run the main event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the TodoListGUI class
    todo_list_gui = TodoListGUI()
    # Run the GUI application
    todo_list_gui.run()