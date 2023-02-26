
import colorama
from colorama import Fore as f ,Back

colorama.init()

print(f.BLUE)

print('''────────▄▄▄▄▄▄▄▄▄
────────▌▐░▀░▀░▀▐
────────▌░▌░░░░░▐
────────▌░░░░░░░▐
────────▄▄▄▄▄▄▄▄▄
──▄▀▀▀▀▀▌▄█▄░▄█▄▐▀▀▀▀▀▄
─█▒▒▒▒▒▐░░░░▄░░░░▌▒▒▒▒▒█
▐▒▒▒▒▒▒▒▌░░░░░░░▐▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒█░▀▀▀▀▀░█▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▒▌
▐▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▌
▐▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▌
▐▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▄▄▄▄▄▄▄▄▄▐▒▒▒▒▒▒▌
▐▄▄▄▄▄▄▌▌███████▌▐▄▄▄▄▄▄▌
─█▀▀▀▀█─▌███▌███▌─█▀▀▀▀█
─▐░░░░▌─▌███▌███▌─▐░░░░▌
──▀▀▀▀──▌███▌███▌──▀▀▀▀
────────▌███▌███▌
────────▌███▌███▌
──────▐▀▀▀██▌█▀▀▀▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒
На пути большой дороги, под ногами серпантин
Каменные блоки закрывают ориентир
''')

def general():
    print(Back.RESET)
    print(f.BLUE)
    off = True
    while off == True:
        command = input('>>>')

        if command == 'exit':
            off = False
        elif command == 'add':
            return todo_create()
        elif command == '?':
            print('[+] add, exit, show, del')
        elif command == 'show':
            return show_tasks()
        elif command == 'del':
            return del_tasks()

def todo_create():
    print(f.YELLOW)
    while True:

        todo = input('[+]ToDo add:>>')

        if todo == '':
            return general()

        with open('tasks.txt', 'a', encoding='utf-8') as task:
            task.write(todo + '\n')
        task.close()

def show_tasks():

    list_count = open('tasks.txt', 'r', encoding='utf-8').readlines()
    list_len = [x for x in range(1, len(list_count) + 1)]
    dict_list = (dict(zip(list_len, list_count)))

    with open('tasks.txt', 'r', encoding='utf-8') as show:
        print(f.MAGENTA)
        for x, i in dict_list.items():
            print(x, ':', i)
        print(f.GREEN + '[+]Your tasks, that you will done :)')
    show.close()

    return general()

def del_tasks():
    print(Back.WHITE + f.RED)
    while True:
        delete = input('[Delete task]:>>')

        if delete == '':
            return general()

        file = (open('tasks.txt', 'r+',encoding='utf-8'))
        lis = file.readlines()
        file.seek(0)
        for i in lis:
            if i != delete + '\n':
                file.write(i)
        file.truncate()
        file.close()



general()



