from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
is_on = True

while is_on:
    valid_response = False
    # prompt user for choice of item
    while not valid_response:
        coffee_choice = input(f"Hello! What would you like today? {my_menu.get_items()}: ").lower()
        if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
            ordered_item = my_menu.find_drink(coffee_choice)
            sufficient_resources = my_coffee_maker.is_resource_sufficient(ordered_item)
            if sufficient_resources:
                sufficient_payment = my_money_machine.make_payment(ordered_item.cost)
                if sufficient_payment:
                    my_coffee_maker.make_coffee(ordered_item)
        elif coffee_choice == "off":
            valid_response = True
        elif coffee_choice == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        else:
            print("Invalid response.")

        is_on = False


