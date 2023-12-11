from menu import MENU
from resources import resources

revenue = 0.0
choice = ""


def make_drink(_choice_):
    """
    Serves the drink
    Decrements the resources per ingredient used for the drink

    :param _choice_: user's menu choice
    :return: None
    """
    drink_ingredients = MENU[_choice_]["ingredients"]
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {_choice_}. Enjoy!")


def pay_amount(_choice_):
    """
    Takes the amount from the user in Quarters, Dimes, Nickels and Pennies
    Checks if the amount is equal to the choice price
    if the amount is less than the price of the chosen drink it aborts
    if the amount is more it returns change
    Adds the amount to revenue
    Calls make_drink function

    :param _choice_: user's menu choice
    :return: None
    """
    drink_price = MENU[_choice_]["cost"]

    print("Please Enter the amount.")
    quarters = input("Enter Quarters: ")
    dimes = input("Enter Dimes: ")
    nickels = input("Enter Nickels: ")
    pennies = input("Enter Pennies: ")

    fees = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * 0.01

    if fees < drink_price:
        print("Sorry that is not enough money , Money Refunded!")
        return

    if fees > drink_price:
        print(f"Here is your change: ${fees - float(drink_price)}")

    global revenue
    revenue += drink_price
    return make_drink(_choice_)


def check_drink_availability(_choice_):
    """
    Checks first if the drink ordered by the user is in the menu
    if found it checks if there is enough resources to make that drink
    returns boolean value

    :param _choice_: user's menu choice
    :return: boolean
    """
    if MENU.get(_choice_) is None:
        print("Sorry we don't serve this drink...")
        return False

    drink_ingredients = MENU[_choice_]["ingredients"]
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def display_resources():
    """
    Displays the resources of the program and the money made

    :return: None
    """
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money: {revenue}")


def display_menu():
    """
    Displays the menu of the program and take she input from the user in lower case format

    :return: input string from the user
    """
    print("Menu: ")
    for drink in MENU:
        print(f"\t{drink} ${MENU[drink]['cost']}")
    return input("What would you like?\n").lower()


while True:
    choice = display_menu()
    if choice == "off":
        break

    if choice == "report":
        display_resources()
    elif check_drink_availability(choice):
        pay_amount(choice)

print("Turning OFF...")
