nev = input("Mi a te neved?:")
print("Szia", nev)

if nev == 'Aronn':
    print("Welcome!!")
elif nev == 'Putyin':
    print("Go away!")
else:
    print("Good bye.")



rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("0", end='')
    for j in range(1, rows+1 *2):
        print("0"*j)

    print('\r')

print("--------End------")

rows = 5 
for j in range(1, rows+1):
    print("0" *j)

    