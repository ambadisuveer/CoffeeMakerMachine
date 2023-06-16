from coffee_data import MENU, resources


def print_report():
    print(resources)


def check_resources_sufficient(coffee):
    coffee_recipie = MENU[coffee]["ingredients"]
    for ingredient in coffee_recipie:
        if resources[ingredient] < coffee_recipie[ingredient]:
            return False
    return True


def process_coins(quarters, dimes, nickels, pennies, coffee):
    money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    change = 0
    sufficient_money = True
    return_value = [change, sufficient_money]
    if MENU[coffee]["cost"] == money:
        return return_value
    if MENU[coffee]["cost"] < money:
        return_value[0] = round(money - MENU[coffee]["cost"], 2)
        return return_value
    return_value[0] = round(money, 2)
    return_value[1] = False
    return return_value


def do_transaction(coffee):
    coffee_recipie = MENU[coffee]["ingredients"]
    for ingredient in coffee_recipie:
        resources[ingredient] -= coffee_recipie[ingredient]
    resources["money"] += MENU[coffee]["cost"]


resources["money"] = 0
user_input = True
while not user_input == "off":
    print("Hi Welcome to Coffee Machine")
    print("Menu\n"
          "1. Espresso : $1.5\n"
          "2. Latte : $2.5\n"
          "3. cappuccino: $3.0\n"
          "Type 'report' to see remaining resources\n"
          "Type 'off' to switch off the machine")
    user_input = (input("Enter your choice : ")).lower()
    if user_input == 'off':
        print("Turning off coffee machine")
        break
    if user_input == 'report':
        print_report()
    else:
        if check_resources_sufficient(user_input):
            print(f"Please pay ${MENU[user_input]['cost']} for your {user_input}")
            quarters = int(input("Number of quarters : "))
            dimes = int(input("Number of dimes : "))
            nickels = int(input("Number of nickels : "))
            pennies = int(input("Number of pennies : "))
            coins = process_coins(quarters, dimes, nickels, pennies, user_input)
            if coins[1]:
                do_transaction(user_input)
                print(f"Here is your {user_input}. Enjoy!")
                if coins[0] > 0:
                    print(f"Here is your remaining money ${coins[0]}")
            else:
                print(f"Insufficient money for {user_input}. Your ${coins[0]} is refunded.")
        else:
            print(f"Insufficient ingredients for {user_input}")
    print("\n\n")
