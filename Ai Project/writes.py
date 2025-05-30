import os
import time
file_name = input("Enter thev filename to create: - ")

# Step number one
print(file_name)

def write_to_file(file_name):
    if os.path.exist(file_name):
        print(f"Error: {file_name} already exist.")
    else:
        with open(file_name, "a" )as F:
            while True:
                text = input("Enter any text: ")
                F.write(f"{text} \n")

                if input("Do you  want enter more, y/n: ").lower() == "n":
                    break
#Step number 2:

def check_first_letter():
    with open(file_name) as F:
        lines = F.read().split()
        #stor all starting letters from each line in one string.
        first_letters = "".join([line[0].lower() for line in lines ])
        count_i =first_letters.count("i")
        count_m = first_letters.count("m")


        print(f"The total number of sentence starting with I or M are {count_i + count_m} ")

if __name__ =="__main__":
    write_to_file(file_name)
    time.sleep(1)
    check_first_letter()
    