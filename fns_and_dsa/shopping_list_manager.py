def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f'"{item}" added.')
            else:
                print("No item entered. Nothing added.")

        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed.')
            else:
                print(f'"{item}" not found in the list.')

        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Current Shopping List:")
                for i, it in enumerate(shopping_list, start=1):
                    print(f"{i}. {it}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
