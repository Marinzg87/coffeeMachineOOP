from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

print(logo)
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ").lower()
    if choice == "off":
        print("Welcome in service mode.")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink) and
                money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
