##Rename directory

import os
import colorama
from colorama import Fore as f

colorama.init()

print(f'''
  {f.RED}  ____     ______   _   __   ___       __  ___   ______
   / __ \   / ____/  / | / /  /   |     /  |/  /  / ____/            V1.00
  / /_/ /  / __/    /  |/ /  / /| |    / /|_/ /  / __/   
 {f.WHITE}/ _, _/  / /___   / /|  /  / ___ |   / /  / /  / /___       {os.getcwd()}
/_/ |_|  /_____/  /_/ |_/  /_/  |_|  /_/  /_/  /_____/\n''')

print(f'[*]Пример C:\\Users\\user\\folder\your_folder\\' + '   <---------')
print('-' * 57)
path = input('[!]Введите путь ------> ')
name_of_dirs = os.listdir(path)

list_dir = []
list_names = []
name_dir = ''

for i in name_of_dirs:
    if os.path.isdir(f'{path}{i}') == True:
        list_dir.append(f'{path}{i}')

for x in range(1, len(list_dir) + 1):
    name_dir = 'dir' + str(x)
    list_names.append(name_dir)

for y in range(len(list_dir)):
    os.rename(f'{list_dir[y]}',f'{path}{list_names[y]}')
    
print(f.GREEN + '\n\n[!]Папки переименованы!  [OK]')
#well
input()


