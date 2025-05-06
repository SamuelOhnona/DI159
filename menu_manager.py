# menu_manager.py

import psycopg2
from menu_item import MenuItem

# This class provides methods to query the menu items
class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        # Returns a MenuItem object if the item exists in the database
        try:
            connection = psycopg2.connect(
                dbname="restaurant_db", user="your_username", password="your_password", host="localhost"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
            result = cursor.fetchone()
            if result:
                return MenuItem(result[0], result[1])
            else:
                return None
        except Exception as e:
            print("Error retrieving item:", e)
            return None
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def all_items(cls):
        # Returns a list of all MenuItem objects in the database
        try:
            connection = psycopg2.connect(
                dbname="restaurant_db", user="your_username", password="your_password", host="localhost"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items")
            results = cursor.fetchall()
            return [MenuItem(name, price) for name, price in results]
        except Exception as e:
            print("Error retrieving all items:", e)
            return []
        finally:
            cursor.close()
            connection.close()