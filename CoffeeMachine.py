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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def enough_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Calculates the cash provides"""
    print("Please inert coins.")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    cash = round(.05 * quarter + dimes + .05 * nickles + 0.01 * pennies, 2)
    return cash


def update_resources(drink, cash):
    """Update resources and return remaining cash"""
    global profit
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    profit += MENU[drink]['cost']
    cash -= MENU[drink]['cost']
    print(f"Here is ${cash} dollars in change.")


is_on = True
while is_on:
    service = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if service == "off":
        is_on = False
    elif service == "report":
        report()
    else:
        if enough_resources(service):
            money = process_coins()
            if money < MENU[service]['cost']:
                print("Sorry that's not enough money")
            else:
                update_resources(service, money)
                print(f"Here is your {service}☕. Enjoy!")
