from requests import get
from time import sleep

def ipTrack(ip):
    response = get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query')
    data = response.json()

    while True:
        if 'message' in data:
            print('\n\033[31m> Invalid/Nonexistant IP. \033[33m(Example: 123.456.789.000)\n\033[m')
            break
        else:
            print()
            print('='*28)
            print(f'\033[34mIP to Track: \033[33m{data["query"]}\033[m')
            print('='*28)
            print(f'\033[34m> Continent: \033[33m{data["continent"]}\033[m')
            print(f'\033[34m> Country: \033[33m{data["country"]}')
            print(f'\033[34m> Country Code: \033[33m{data["countryCode"]}')
            print(f'\033[34m> State: \033[33m{data["regionName"]}')
            print(f'\033[34m> City: \033[33m{data["city"]}')
            print(f'\033[34m> Latitude: \033[33m{data["lat"]}')
            print(f'\033[34m> Longitude: \033[33m{data["lon"]}')
            print(f'\033[34m> Timezone: \033[33m{data["timezone"]}')
            print(f'\033[34m> Provider: \033[33m{data["isp"]}\n\033[m')
            sleep(2)
            break

print('\n\033[34mCoded by f4ll_py\033[m')
print('\n\033[34mVersion: \033[33m0.1\033[m')
print('''\033[31m
██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  
\033[m''')

while True:
    try:
        ip = str(input('\033[32mEnter the IP (w/ dots | 0 to quit): \033[m'))
        if ip == '0':
            print('\n\033[34mCoded by f4ll_py\n\033[m')
            sleep(0.5)
            break
        else:
            ipTrack(ip)
    except(KeyboardInterrupt):
        print('\n\n\033[34mCoded by f4ll_py\n\033[m')
        sleep(0.5)
        break