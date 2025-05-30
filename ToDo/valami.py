todos = ['Clean','Cooking', 'Shopping']

while True:
    useer_action = input("Type add, show, edit or exit: ")
    useer_action = useer_action.strip()
    match useer_action:
        case 'add':
            todo = input("Enter your value: ")
            todos.append(todo)
        case'show':
            for item in todos:
                item = item.title()
                print(item)
        case'edit':
            new_todo = input("Enter a new task: ")
            for new_todo in todos:
                item = item.title()
                print(item)
        case'exit':
            break



