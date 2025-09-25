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
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            while True:
                add_item = input("Enter item to add: ")
                if add_item == "exit":
                    break
                else:
                    shopping_list.append(add_item)
                    pass
        elif choice == 2:
            while True:
                remove_item = input("Enter item to remove(type 'exit' to return to main menu): ") 
                if remove_item == "exit":
                    break
                elif remove_item not in shopping_list:
                    print(f"{remove_item} is not in shopping list")
                else: 
                    shopping_list.remove(remove_item)
            pass
        elif choice == 3:
            i = 0
            for items in shopping_list:
                i += 1
                print(f"{i}. {items}")
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
                  