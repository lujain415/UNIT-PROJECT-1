import json
from colorama import *

def check_status():
   try:
        with open("address.json", "r") as f:
            data = json.load(f)
            print(Fore.GREEN + f"Delivery to: {data['address']}")
            print(Fore.GREEN + "Status: In progress")
   except FileNotFoundError:
        print(Fore.RED + "No order found.")

