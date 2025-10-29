#Create job post pyApp for large public

class JobApp:
    #Initialize the JobApp class details

    def __init__(self, title, company, location):
        self.title = title
        self.company = company
        self.location = location
        
    #return job info as string

    def __str__(self):
        return f"Job Title: {self.title}, Company: {self.company}, Location: {self.location}"
    
class JobBoard:
    def __init__(self):
        self.jobs = [ ]

#Add job to list
    def add_job(self, job):
        self.jobs.append(job)
#list all jobs
    def list_jobs(self):
        if not self.jobs:
            print("No jobs available.")
        else:

           for i, job in enumerate(self.jobs, 1):
              print(f"{i}. {job}")
 #remove job from list
    def remove_job(self, index):
        if 0 <= index < len(self.jobs):
            removed_job = self.jobs.pop(index)
            print(f"Removed: {removed_job}")
        else:
            print("Invalid job index.")
#Show menu for interaction
def main():
    board = JobBoard()
    while True:
        print("\nJob Board Menu:")
        print("1. Add Job")
        print("2. List Jobs")
        print("3. Remove Job")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter job title: ")
            company = input("Enter company name: ")
            location = input("Enter job location: ")
            job = JobApp(title, company, location)
            board.add_job(job)
            print("Job added successfully.")

        elif choice == '2':
            board.list_jobs()

        elif choice == '3':
            index = int(input("Enter job index to remove: ")) - 1
            board.remove_job(index)

        elif choice == '4':
            print("Exiting Job Board.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
    





