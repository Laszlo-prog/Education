class FreeLamceApp:
    def __init__(self, username, role):
        self.username = username
        self.role = role

        
class Job:
    def __init__(self, title, description, client):
        self.client = client
        self.title = title
        self.description = description
        self.job = [ ]

    def apply(self, freelancer):
        print(f"{freelancer.username} applied for the job: {self.title}")

class FreeLanceApp:
    def __init__(self):
        self.users = []
        self.jobs = [ ]
    def register_user(self, username, role):
        user = FreeLamceApp(username, role)
        self.users.append(user)
        print(f"User {username} registered as {role} successfully!")
    
    def post_job(self, title, description, client):
        client = next((user for user in self.users if user.username == client), None)
        if client and client.role == 'client':
            job = Job(title, description, client)
            self.jobs.append(job)
            print(f"Job '{title}' posted successfully by {client.username}.")

        else:
            print("Client not found or not registered ")

    def apply_job(self, title, freelancer_username):
        freelancer = next((user for user in self.users if user.username == freelancer_username and user.role == 'freelancer'), None)
        job = next((job for job in self.jobs if job.title == title), None)

        if freelancer and job:
            job.apply(freelancer)
        else:
            print("Freelancer or Job not found.") 

    def list_jobs(self):
        if not self.jobs:
            print("No jobs available.")
            return
        print("\nAvailable Jobs:")
        for job in self.jobs:
            print(f"Title: {job.title}, Description: {job.description}, Posted by: {job.client.username}")  

    def menu(self):
        while True:
            print("\nFreelance App Menu:")
            print("1. Register User")
            print("2. Post Job")
            print("3. Apply for Job")
            print("4. List Jobs")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter username: ")
                role = input("Enter role (client/freelancer): ").lower()
                self.register_user(username, role)
            elif choice == '2':
                title = input("Enter job title: ")
                description = input("Enter job description: ")
                client = input("Enter your username (client): ")
                self.post_job(title, description, client)
            elif choice == '3':
                title = input("Enter job title to apply for: ")
                freelancer_username = input("Enter your username (freelancer): ")
                self.apply_job(title, freelancer_username)
            elif choice == '4':
                self.list_jobs()
            elif choice == '5':
                print("Exiting Freelance App.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FreeLanceApp()
    app.menu() 


               
