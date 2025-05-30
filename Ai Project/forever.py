print("=======Welcome=======")
print("=======Let's play======")

benzina = 10
nume = 'Laszlo'
while benzina > 0:
    print(f'Go attack {nume}')
    benzina = benzina -1
    print(f'Ai putina combustibil{benzina}')
    if benzina < 3:
        print(f'Se aprinde becul rosu {nume}')
        if benzina < 1:
            print(f'Warning!!!! {nume}')
print(f"Numai ai combustibil{ benzina}")
name = input("Enter your name: ")
if name == 'Balint':
    print(f'You are the winner ...{name}')
elif name == 'Foro':
    print(f'You are welcome!! {name}')
else:
    print(f'You are not welcome {name}')


