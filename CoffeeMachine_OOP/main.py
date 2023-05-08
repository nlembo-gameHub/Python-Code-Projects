# Modules & Libraries
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating Object variables from classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Creating a copy of the CoffeeMaker's resource dictionary
resources_copy = coffee_maker.resources.copy()

# Bool/Flag variable to keep machine on
is_on = True


# Function that checks if the order is an option
def is_option(_order):
    options = menu.menu
    for item in options:
        if _order == item.name:
            print("Found the order")
            return True
    return False


# Setting up the while loop to continue process
while is_on:
    # Prompting User
    menu_options = menu.get_items()
    order = input(f"Welcome to Nathan's Cafe. Our items on the menu are {menu_options}. Please pick one: ").lower()
    # Checking User Input Options
    if order == "off":
        is_on = False
        print("Thanks for Ordering with us. the coffee machines are off and the store is closed!")
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "refill":
        coffee_maker.refill_machine(resources_copy)
    else:
        drink = menu.find_drink(order)
        # Check to see if the order is indeed an option
        if is_option(order):
            print(f"Your {drink.name} will cost ${drink.cost}.")
            if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
                print(f"You've paid a total of ${money_machine.money_received}.")
                coffee_maker.make_coffee(drink)
