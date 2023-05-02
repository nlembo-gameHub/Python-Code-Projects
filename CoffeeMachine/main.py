
# TODO: 1. Set up Menu variable
# Importing Libraries
from menu import MENU, RESOURCES, PROFIT
# Setting menu = Menu from the meny.py library
menu = MENU.copy()
resources = RESOURCES.copy()
profit = PROFIT.copy()


# Ensure there is no error when user does not input an int
def num_input_check(coin_type):
    """Returns the inputted number requested from the user"""
    while True:
        try:
            num = int(input(f"how many {coin_type}?: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    return num

# TODO: 4. Check if resources are sufficient
# Compare Machine's Resources to coffee requirements
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins
# Process the coins being spent
def process_coins_spent():
    """Returns the total value of coins spent"""
    print("Please insert coins.")
    total = num_input_check("quarters") * 0.25
    total += num_input_check("dimes") * 0.10
    total += num_input_check("nickles") * 0.05
    total += num_input_check("pennies") * 0.01
    return total


# TODO: 6. Check if the transaction was successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


# TODO: 7. Make the ordered coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# TODO: 2. Print report all coffee machine resources.
# Creating the flag to turn the machine on or off
machine_on = True
# Loop that runs through the code logic
while machine_on:
    correct_item = False
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Check to make sure user inputs an item
    for item in menu:
        if choice == item:
            correct_item = True

    # User chooses to turn machine off, or user wishes to check machine resources
    if choice == "off":
        machine_on = False
    elif choice == "report":
        # TODO: 3. Print out a report of the machine's current resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill":
        print("Refilling machine...refilled ☕!")
        resources = RESOURCES.copy()

    # If correct items has been selected, continue with order process
    if correct_item:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins_spent()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice.capitalize(), drink["ingredients"])

