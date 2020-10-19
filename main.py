#!/usr/bin/env python3

from rich import print
from requests import get
from ascii import ascii

import os
import time

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main
def main():
    clearTerminal()
    print(ascii)

    ipInput = input('Type the IP number to track ~> ')
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
print(main())
