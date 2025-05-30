
import os

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.txt"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = [line.strip().split("|") for line in f.readlines()]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task[0]}|{task[1]}\n")

    def add_task(self, task):
        self.tasks.append([task, "Incomplete"])
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task[0]} - {task[1]}")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1][1] = "Complete"
            self.save_tasks()
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n--- To-Do List App ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Quit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                task_index = int(input("Enter the task number to mark as complete: "))
                self.mark_complete(task_index)
            elif choice == "4":
                print("Thank you for using the To-Do List App!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()