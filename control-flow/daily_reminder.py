# daily_reminder.py

while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    print()  # Add a blank line for readability

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be addressed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Plan to work on it soon.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that still needs to be done today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")

    print()  # Add spacing between reminders
    again = input("Would you like to enter another task? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
