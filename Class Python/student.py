


class Student:
    def __init__(self, name, house, patronus):

        self.name = name
        self.house = house
        self.patronus = patronus
        

    def __str__(self):
       return f"{self.name} from {self.house} use {self.patronus}"
    
    def charm(self):
        if self.patronus == "Stag":
            return"horse"
        elif self.patronus == "otter":
            return"shoes"
        else:
            return"bye"
        
    def main(self):
        student = "students"
        print("Expect Patronus")
        print(student.charm())

    def students(name, house, patronus):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return Student(name, house, patronus)
    
    if __name__ == "__main__": 
       main()
       #charm()
       #students()

        
          