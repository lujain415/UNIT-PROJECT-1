import json
from colorama import *

def enter_address():
    address = input(Fore.CYAN + "Enter your delivery address: ")
    with open("address.json", "w") as f:
        json.dump({"address": address}, f)
    print(Fore.GREEN + "Address saved successfully.")