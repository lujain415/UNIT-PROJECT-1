
from main import *
Cart_File = "cart.json"

def add_to_cart(item_number_str):
    try:
        index = int(item_number_str) - 1
        with open(Menu_File, "r") as file:
            menu = json.load(file)

        if index < 0 or index >= len(menu):
            print(Fore.RED + " Invalid menu number.")
            return

        found_item = menu[index]

        if found_item['quantity'] <= 0:
            print(Fore.YELLOW + "Sorry, this item is out of stock.")
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

        print(Fore.GREEN + f"✅ {found_item['name']} added to your cart.")

    except ValueError:
        print(Fore.RED + " Please enter a valid number.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")