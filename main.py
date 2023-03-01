import requests
import argparse
import services
import asyncio
import aiohttp
from modules import popular_services
from colorama import init, Fore
from typing import NoReturn


string: str = """ 
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███╗   ███╗██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║████╗ ████║╚██╗ ██╔╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
███████╗█████╗  ███████║██████╔╝██║     ███████║██╔████╔██║ ╚████╔╝ ██╔██╗ ██║███████║██╔████╔██║█████╗  
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╔╝██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚═╝ ██║   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                            by Niko13TeeN"""


async def main(username: str) -> NoReturn:
	services.init()
	print(f"\n{string}\n[*] All Services: {len(services.service)}\n[?] Channel: https://t.me/niko13teen_channel\n\n")
	popular_services(username)
	async with aiohttp.ClientSession() as session:
	    for lists in services.service:
	        try:
	            async with session.get(lists + username) as response:
	                if response.status == 200:
	                    print(Fore.GREEN + f"[+] Found: {lists}{username}")
	        except Exception as error:
	            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', '-u',
                        action='store',
                        dest='username',
                        help='write username')
    args = parser.parse_args()
    asyncio.run(main(args.username))
