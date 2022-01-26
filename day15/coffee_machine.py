from data import resources, MENU 

money = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(ingredients: 'dict[str, int]'):
    is_enough = True
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def processed_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters ? "))
    dimes = int(input("How many dimes ? "))
    nickles = int(input("How many nickles ? "))
    pennies = int(input("How many pennies ? "))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

def check_transactions(cost: float, coins: float):
    global money
    if cost > coins:
        print("Sorry that's not enough money. Money refunded.​")
        return False
    elif cost == coins:
        money += coins
    elif coins > cost:
        money += cost
        change  = round(coins - cost, 2)
        print(f"Here is ${change} dollars in change.")
    return True

def craft(menu):
    global resources
    ingredients: 'dict[str, int]' = menu['ingredients']
    
    is_sufficient_resources = check_resources(ingredients)
    is_transaction_succesful = check_transactions(menu['cost'], processed_coins())
    if is_sufficient_resources and is_transaction_succesful:
        for item in ingredients:
            resources[item] -= ingredients[item]    
        return 'crafted'


while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if choice not in ['off', 'report', 'espresso', 'latte', 'cappuccino']: break
    if choice == 'off': 
        break
    elif choice == 'report': 
        report()
    elif craft(MENU[choice]) == 'crafted':
        print(f"Here is your {choice}. Enjoy!")