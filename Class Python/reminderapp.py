import time

class ReminderApp:
    def __init__(self):
        self.reminders = []

    def add_reminder(self):
        reminder_text = input("Enter your reminder: ")
        reminder_time = input("Enter time for reminder (HH:MM): ")
        self.reminders.append((reminder_text, reminder_time))
        print("Reminder added successfully!")

    def view_reminders(self):
        if not self.reminders:
            print("No reminders set.")
            return
        print("\nReminders:")
        for idx, (text, time) in enumerate(self.reminders, start=1):
            print(f"{idx}. {text} at {time}")

    def delete_reminder(self):
        self.view_reminders()
        if not self.reminders:
            return
        try:
            index = int(input("Enter the number of the reminder to delete: ")) - 1
            if 0 <= index < len(self.reminders):
                removed = self.reminders.pop(index)
                print(f"Removed reminder: {removed[0]} at {removed[1]}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    def menu(self):
        while True:
            print("\nReminder App Menu:")
            print("1. Add Reminder")
            print("2. View Reminders")
            print("3. Delete Reminder")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_reminder()
            elif choice == '2':
                self.view_reminders()
            elif choice == '3':
                self.delete_reminder()
            elif choice == '4':
                print("Exiting Reminder App.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ReminderApp()
    app.menu()
