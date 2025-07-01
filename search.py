import json
from colorama import *
from main import *
Menu_File = "menu.json"

def search_products():
    keyword = input(Fore.YELLOW + "Enter a product name to search: ").lower()

    try:
        with open(Menu_File, "r") as file:
            menu = json.load(file)

        found = False
        for item in menu:
            if keyword == item['name'].lower():
                found = True
                print(Fore.GREEN + f" Found: {item['name']} - {item['price']} SAR")
                print(f"   {item['description']} - Available: {item['quantity']}")
                
                break

        if not found:
            print(Fore.RED + "Product not found.")

    except Exception as e:
        print(Fore.RED + f" Error: {e}")
