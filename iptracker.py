#!/usr/bin/env python3
try:
    from requests import get
    from sys import argv
except Exception as e:
    print(f'Missing this module: {e}')
    print("Try 'pip install -r dependencies.txt' to install all modules.")

def ipTrack(ip):
    response = get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query')
    data = response.json()

    while True:
        if data["status"] == 'fail':
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
            break

print('\n\033[34mCoded by f4ll_py\033[m')
print('\n\033[34mVersion: \033[33m0.2\033[m')
print('''\033[31m
██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  
\033[m''')

while True:
    if len(argv) == 1:
        print('\n\033[31m> Invalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m\n')
        break
    else:
        if argv[1] != '':
            arg_cmd = argv[1]
            if arg_cmd == '-t' or arg_cmd == '--target':
                if len(argv) == 3:
                    arg_target = argv[2]
                    ipTrack(arg_target)
                    break
                else:
                    print('\n\033[31m> Invalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m\n')
                    break
            if arg_cmd == '-h' or arg_cmd == '--help':
                print('> Basic Commands:\n')
                print('>   -h                 Help')
                print('>   --help             Help')
                print('>   -t {IP}            Target IP')
                print('>   --target {IP}      Target IP\n')
                break