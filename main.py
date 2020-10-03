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

    print(f'\nIP Number ~> {getIpInfoResult["query"]}')
    print(f'Country ~> {getIpInfoResult["country"]} {getIpInfoResult["countryCode"]}')
    print(f'State ~> {getIpInfoResult["regionName"]}')
    print(f'City ~> {getIpInfoResult["city"]}')
    print(f'Timezone ~> {getIpInfoResult["timezone"]}')
    print(f'Provider ~> {getIpInfoResult["isp"]}')

    time.sleep(3)

# Call main function
main()
