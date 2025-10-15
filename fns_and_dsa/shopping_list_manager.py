#shoping list mnager 
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
            # Prompt for and add an item
            shopping_list = []
            item = input("Enter the item to add: ")  # exact text
            shopping_list.append(item)

            print(f"{item} has been added to the list.\n")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter Item Name to Delete: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.\n")
            else: print(f"{item} is NOT in the list!")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()