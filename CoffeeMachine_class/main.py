from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_1 = Menu()

# latte = MenuItem(name="latte", water= 200, milk=150, coffee=24, cost=2.5)
# espresso = MenuItem(name="espresso", water= 50, milk=0, coffee= 18, cost= 1.5)
# cappuccino = MenuItem(name="cappucchino", water=250, milk=100, coffee=24, cost=3.0)

coffee_machine = CoffeeMaker()

money = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"​What would you like? {menu_1.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money.report()
    else: 
        drink = menu_1.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            payment = money.make_payment(drink.cost)
            if payment == True:
                coffee_machine.make_coffee(drink)
                


# print(menu_1.get_items()) 
# print(menu_1.find_drink("espresso"))

# print(latte.name, espresso.cost, cappuccino.ingredients)

# print(coffee_machine.is_resource_sufficient(latte))
# print(coffee_machine.report())
# coffee_machine.make_coffee(latte)
# print(coffee_machine.report())

# print(money.report())
# print(money.make_payment(latte.cost))


