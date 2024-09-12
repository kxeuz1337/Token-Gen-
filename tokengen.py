import random
import string
import requests
import time
from colorama import Fore, init
import os

init(autoreset=True)

def generate_token():
    starts = ["MTE0NDQ1", "MTEx", "MTIwOTQ2O", "MTE0NDky", "MTIxMTQ", "MTIxMjc"]
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    secret = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    secret2 = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

    return f"{random.choice(starts)}{secret2}.{secret}.{token}"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def update_title(valid_count, inv_count):
    if os.name == 'nt':
        os.system(f'Title Token Gen - Valid: {valid_count} - Invalid: {inv_count}')
    else:
        os.system(f'echo -ne "\033]0;Token Gen - Valid: {valid_count} - Invalid: {inv_count}\007"')
def main():
    valid_count = 0
    inv_count = 0
    clear_screen()
    update_title(valid_count, inv_count)
    print(Fore.LIGHTMAGENTA_EX + '''
                                ██╗  ██╗██╗  ██╗███████╗██╗   ██╗███████╗
                                ██║ ██╔╝╚██╗██╔╝██╔════╝██║   ██║╚══███╔╝
                                █████╔╝  ╚███╔╝ █████╗  ██║   ██║  ███╔╝ 
                                ██╔═██╗  ██╔██╗ ██╔══╝  ██║   ██║ ███╔╝  
                                ██║  ██╗██╔╝ ██╗███████╗╚██████╔╝███████╗
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
    ''')
    while True:
        try:
            token = generate_token()
            response = requests.get("https://discord.com/api/v10/users/@me", headers={'Authorization': token})
            
            if response.status_code == 200:
                print(f"{Fore.LIGHTBLUE_EX}Token: {Fore.LIGHTBLACK_EX}{token} {Fore.LIGHTBLUE_EX}-> {Fore.LIGHTGREEN_EX}Valid")
                valid_count += 1
                with open("tokens.txt", 'a', encoding="utf-8") as file:
                    file.write(f"{token}\n")
            else:
                print(f"{Fore.LIGHTBLUE_EX}Token: {Fore.LIGHTBLACK_EX}{token} {Fore.LIGHTBLUE_EX}-> {Fore.LIGHTRED_EX}Invalid")
                inv_count += 1
            
            update_title(valid_count, inv_count)
            time.sleep(1)
        except requests.RequestException as e:
            print(f"{Fore.RED}Network error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
