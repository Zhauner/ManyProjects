from pyfiglet import Figlet
import os
import colorama
from colorama import Fore as fo , Back

colorama.init()

text = Figlet(font='slant')
print(fo.MAGENTA + text.renderText('S O R T'))
p = f'[+]{os.getcwd()}'
print(len(p) * '_')
print(fo.CYAN + p)
print()
while True:
    print(fo.RED, Back.WHITE)
    path = input('[+]Path of file: ')
    print(Back.RESET)

    python_path = f'{os.getcwd()}\\python\\'
    txt_path = f'{os.getcwd()}\\txt\\'
    if path == '':
        break

    if os.path.isfile(path) == True:
        print(fo.GREEN + '[+]Фаил Найден!', '\n')
        name_of_file = os.path.splitext(path)[0].split('\\')
        rash = os.path.splitext(path)[1]
        if rash == '.py':
            os.system(f'move {path} {python_path}{name_of_file[-1]}.py')
            print(fo.GREEN + '[+]Файл перемещен!')
        elif rash == '.txt':
            os.system(f'move {path} {txt_path}{name_of_file[-1]}.txt')
            print(fo.GREEN + '[+]Файл перемещен!')
    else:
        print(fo.RED + '[+]Такого файла нет!')

    #move c:\test\file1.txt D:\folder2\file2.txt