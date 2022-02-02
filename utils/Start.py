import os
import time
import requests
import sys
import json


def get_info():
    with open('config.json') as f:
        js = json.load(f)
    salad_auth = js['salad_key']
    salad_refresh_token = js['salad_refresh_token']
    cookie = {
        "sAccessToken": salad_auth,
        "sIdRefreshToken": salad_refresh_token
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Salad/0.4.2 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
    }
    with open('utils/Login screen.txt', encoding='utf-8') as f:
        login_screen = f.read()

    salad_user = requests.get(url='https://app-api.salad.io/api/v1/profile', headers=headers, cookies=cookie)
    if salad_user.status_code != 200:
        print('REPLACE YOUR SALAD AUTH CODE!')
        input()
        exit()
    salad_user = salad_user.json()

    referral = requests.get(url='https://app-api.salad.io/api/v1/profile/referral-code', headers=headers,
                            cookies=cookie)
    if referral.status_code != 200:
        print('REPLACE YOUR SALAD AUTH CODE!')
        input()
        exit()
    referral = referral.json()
    return [salad_user, referral, login_screen]


def print_info(salad_user, login_screen):
    print(login_screen)
    print('Username: ' + str(salad_user['username']))
    print('Email: ' + str(salad_user['email']))
    print('User id: ' + str(salad_user['id']))
    # print('Username: HIDDEN IN TEST MODE!')
    # print('Email: HIDDEN IN TEST MODE!')
    # print('User id: HIDDEN IN TEST MODE!')
    print("\n\n")




def starting(info):
    os.system('clear')
    sys.stdout.write("\x1b]2;Salad CLI+\x07")
    color = "\033[32m"  # this color is green
    os.system(f"echo {color}")
    print(info[2])
    # input selection
    return 6
    print_info(info[0], info[2])
