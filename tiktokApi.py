import requests as req
import random
from colorama import Fore, Back, Style

def download_tiktok(url):
    getdataclean1 = url.split('/')[-3]
    getdataclean2 = url.split('?')[0]
    getdataclean3 = getdataclean2.split('/')[-1]


    userAgent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    ]

    headers = {
    "User-Agent": random.choice(userAgent)
    }

    respone = req.get(f"https://tikcdn.io/ssstik/{getdataclean3}", headers=headers)

    if respone.status_code == 200:
        with open(f"video_{getdataclean1}_by_k1dotok.mp4", "wb") as video:
            video.write(respone.content)
        return {
            "username": getdataclean1,
            "idVideo": getdataclean3
        }
    else:
        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.BLUE}Server Down!")


