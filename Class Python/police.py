class Cop():
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.arrests = 0
    #Show cop info
    
    def show_info(self):
        print(f"Cop Name: {self.name}, Rank: {self.rank} | Arrests: {self.arrests}")
        #Promote cops
    def promote(self, new_rank):
        self.rank = new_rank
        print("Rank updated")

    #Make an arrest
    def arrest(self, criminal_name):
        self.arrests += 1
        print(f"{self.name} arrested {criminal_name}. Total arrests: {self.arrests}")

#Menu
def menu():
    cops = []
    criminals = []

    while True:
        print("\n1. Add Cop\n2. Show Cops\n3. Promote Cop\n4. Make Arrest\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter cop name: ")
            rank = input("Enter cop rank: ")
            cops.append(Cop(name, rank))
            print("Cop added.")

        elif choice == '2':
            for cop in cops:
                cop.show_info()

        elif choice == '3':
            name = input("Enter cop name to promote: ")
            new_rank = input("Enter new rank: ")
            for cop in cops:
                if cop.name == name:
                    cop.promote(new_rank)
                    break
            else:
                print("Cop not found.")

        elif choice == '4':
            cop_name = input("Enter cop name: ")
            criminal_name = input("Enter criminal name: ")
            for cop in cops:
                if cop.name == cop_name:
                    cop.arrest(criminal_name)
                    criminals.append(criminal_name)
                    break
            else:
                print("Cop not found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()






    
