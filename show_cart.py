from main import *
Cart_File = "cart.json"
def show_cart():
    try:
        with open(Cart_File, "r") as file:
            cart = json.load(file)

        if not cart:
            print(Fore.YELLOW + " Your cart is empty.")
            return

        print(Fore.CYAN + "\n Your Cart:")
        total = 0
        for idx, item in enumerate(cart, start=1):
            print(f"{idx}. {item['name']} ({item['price']} SAR)")
            total += item['price']

        print("-" * 30)
        print(Fore.GREEN + f"Total: {total} SAR")

    except FileNotFoundError:
        print(Fore.YELLOW + " Your cart is empty (no file).")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")
