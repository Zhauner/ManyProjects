import os
import colorama
from colorama import Fore as f

colorama.init()

print(f'''
                      {f.BLUE}  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                       
                       {f.BLUE}@@{f.WHITE},*,,,,,,,,,,,,,,,,,,,,,,,,,,,*{f.BLUE}*@%                      
                       {f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{f.BLUE}*@%        Sort files              
                       {f.BLUE}@@{f.WHITE},,,,***********************,,,{f.BLUE}*@%                      
                       {f.BLUE}@@{f.WHITE},,,,&@@@@@@@@@@@@@@@@@@@@@%,,,{f.BLUE}*@%                      
                       {f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,**,,,,,,,,,,,,,,{f.BLUE}*@%                      
             {f.RED}@@@@@@@@@@{f.BLUE}@@{f.WHITE},,,,,******,,************,*,,,{f.BLUE}*@%                      
           {f.RED}@@..........{f.BLUE}@@{f.WHITE},,,,*&&&&&&&&&&&&&&&&&&&&&,,,,{f.BLUE}*@%                     
          {f.RED}%@...........{f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{f.BLUE}*@%                      
          {f.RED}%@...........{f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{f.BLUE}*@@{f.RED}@@%                   
          {f.RED}%@...........{f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{f.BLUE}*@%{f.RED}..%@*         v.2.0             
          {f.RED}%@...........{f.BLUE}@@{f.WHITE},,,,,,,,,,,*,,,,,,,,,,,,,,,,,,{f.BLUE}*@%{f.RED}...@@                 
          {f.RED}%@...........{f.BLUE}@@{f.WHITE},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{f.BLUE}*@%{f.RED}...@@                 
          {f.RED}%@......../@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*          
          {f.RED}%@......@@*...............................................%@          
          {f.RED}%@.....@@................................................#@/          
          %@....@@................................................#@/           
          %@...@@................................................#@(            
          %@..@@................................................#@/             
          %@.@@................................................(@/              
          %@@@................................................(@#               
           @@................................................%@#                
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,
''')

print(f.CYAN, f'example: {os.getcwd()}\\', '\n')

path = input('Path -----> ')

dirs = []
files = []
                                    #Create dirs
for file in os.listdir(path):
    if os.path.isfile(f'{path}{file}') == True:
        dirs.append(file.split('.')[1])
        files.append(file)

dir_names = list(set(dirs))

for dir_r in dir_names:
    if os.path.exists(f'{path}{dir_r}') == True:
        continue
    else:
        os.mkdir(f'{path}{dir_r}')

                                    #Move files

for move in files:
    file_name = os.path.splitext(f'{path}{move}')
    if file_name[1][1:] in dir_names:
        os.system(f'move "{path}{move}" "{path}\\{file_name[1][1:]}\\{move}"')


print(f.GREEN + '[!]Файлы перемещены')
input()
