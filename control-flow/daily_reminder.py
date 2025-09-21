task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' is a task"

if time_bound == "yes":
    message = base + " that requires immediate attention today!"
else:
    message = base + " and does not require immediate attention today. Consider completing it when you have free time."

for _ in range(1):
    print("\nReminder:", message)
