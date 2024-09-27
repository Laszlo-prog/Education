print("========Welcome=======")
print("=======Let's goo to RACE========")



benzina = 10
nume = 'Laszlo'

while benzina > 0:
    print(f'Go race {nume}')
    benzina = benzina -1
    print(f'ai putina combustibil {benzina}')
    if benzina < 3:
        print(f'Se aprinde becul rosul {nume}')
        if benzina < 1:
            print(f'ATENTIE!!! {nume}')


print(f"Numai ai benzina {benzina}")
name = input("Enter your name: ")

if name == 'Ashe':
    print(f'You are the winner ...{name}')
elif name == 'Ketchump':
    print(f"Are you welcome..{name}")
else:
    print(f'You are not welcom!!{name}')
