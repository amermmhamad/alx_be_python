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
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
                print(f'"{item}" added.')
            else:
                print("No item entered. Nothing added.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed.')
            else:
                print(f'"{item}" not found in the list.')

        elif choice == '3':
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
