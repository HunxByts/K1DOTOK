from tiktokApi import download_tiktok as downloadTTOk
import time
from colorama import Fore, Back, Style

print(f"""{Fore.CYAN}

██╗  ██╗ ██╗██████╗  ██████╗ ████████╗ ██████╗ ██╗  ██╗
██║ ██╔╝███║██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██║ ██╔╝
{Fore.WHITE}█████╔╝ ╚██║██║  ██║██║   ██║   ██║   ██║   ██║█████╔╝{Fore.CYAN}
██╔═██╗  ██║██║  ██║██║   ██║   ██║   ██║   ██║██╔═██╗ 
██║  ██╗ ██║██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║  ██╗
╚═╝  ╚═╝ ╚═╝╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝

{Fore.WHITE}> {Fore.CYAN} DEVELOP BY K1LLU
{Fore.WHITE}> {Fore.WHITE} TIKTOK DOWNLOADER  
""")

try:
    downloadTiktok = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] {Fore.CYAN}Enter Your Link Tiktok : {Fore.WHITE}")
    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.CYAN}Process Download...")
    time.sleep(1)

    result = downloadTTOk(downloadTiktok)
    print(f"""
{Fore.WHITE}> {Fore.CYAN}Username {Fore.WHITE}: {Fore.CYAN}{result['username']}
{Fore.WHITE}> {Fore.CYAN}ID Video {Fore.WHITE}:{Fore.CYAN}{result['idVideo']}
{Fore.WHITE}> {Fore.CYAN}Download Success... 
""")
except KeyboardInterrupt:
    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.CYAN}User to  Press CTRL + C")
except TypeError as e:
    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.CYAN}Server Error {e}")
