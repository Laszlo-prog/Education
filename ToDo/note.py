def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def add_task(todo_list):
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        todo_list.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added!")
    else:
        print("Task cannot be empty!")

def mark_completed(todo_list):
    view_tasks(todo_list)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print(f"Task '{todo_list[task_number - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(todo_list):
    view_tasks(todo_list)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            deleted_task = todo_list.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def todo_app():
    todo_list = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("\nGoodbye! Have a productive day! 🚀")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")

# Run the To-Do App
todo_app()