import json
from colorama import *
import add_to_cart,show_cart,checkout,search,address,delivery
from art import *

init(autoreset=True)

Menu_File = "menu.json"
Cart_File = "cart.json"

def print_colored_box(text, fg_color=Fore.WHITE, bg_color=Back.BLUE, width=60):
    print(bg_color + " " * width + Style.RESET_ALL)  
    for line in text.split("\n"):
        
        print(bg_color + fg_color + line.center(width) + Style.RESET_ALL)
    print(bg_color + " " * width + Style.RESET_ALL) 
def main():
   
    title_art = text2art("Restaurant", font="isometric1")
    print_colored_box(title_art, fg_color=Fore.RED, bg_color=Back.YELLOW,width=155)

    welcome_text ="Welcome to the Restaurant!"
    print_colored_box(welcome_text, fg_color=Fore.BLACK, bg_color=Back.RED, width=155)

    while True:
        user = input(Fore.YELLOW  + """
Choose an option:
                     
1- List menu
                     
2- Add item 
                     
3- Show cart
                     
4- Checkout
                     
5- Search
                     
6- Enter address
                     
7- Check delivery status
                                         
8- Exit
                     
Your choice: """ + Style.RESET_ALL).lower().strip()

        if user == "1":
            list_menu()
        elif user == "2":
           item_name = input(Fore.CYAN + "Enter the name of the item you want to add: ").strip()
           add_to_cart.add_to_cart_by_name(item_name)

        elif user == "3":
            show_cart.show_cart()
        elif user == "4":
            checkout.checkout()
        elif user == "5":
            search.search_products()

        elif user == "6":
            import address
            address.enter_address()
        elif user == "7":
          import delivery
          delivery.check_status()
        elif user == "8":
            print(Fore.MAGENTA + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")

def list_menu():
    try:
        with open(Menu_File, "r") as file:
            menu = json.load(file)
            print(Fore.CYAN + "MENU")
            for idx, item in enumerate(menu, start=1):
                print(f"{idx}. {item['name']} - {item['price']} SAR")
                print(f"   {item['description']} - Available {item['quantity']}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")+print_colored_box( fg_color=Fore.BLACK, bg_color=Back.YELLOW, width=155)


main()
