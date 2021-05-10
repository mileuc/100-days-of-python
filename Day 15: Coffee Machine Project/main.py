MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def user_prompt():
    """Prompt user for their choice of coffee and return this choice. If report is entered, print the
    current resource supply of the coffee machine."""
    valid_response = False
    while not valid_response:
        choice = input("Hello! What would you like today? (espresso/latte/cappuccino): ").lower()
        if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "off":
            return choice
        elif choice == "report":
            # TODO: 3. Print report of all coffee machine resources if "report" is entered
            print_resources()
        else:
            print("Invalid response.")


def check_for_off_command(command):
    """Check if off command was entered. If so, return False with the intention of turning off the
    machine."""
    if command == "off":
        print("Coffee machine turned off.")
        return False
    else:
        return True


def print_resources():
    """Print current resources inside the coffee machine."""
    print("Current resource values:")
    for resource in resources:
        amount = resources[resource]
        resource_name = resource.capitalize()
        if resource == "water" or resource == "milk":
            units = "ml"
            print(f"{resource_name}: {amount}{units}")
        elif resource == "coffee":
            units = "g"
            print(f"{resource_name}: {amount}{units}")
        else:
            print(f"{resource_name}: ${'{:.2f}'.format(round(amount, 2))}")


def check_resources(choice):
    """Return True and subtract resources if machine resources are sufficient for choice of coffee.
    Return False otherwise."""
    required_ingredients = MENU[choice]["ingredients"]

    for ingredient in required_ingredients:
        if resources[ingredient] >= required_ingredients[ingredient]:
            resources[ingredient] -= required_ingredients[ingredient]
        else:
            print(f"Sorry, there's not enough {ingredient} in the machine.")
            return False

    return True


def take_coins(choice):
    """Prompt the user to enter payment and return True if money is sufficient, return False otherwise.
    If payment is sufficient, add money to the machine resources and return any change."""
    coin_amounts = []
    coin_values = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
    price = MENU[choice]["cost"]

    print("Please insert coins.")
    for coin in coin_values:
        valid_response = False
        while not valid_response:
            num_of_coins = input(f"How many {coin}?: ")
            if not check_for_off_command(num_of_coins):
                return False
            else:
                try:
                    coin_amount = int(num_of_coins) * coin_values[coin]
                    coin_amounts.append(coin_amount)
                    valid_response = True
                except ValueError:
                    print("Invalid response")

    total_amount = sum(coin_amounts)

    if total_amount >= price:
        print(f"Your total is ${'{:.2f}'.format(round(price, 2))}.")
        change = total_amount - price
        print(f"Here is ${'{:.2f}'.format(round(change, 2))} of change.")
        resources["money"] += float('{:.2f}'.format(round(price, 2)))
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


coffee_machine_on = True
while coffee_machine_on:
    # TODO: 1. Prompt user by asking what would they like
    coffee_choice = user_prompt()
    # TODO: 2. Check if the off command was entered
    coffee_machine_on = check_for_off_command(coffee_choice)

    if coffee_machine_on:
        # TODO: 4. Check if there are sufficient resources to make the coffee. If so, make the coffee
        is_resource_sufficient = check_resources(coffee_choice)
        if is_resource_sufficient:
            # TODO: 5. Process coins and check if the transaction is successful
            coffee_machine_on = take_coins(coffee_choice)
            print(f"Here is your {coffee_choice}☕. Enjoy!")
        else:
            coffee_machine_on = False
    else:
        coffee_machine_on = False



