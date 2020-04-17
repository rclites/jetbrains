stock = [400, 540, 120, 9, 550] # water, milk, beans, cups and cash

def print_status(stock):
    status = '''
The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money'''.format(stock[0], stock[1], stock[2], stock[3], stock[4])
    print(status)


def take_action():
    action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    else:
        leave()


def buy():
    global stock
    cust_order = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:\n')
    while cust_order == '1':
        if stock[0] >= 250:
            stock[0] -= 250
        else:
            print('Sorry, not enough water!')
            break
        if stock[2] >= 16:
            stock[2] -= 16
        else:
            print('Sorry, not enough coffee beans!')
            break
        if stock[3] >= 1:
            stock[3] -= 1
        else:
            print('Sorry, not enough disposable cups!')
            break
        stock[4] += 4
        print('I have enough resources, making you a coffee!')
        break
    while cust_order == '2':
        if stock[0] >= 350:
            stock[0] -= 350
        else:
            print('Sorry, not enough water!')
            break
        if stock[1] >= 75:
            stock[1] -= 75
        else:
            print('Sorry, not enough milk!')
            break
        if stock[2] >= 20:
            stock[2] -= 20
        else:
            print('Sorry, not enough coffee beans!')
            break
        if stock[3] >= 1:
            stock[3] -= 1
        else:
            print('Sorry, not enough disposable cups!')
            break
        stock[4] += 7
        print('I have enough resources, making you a coffee!')
        break
    while cust_order == '3':
        if stock[0] >= 200:
            stock[0] -= 200
        else:
            print('Sorry, not enough water!')
            break
        if stock[1] >= 100:
            stock[1] -= 100
        else:
            print('Sorry, not enough milk!')
            break
        if stock[2] >= 12:
            stock[2] -= 12
        else:
            print('Sorry, not enough coffee beans!')
            break
        if stock[3] >= 1:
            stock[3] -= 1
        else:
            print('Sorry, not enough disposable cups!')
            break
        stock[4] += 6
        print('I have enough resources, making you a coffee!')
        break
    else:
        take_action()


def fill():
    global stock
    stock[0] += int(input('Write how many ml of water do you want to add:\n'))
    stock[1] += int(input('Write how many ml of milk do you want to add:\n'))
    stock[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
    stock[3] += int(input('Write how many disposable cups of coffee do you want to add:\n'))


def take():
    global stock
    print(f'\nI gave you ${stock[4]}')
    stock[4] = 0


def remaining():
    print_status(stock)


def leave():
    global x
    x = 1


x = 0
while x == 0:
    take_action()
