from colorama import Fore as f
import capmonster_python
import requests
import threading
import os
import time



def logo():
    print('                          _               _                  _')
    print(' _ __  ___  ___       ___| |__   ___  ___| | _____ _ ___ __ | |')
    print('| `_ \/ __|/ _______ / __| `_ \ / _ \/ __| |/ / _ | `__| `_ \| |')
    print('| |_) \__ | (_|_____| (__| | | |  __| (__|   |  __| |_| |_) | |')
    print('| .__/|___/\___|     \___|_| |_|\___|\___|_|\_\___|_(_| .__/|_|')
    print('|_|                                                    |_|')


def sprawdz_linie(api_url, lines):
    for linia in lines:
        full_url = f"{api_url}"
        payload = {
            "pin": linia.strip()
        }
        response = requests.post(full_url, json=payload)
        print(f"Kod: {linia.strip()}, Wynik: {response.text} - {response.status_code}")


# Otwórz plik tekstowy
with open('codes.txt', 'r') as file:
    # Wczytaj linie z pliku do listy
    lines = file.readlines()

# Utwórz wątek
thread = threading.Thread(target=sprawdz_linie, args=("https://www.paysafecard.com/index.php?eID=balanceCheck", lines))

# Uruchom wątek
thread.start()

# Poczekaj, aż wątek zakończy pracę
thread.join()