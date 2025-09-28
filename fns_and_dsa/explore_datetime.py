from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    Saves the current datetime in a variable named `current_date`.
    """
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date 

def calculate_future_date(days_to_add):
    """
    Calculate and print the date after adding `days_to_add` days to today.
    Saves the result in a variable named `future_date`, then prints it as 'YYYY-MM-DD'.
    """
    future_date = (datetime.now() + timedelta(days=days_to_add))
    print(future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    display_current_datetime()

    while True:
        user_input = input("Enter the number of days to add: ")
        try:
            days = int(user_input)
            break
        except ValueError:
            print("Please enter an integer (e.g., 7).")

    calculate_future_date(days)

if __name__ == "__main__":
    main()
