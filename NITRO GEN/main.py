
   ####################################################################################################
   ### █▀▄▀█  █▀▀█  █▀▀▄  █▀▀▀      █▀▀█  █   █     ▀▀█▀▀  █   █ ▀█▀  █▀▀▄  █▀▀▄  █     █     █▀▀▀█ ###
   ### █ █ █  █▄▄█  █  █  █▀▀▀      █▀▀▄  █▄▄▄█       █    █ █ █  █   █  █  █  █  █     █     █   █ ###
   ### █   █  █  █  █▄▄▀  █▄▄▄      █▄▄█    █         █    █▄▀▄█ ▄█▄  █▄▄▀  █▄▄▀  █▄▄█  █▄▄█  █▄▄▄█ ###
   ####################################################################################################

import requests
import threading
import user_agent
import uuid
import random
import os
from colorama import Fore # UWU
from requests.exceptions import RequestException
os.system("cls")

# discord nitro generator
class NITRO:
    def __init__(self):
        # Initialize with a random user agent
        self.useragent = user_agent.generate_user_agent()

    def Proxy(self):
        try:
            # Read proxies from the file and select a random one
            with open("proxy.txt", "r") as proxy_file:
                proxy_list = random.choice(proxy_file.read().splitlines())
                https_proxy = {
                    "http": f"http://{proxy_list}",
                    "https": f"http://{proxy_list}"
                }
                return https_proxy
        except FileNotFoundError:
            print(f" {Fore.LIGHTYELLOW_EX}[{Fore.RED}X{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Proxy file not found. :c")
            return None

    def GEN(self):
        try:
            # Generate a proxy
            https_proxy = self.Proxy()
            if not https_proxy:
                return

            headers = {
                'authority': 'api.discord.gx.games',
                'accept': '*/*',
                'accept-language': 'en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                'origin': 'https://www.opera.com',
                'referer': 'https://www.opera.com/',
                'sec-ch-ua': '"Opera GX";v="104", "Chromium";v="111", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': self.useragent,
            }

            json_payload = {
                'partnerUserId': str(uuid.uuid4()),
            }

            # Make a POST request to generate a Nitro code
            response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers,
                                     json=json_payload, proxies=https_proxy)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            # Extract and print the Nitro code UWU
            token = response.json().get('token')
            if token:
                nitro_link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                short_link_end = nitro_link[-8:]
                print(f" {Fore.LIGHTYELLOW_EX}[{Fore.GREEN}V{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Generated{Fore.LIGHTBLACK_EX} discord.com/billing/partner-promotions/1180231712274387115/...{short_link_end}")
                with open("nitro.txt", "a") as nitro_file:
                    nitro_file.write(nitro_link + "\n")

        except RequestException as e:
            print(f" {Fore.LIGHTYELLOW_EX}[{Fore.RED}X{Fore.LIGHTYELLOW_EX}]{Fore.RESET}An error occurred: {Fore.LIGHTBLACK_EX}\n{e}")

    def start(self):
        while True:
            # Continuously generate Nitro codes
            self.GEN()

if __name__ == "__main__":
    # Create an instance of the NITRO
    generator = NITRO()

    while True:
        # Start a new thread for Nitro code generation
        threading.Thread(target=generator.start).start()
