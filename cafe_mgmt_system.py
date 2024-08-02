add_item(item_id, name, price)
        elif choice == 2:
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
        elif choice == 3:
            item_id = int(input("Enter item ID to update price: "))
            new_price = float(input("Enter new price: "))
            update_price(item_id, new_price)
        elif choice == 4:
            view_menu()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    print("Welcome to AARR Cafe!")
    role = input("Are you an Admin or a Customer? ").strip().lower()
    if role == "admin":
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            admin_tasks()
        else:
            print("Incorrect password. Access denied.")
    elif role == "customer":
        view_menu()
        place_order()
    else:
        print("Invalid role. Please enter 'Admin' or 'Customer'.")

# Run the main function
if _name_ == "_main_":
    main()
