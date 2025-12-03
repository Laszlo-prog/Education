def techno(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end='')
        print('')

def mega_stars(rows):
    for j in range(1, rows + 1):
        print("*" * j)

def quick_stars(rows):
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end='')
        print('')

def main():
    while True:
        print("1. Print Stars\n2. Mega stars\n3. Quick Stars\n4. Exit")
    

        choose = input("Enter number of menu: ")
        if choose == '1':
            rows = int(input("Enter number of rows: "))
            techno(rows)
        elif choose == '2':
            rows = int(input("Enter number of rows: "))
            mega_stars(rows)
        elif choose == '3':
            rows = int(input("Enter number of rows: "))
            quick_stars(rows)
        elif choose == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
