#!/usr/bin/env python3

import requests
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import colorama
from colorama import Fore


colorama.init()
print(f"""{Fore.LIGHTGREEN_EX}
 ____                        _             
/ ___|  ___ __ _ _ __   __ _| |_ ___  _ __ 
\___ \ / __/ _` | '_ \ / _` | __/ _ \| '__|
 ___) | (_| (_| | | | | (_| | || (_) | |   
|____/ \___\__,_|_| |_|\__,_|\__\___/|_|   

                                     {Fore.LIGHTMAGENTA_EX}by @letfornz""")
print('\n')

def usr_input(args=None):
    parser = argparse.ArgumentParser(description='Scanator is a tool used to find active Spring Boot Actuator directories, using the brute-froce attack method.')
    parser.add_argument('-u', '--url', type=str, help='Target url to be scan.'.title())
    parser.add_argument('-l', '--listurl', type=str, help='File containing list of URLs to test.'.title())
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist file, must be a .txt file.'.title())
    return parser.parse_args(args)

def main(args=usr_input()):

    if args.url:
        try:
            website = args.url
            wordlist = open(str(args.wordlist), 'r')
        except FileNotFoundError:
            wordlist = open('actuatorwl.txt', 'r')

        for words in wordlist:
                resp = requests.get(str(website) + str(words.strip()))
                if resp.status_code == requests.codes.ok:
                    print("Successful: " + website + words)
                elif resp.status_code == 404:
                    pass

    if args.listurl:
        try:
            website = open(str(args.listurl), 'r')
            hostlist = website.readlines()
            wordlist = open(str(args.wordlist), 'r')
        except FileNotFoundError:
            wordlist = open('actuatorwl.txt', 'r')

        for words in wordlist:
            for hostname in hostlist:
                hostname = hostname.rstrip()
                resp = requests.get(str(hostname) + str(words.strip()))
                if resp.status_code == requests.codes.ok:
                    print("Successful: " + hostname + words)
                elif resp.status_code == 404:
                    pass

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.MissingSchema:
        print('Invalid url or no url provided....'.upper())
