water = 1200
milk = 540
beans = 120
cups = 9
cash = 550

def print_status():
    print('The coffee machine has:')
    print('{} of water'.format(water))
    print('{} of milk'.format(milk))
    print('{} of coffee beans'.format(beans))
    print('{} of disposable cups'.format(cups))
    print('{} of money'.format(cash))

def take_action():
    action = input("Write action (buy, fill, take):\n")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    else:
        take()

def buy():
    cust_order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:\n')
    if cust_order == '1':
        # reduce 250 ml water, 16 g coffee beans
        # add $4
    elif cust_order == '2':
        # reduce 350 ml water, 75 ml milk, 20 g coffee beans,
        # add $7
    else:
        # reduce 200 ml water, 100 ml milk, 12 g coffee beans,
        # add $7

def fill():
    water_fill = int(input('Write how many ml of water do you want to add:\n'))
    # add water_fill to water
    milk_fill = int(input('Write how many ml of milk do you want to add:\n'))
    #add milk_fill to milk
    beans_fill = int(input('Write how many grams of coffee beans do you want to add:\n'))
    #add beans_fill to beans
    cups_fill = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    #add cups_fill to cups

def take():
    print('I gave you ${}'.format(cash))
    # reduce cash to 0

print_status()

take_action()

print_status()