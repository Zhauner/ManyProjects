###Stone Paper Scissors

from random import choice
import colorama as c
from colorama import Fore as f
from pyfiglet import Figlet

c.init()

text = Figlet(font='slant')
print(f.BLUE + text.renderText('S t P a S c'))

print(f.YELLOW + '1. Камень\n2. Бумага\n3. Ножницы\n')

exit = '[!]Для выхода нажмите 0'
print(f.LIGHTRED_EX + '-' * len(exit))
print(exit)
print('-' * len(exit))

bot_list = ['Камень', 'Бумага', 'Ножницы']

while True:
    print(f.WHITE)
    #Bot input
    bot_input = choice(bot_list)

    ##User input
    user_input = input('Ваш ход: ')

    if user_input == '0':
        break


    if user_input == '1' and bot_input == 'Камень':
        print(f.CYAN +  f'\nТвой ход: Камень\nХод компьютера: {bot_input}')
        print(f.MAGENTA + '\n[-]Ничья')
    elif user_input == '1' and bot_input == 'Бумага':
        print(f.CYAN + f'\nТвой ход: Камень\nХод компьютера: {bot_input}')
        print(f.RED + '\n[!]Ты проиграл!')
    elif user_input == '1' and bot_input == 'Ножницы':
        print(f.CYAN + f'\nТвой ход: Камень\nХод компьютера: {bot_input}')
        print(f.GREEN + '\n[+]Ты выйграл!')
    elif user_input == '2' and bot_input == 'Камень':
        print(f.CYAN + f'\nТвой ход: Бумага\nХод компьютера: {bot_input}')
        print(f.GREEN + '\n[+]Ты выйграл!')
    elif user_input == '2' and bot_input == 'Бумага':
        print(f.CYAN + f'\nТвой ход: Бумага\nХод компьютера: {bot_input}')
        print(f.MAGENTA + '\n[-]Ничья!')
    elif user_input == '2' and bot_input == 'Ножницы':
        print(f.CYAN + f'\nТвой ход: Бумага\nХод компьютера: {bot_input}')
        print(f.RED + '\n[!]Ты проиграл!')
    elif user_input == '3' and bot_input == 'Камень':
        print(f.CYAN + f'\nТвой ход: Ножницы\nХод компьютера: {bot_input}')
        print(f.RED + '\n[!]Ты проиграл!')
    elif user_input == '3' and bot_input == 'Бумага':
        print(f.CYAN + f'\nТвой ход: Ножницы\nХод компьютера: {bot_input}')
        print(f.GREEN + '\n[+]Ты выйграл!')
    elif user_input == '3' and bot_input == 'Ножницы':
        print(f.CYAN + f'\nТвой ход: Ножницы\nХод компьютера: {bot_input}')
        print(f.MAGENTA + '\n[-]Ничья!')
    elif user_input != '1' or user_input != '2' or user_input != '3':
        print(f.RED + '\n[!]Введите цифру от 1 до 3')