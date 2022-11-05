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

def money_collector():
    global total_money
    quater = int(input('How many quaters: '))
    dyne = int(input("How many dynes"))
    nickel = int(input("How many nickels: "))
    penny = int(input('How many pennies: '))
    total_quater = quater*0.25
    total_dyne = dyne*0.10
    total_nickel = nickel*0.05
    total_penny = penny*0.01
    total_money = total_nickel+total_dyne+total_penny+total_quater

def make_coffee():
    water_mac = 300 
    milk_mac = 200
    coffee_mac = 100
    money_mac = 0
    is_machine_off = False
    while is_machine_off == False:
        ask_usr = input('What would you like expresso/latte/cappuccino: ')
        if ask_usr == 'report':
            print(f'water left {water_mac}ml')
            print(f'milk: {milk_mac}ml')
            print(f'coffee: {coffee_mac}g')
            print(f'money: ${money_mac}')
        if ask_usr == 'espresso':
            if water_mac > MENU["espresso"]["ingredients"]["water"]:
                if coffee_mac > MENU["espresso"]["ingredients"]["coffee"]:
                    money_collector()
                    if total_money < 1.50:
                        print('sorry , money is insufficient')
                        is_machine_off = False
                    elif total_money >= 1.50:
                        water_mac = water_mac - 50
                        coffee_mac = coffee_mac - 18
                        change = total_money - 1.50
                        print('here is your change' , '$',change)
                        money_mac = money_mac + 1.50
                        is_machine_off = False
                else:
                    print('insufficient coffee')
                    is_machine_off = False
            else:
                print('insufficient water')
                is_machine_off = False
        elif ask_usr == 'latte':
            if water_mac > MENU["latte"]["ingredients"]["water"]:
                if coffee_mac > MENU["latte"]["ingredients"]["coffee"]:
                    if milk_mac > MENU["latte"]["ingredients"]["milk"]:
                        money_collector()
                        if total_money < 2.50:
                            print('money insufficient')
                            is_machine_off = False
                        elif total_money >= 2.20:
                            water_mac = water_mac - 200
                            coffee_mac = coffee_mac - 24
                            milk_mac  = milk_mac - 150
                            change_l = total_money - 2.50
                            print('here is your change' , '$' , change_l)
                            money_mac = money_mac + 2.50
                            is_machine_off = False
                    else:
                        print('less milk')
                        is_machine_off = False
                else:
                    print('less coffee')
                    is_machine_off = False
            else:
                print('less water')
                is_machine_off = False
        elif ask_usr == 'cappuccino':
            if water_mac > MENU["cappuccino"]["ingredients"]["water"]:
                if coffee_mac > MENU["cappuccino"]["ingredients"]["coffee"]:
                    if milk_mac > MENU["cappuccino"]["ingredients"]["milk"]:
                        money_collector()
                        if total_money < 3.0:
                            print('money insufficient')
                            is_machine_off = False
                        elif total_money >= 3.0:
                            water_mac = water_mac - 280
                            coffee_mac = coffee_mac - 24
                            milk_mac  = milk_mac - 100
                            change_c = total_money - 3.0
                            print('here is your change' , '$', change_c)
                            money_mac = money_mac + 3.0
                            is_machine_off = False
                    else:
                        print('less milk')
                        is_machine_off = False
                else:
                    print('less coffee')
                    is_machine_off = False
            else:
                print('less water')
                is_machine_off = False
        elif ask_usr == 'refill':
            water_mac = 300
            milk_mac = 300
            coffee_mac = 300
            is_machine_off = False
        elif ask_usr == 'off':
            is_machine_off = True
        else:
            print('pls enter a valid operation')
            is_machine_off = False
make_coffee()
