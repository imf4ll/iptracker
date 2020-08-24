#!/usr/bin/env python3
try:
    from requests import get
    from sys import argv
except Exception as e:
    print()
    print(f'\033[31mError with a module: {e}\033[m')
    print("\033[31mTry 'pip install -r dependencies.txt' to install all modules.\033[m")
    print()
else:
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
                print(f'[+] \033[34mIP to Track: \033[33m{data["query"]}\033[m')
                print('='*28)
                print(f'[+] \033[34mContinent: \033[33m{data["continent"]}\033[m')
                print(f'[+] \033[34mCountry: \033[33m{data["country"]}\033[m')
                print(f'[+] \033[34mCountry Code: \033[33m{data["countryCode"]}\033[m')
                print(f'[+] \033[34mState: \033[33m{data["regionName"]}\033[m')
                print(f'[+] \033[34mCity: \033[33m{data["city"]}\033[m')
                print(f'[+] \033[34mLatitude: \033[33m{data["lat"]}\033[m')
                print(f'[+] \033[34mLongitude: \033[33m{data["lon"]}\033[m')
                print(f'[+] \033[34mTimezone: \033[33m{data["timezone"]}\033[m')
                print(f'[+] \033[34mProvider: \033[33m{data["isp"]}\n\033[m')
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
            print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m\n')
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
                        print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m\n')
                        break
                if arg_cmd == '-h' or arg_cmd == '--help':
                    print('[+] Basic Commands:\n')
                    print('[+]   -h                 Help')
                    print('[+]   --help             Help')
                    print('[+]   -t {IP}            Target IP')
                    print('[+]   --target {IP}      Target IP')
                    break