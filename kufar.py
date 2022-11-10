import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore as f
colorama.init()
                                              #Connection
response = requests.get('https://re.kufar.by/l/baranovichi/snyat/kvartiru-dolgosrochno?cur=USD&size=\
                                30&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=')

soup = BeautifulSoup(response.text, 'lxml')

divchik1 = soup.find_all('div', id='__next')

prices = []
                                    #Find price and address, count of room and links
for x in divchik1:
    section = x.find('div', class_='styles_wrapper__CPTRM').find('div', class_='styles_main__9wjwo').\
          find('main', class_='styles_content__pwXdX').find('div', class_='styles_cards__ZRGjW').find_all('section')

    for y in section:
        price = y.find('a', class_='styles_wrapper__8rw3D').find('div', class_='styles_content__Aaqr3').\
              find('div', class_='styles_top__K6vVp').text

        count_of_rooms = y.find('a', class_='styles_wrapper__8rw3D').find('div', class_='styles_content__Aaqr3').\
            find('div', class_='styles_parameters__sDPAy styles_ellipsis__Nb6YJ').text

        link = y.find('a', class_='styles_wrapper__8rw3D').get('href')

        address = y.find('a', class_='styles_wrapper__8rw3D').find('div', class_='styles_content__Aaqr3').\
            find('div', class_='styles_wrapper__DyCkx').find('span', class_='styles_address__ohBZV').text


        pr = price.split('*')

        if pr[0] != 'Договорная/ месяц':
            res = pr[0].split('р')
            prices.append([f.YELLOW + 'BYN: ' + res[0], 'USD: ' + res[1][1:], 'Комнаты: '\
                                                    + count_of_rooms, '\n', address, '\n', f.BLUE + link])
        else:
            prices.append([f.YELLOW + pr[0], 'Комнаты: ' + count_of_rooms, '\n', address, '\n', f.BLUE + link])

sort = sorted(prices)

print(f'''░░░░░░░░░░░░░░░░░▄▄▄███▄▄▄░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█████▀▀█████░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░█████░░▄▄▄▄███▄▄░░░
░░░░░░░░░░░░░░█▀▀██▀▀█████████▀▀▀████░░░
░░░░▄▄▄▄▄███▄▄█░░░█░▄█████░░░█░░▄████░░░
░░░█▀▀█▀░░█████▀▀▀█▀░█████▀▀▀█▀░▀████░░░
░░░█░░█▄▄▄█████░░▄█▄▄█████░░░█▄▄▄████░░░
░░░█▀▀█▀░░█████▀▀▀█░░█████▀▀▀█░░░████░░░            {f.CYAN + 'Данные взяты с сайта:'}
{f.RESET}░░░█▄▄█▄▄▄█████▄▄▄█▄▄█████░░▄█▄▄▄████░░░        {f.RED + 'https://re.kufar.by/l/baranovichi/snyat/kvartiru-dolgosr'}
{f.RESET}░░░█░░█░░░█████░░▀█░░█████▀░░█░░░████░░░        {f.RED + 'ochno?cur=USD&size=30&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0='}
{f.RESET}░░░█▄▄██▄▄█████▄▄▄█▄▄█████▄▄▄█▄▄█████░░░
░░░█░░█░░░█████░░░█░░█████░░░█░░░████░░░
░░░█▄▄██▀▀█████▄▄██▀▀█████▄▄▄█▀▀█████░░░
░░░█░░█░░░█████░░░█░░█████░░░█░░░████░░░
░░░█▀▀██▀▀█████▀▀██▀▀█████▀░▀█▀▀▀████░░░
░░░█░░█░░░█████░░░█░░█████░░░█░░░████░░░
▄▄▄██████████████████████████████████▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
print(f.GREEN,'Самая выгодная --->',*sort[0])

for houses in range(1, len(sort) - 1):
    print()
    print(*sort[houses])
    print()

input()











