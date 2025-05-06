# menu_editor.py

from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Restaurant Menu Manager ---")
        print("V: View an Item")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("S: Show Full Menu")
        print("E: Exit")
        choice = input("Enter your choice: ").upper()

        if choice == "V":
            name = input("Enter item name to view: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name} - {item.price}€")
            else:
                print("Item not found.")

        elif choice == "A":
            add_item_to_menu()

        elif choice == "D":
            remove_item_from_menu()

        elif choice == "U":
            update_item_from_menu()

        elif choice == "S":
            show_restaurant_menu()

        elif choice == "E":
            print("\nFinal restaurant menu:")
            show_restaurant_menu()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    name = input("Enter the name of the new item: ")
    try:
        price = int(input("Enter the price of the new item: "))
        item = MenuItem(name, price)
        item.save()
    except ValueError:
        print("Invalid price. Please enter a number.")

def remove_item_from_menu():
    name = input("Enter the name of the item to delete: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
    else:
        print("Item not found. Deletion failed.")

def update_item_from_menu():
    old_name = input("Enter the current name of the item: ")
    item = MenuManager.get_by_name(old_name)
    if item:
        new_name = input("Enter the new name: ")
        try:
            new_price = int(input("Enter the new price: "))
            item.update(new_name, new_price)
        except ValueError:
            print("Invalid price. Update failed.")
    else:
        print("Item not found. Update failed.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"{item.name} - {item.price}€")
    else:
        print("Menu is empty.")