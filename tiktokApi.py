import requests as req,random
from colorama import Fore,Back,Style
def download_tiktok(url):
	A=url.split('/')[-3];D=url.split('?')[0];B=D.split('/')[-1];E=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'];F={'User-Agent':random.choice(E)};C=req.get(f"https://tikcdn.io/ssstik/{B}",headers=F)
	if C.status_code==200:
		with open(f"video_{A}_by_k1dotok.mp4",'wb')as G:G.write(C.content)
		return{'username':A,'idVideo':B}
	else:print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.BLUE}Server Down!")