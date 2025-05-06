# menu_item.py

import psycopg2

# This class represents a menu item in the database
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        # Inserts the item into the database
        try:
            connection = psycopg2.connect(
                dbname="restaurant_db", user="your_username", password="your_password", host="localhost"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                (self.name, self.price),
            )
            connection.commit()
            print("Item saved successfully.")
        except Exception as e:
            print("Error saving item:", e)
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        # Deletes the item from the database
        try:
            connection = psycopg2.connect(
                dbname="restaurant_db", user="your_username", password="your_password", host="localhost"
            )
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM Menu_Items WHERE item_name = %s", (self.name,)
            )
            if cursor.rowcount == 0:
                print("Item not found.")
            else:
                connection.commit()
                print("Item deleted successfully.")
        except Exception as e:
            print("Error deleting item:", e)
        finally:
            cursor.close()
            connection.close()

    def update(self, new_name, new_price):
        # Updates the name and price of an item
        try:
            connection = psycopg2.connect(
                dbname="restaurant_db", user="your_username", password="your_password", host="localhost"
            )
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                (new_name, new_price, self.name)
            )
            if cursor.rowcount == 0:
                print("Item not found.")
            else:
                connection.commit()
                print("Item updated successfully.")
        except Exception as e:
            print("Error updating item:", e)
        finally:
            cursor.close()
            connection.close()