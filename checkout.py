import json
from colorama import *
Cart_File = "cart.json"

def checkout():
    try:
        with open(Cart_File, "r") as file:
            cart = json.load(file)

        if not cart:
            print(Fore.BLUE + " Your cart is empty. Nothing to checkout.")
            return

        print(Fore.CYAN + "\n Checkout Receipt:")
        total = 0
        for item in cart:
            print(f"- {item['name']} ({item['price']} SAR)")
            total += item['price']

        print("-" * 30)
        print(Fore.GREEN + f"Total: {total} SAR")
        print(Fore.MAGENTA + "Thank you for your order!")

        with open(Cart_File, "w") as file:
            json.dump([], file)

    except FileNotFoundError:
        print(Fore.BLUE + " Your cart is empty (no file).")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")