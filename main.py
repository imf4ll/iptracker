#!/usr/bin/env python3

from rich import print
from requests import get
from modules.banner import banner
from modules.check_ip import validates_ip
from os import system, name

def clearTerminal():
    system('cls' if name == 'nt' else 'clear')

# Main
def main():
    clearTerminal()
    print(banner())

    while True:
        ipInput = input('Type the IP number to track ~> ')
        if validates_ip(ipInput):
            break
        else:
            print('Invalid ip')
            continue
    getIpInfo = get(f'http://ip-api.com/json/{ipInput}?fields=status,continent,continentCode,country,countryCode,region,regionName,city,timezone,isp,query')
    getIpInfoResult = getIpInfo.json()

    return f'''
IP Number ~> {getIpInfoResult["query"]}
Country ~> {getIpInfoResult["country"]} {getIpInfoResult["countryCode"]}
State ~> {getIpInfoResult["regionName"]}
City ~> {getIpInfoResult["city"]}
Timezone ~> {getIpInfoResult["timezone"]}
Provider ~> {getIpInfoResult["isp"]}'''

# Call main function
try:
    print(main())
except KeyboardInterrupt:
    pass
