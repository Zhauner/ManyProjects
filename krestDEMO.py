import colorama
from colorama import Fore as f
from random import randint
from pyfiglet import Figlet

colorama.init()
text = Figlet(font='slant')
print(f.BLUE + text.renderText('K r e s t y   & \n N o l l y'))
list = [['1','2','3',], ['4','6','5',], ['8','9','7',]]

for i in list:
    print(f.MAGENTA + '     ', i)


while True:

    print(f.CYAN)


    x = input('[*] X :>> ')

    if x == '0':
       break


#User input
    for answer in range(len(list)):
        if x in list[0]:
            list[0][int(x) - 1] = x.replace(x, 'X')
        elif x in list[1]:
            list[1][4 - int(x)] = x.replace(x, 'X')
        elif x in list[2]:
            list[2][int(x) - 8] = x.replace(x, 'X')


#Bot input
    bot_input = randint(0,2)
    list_random = randint(0,2)
    if (bot_input + 1) == x and ((bot_input + 1) + 3) == x and ((bot_input + 1) + 6) == x:
        if list[list_random][bot_input] != 'X' and bot_input != x:
            list[list_random][bot_input] = 'O'
        elif list[list_random][bot_input] == 'X':
            bot_input = randint(0,2)
            list_random = randint(0,2)
            if list[list_random][bot_input] != 'X' and bot_input != x:
                list[bot_input][list_random] = 'O'
            else:
                bot_input = randint(0,2)
                list_random = randint(0,2)
        elif list[list_random][bot_input] == 'O':
            bot_input = randint(0, 2)
            list_random = randint(0, 2)
            list[bot_input][list_random] = 'O'
    else:
        list[list_random][bot_input] = 'O'





#Result
    if list[0][0] == list[0][1] == list[0][2] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[1][0] == list[1][1] == list[1][2] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[2][0] == list[2][1] == list[2][2] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[0][0] == list[1][0] == list[2][0] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[0][1] == list[1][1] == list[2][1] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[0][2] == list[1][2] == list[2][2] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[0][0] == list[1][1] == list[2][2] == 'X':
        print(f.GREEN + 'You won!')
        break
    if list[0][2] == list[1][1] == list[2][0] == 'X':
        print(f.GREEN + 'You won!')
        break

    ############bot##########BOT#BOt#######bot########################

    if list[0][0] == list[0][1] == list[0][2] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[1][0] == list[1][1] == list[1][2] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[2][0] == list[2][1] == list[2][2] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[0][0] == list[1][0] == list[2][0] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[0][1] == list[1][1] == list[2][1] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[0][2] == list[1][2] == list[2][2] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[0][0] == list[1][1] == list[2][2] == 'O':
        print(f.RED + 'You lose!')
        break
    if list[0][2] == list[1][1] == list[2][0] == 'O':
        print(f.RED + 'You lose!')
        break


    for i in list:
        print(f.MAGENTA + '     ',i)


for i in list:
    print(f.MAGENTA + '     ',i)