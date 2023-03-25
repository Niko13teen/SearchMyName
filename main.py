import services
import asyncio
import aiohttp
import argparse
from modules import popular_services
from typing import NoReturn


banner: str = """
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███╗   ███╗██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║████╗ ████║╚██╗ ██╔╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
███████╗█████╗  ███████║██████╔╝██║     ███████║██╔████╔██║ ╚████╔╝ ██╔██╗ ██║███████║██╔████╔██║█████╗  
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╔╝██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚═╝ ██║   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"""

async def main(username: str) -> NoReturn:
    services.init()
    print(f"{banner}\n\nSearchMyName by Niko13Teen: https://t.me/niko13teen \nAll Services: {len(services.service) + 3}\n")
    popular_services(username)
    async with aiohttp.ClientSession() as session:
        for lists in services.service:
            try:
                async with session.get(lists + username) as response:
                    if response.status == 200:
                        print(f"[+] Found: {lists}{username}")
            except Exception as error:
                pass


if __name__ == "__main__":
    parser: object = argparse.ArgumentParser()
    parser.add_argument('--username',
                        '-u',
                        action='store',
                        dest='username',
                        help='Input username',
                        default='example',
                        )
                        
    args: str = parser.parse_args()
    asyncio.run(main(args.username))
