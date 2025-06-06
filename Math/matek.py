tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- ToDo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            if tasks:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
        elif choice == '4':
            print("Thank you for using the ToDo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()