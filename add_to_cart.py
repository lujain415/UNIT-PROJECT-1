import json
from colorama import *

Menu_File = "menu.json"
Cart_File = "cart.json"

def add_to_cart_by_name(item_name):
    try:
        with open(Menu_File, "r") as file:
            menu = json.load(file)

        matched = None
        for idx, item in enumerate(menu):
            if item_name.lower() == item['name'].lower():
                matched = (idx, item)
                break

        if not matched:
            print(Fore.RED + "Product not found. Please check the name.")
            return

        index, found_item = matched

        if found_item['quantity'] <= 0:
            print(Fore.BLUE + "Sorry, this item is out of stock.")
            return

        try:
            with open(Cart_File, "r") as f:
                cart = json.load(f)
        except FileNotFoundError:
            cart = []

        cart.append({
            "name": found_item['name'],
            "price": found_item['price']
        })

        with open(Cart_File, "w") as f:
            json.dump(cart, f, indent=4)

        
        menu[index]['quantity'] -= 1
        with open(Menu_File, "w") as f:
            json.dump(menu, f, indent=4)

        print(Fore.GREEN + f"{found_item['name']} added to your cart.")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
