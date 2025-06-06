prompt = "\nTell me your account:"
prompt = "\nChoose 'quit' or 'name' go: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    break
if message == 'name':
    print(message)
    for i in range(5):
        break
else:
    print("Goodbye")
