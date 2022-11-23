import telebot
import datetime
import colorama
from colorama import Fore as f


colorama.init()

bot = telebot.TeleBot('5428812113:AAE5FSjM8K_5hbB4hZKDpR42rMMMWVU0bGg')

def mainloop():
    print(f.RED)
    while True:

        command = input('main~notes: ')

        if command == '':
            break
        elif command == 'add':
            return add()
        elif command == 'on':
            return strt()
        elif command == '?':
            print(f.CYAN + 'add, clear, on')
            return mainloop()
        elif command == 'clear':
            with open('C:\\Users\\Stas\\Desktop\\Notification\\notifications.txt', 'w') as clr:
                clr.truncate()
                print(f.GREEN + '[!]File clear!')
            clr.close()
            return mainloop()

def add():

    print(f.BLUE + 'Example 2022-11-21 17:35 ~ Your notification\n')

    notific = input('[+]:>>  ').split('~')

    if notific[0] == '':
        mainloop()
    elif len(notific[0]) != 17:
        print(f.RED + '[!]Wrong')
        add()
    else:
        with open('C:\\Users\\Stas\\Desktop\\Notification\\notifications.txt', 'a', encoding='utf-8') as notifications:
            notifications.write(f"{notific[0].strip()}:00.1{notific[1]}" + '\n')
            notifications.close()
        add()


def strt():

    dcct = {}

    with open('C:\\Users\\Stas\\Desktop\\Notification\\notifications.txt', 'r', encoding='utf-8') as dt:
        for i in dt.readlines():
            keys = i.split(' ')[0] + ' ' + i.split(' ')[1]
            values = i[22:]
            dcct[keys] = values

    @bot.message_handler(commands=['ntfc'])
    def start(message):

        while True:
            x = datetime.datetime.now()

            if str(x)[0:-5] in dcct.keys():
                bot.send_message(message.chat.id, dcct[str(x)[0:-5]])
                continue

    print(f.RED + '\n[!]Notification bot start!\n\n', f.GREEN + 'Enter command /ntfc in bot')
    bot.polling()

mainloop()