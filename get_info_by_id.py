import requests


def get_info(ip='127.0.0.1'):
    try:
        ip = input('[!] Enter ip: ')
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Org]': response.get('org'),
            '[Int prov]': response.get('isp'),
            '[Country]': response.get('country'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }


        for x, r in data.items():
            print(x,r)
    except requests.exceptions.ConnectionError:
        print('[!] Check your connection!')

get_info()

input()
