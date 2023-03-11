import services
import asyncio
import aiohttp
from modules import popular_services
from pywebio.input import input, TEXT
from pywebio.output import put_image, put_html


async def main() -> str:
    services.init()
    put_image(open("logo.png", "rb").read())
    put_html(
        f"<h1 style='text-align: center;'>Welcome to SearchMyName!</h1>\n\n<div style='text-align: center;'><a href='https://t.me/niko13teen'><img src='https://img.shields.io/badge/Telegram_Author-blue?style=for-the-badge&logo=telegram&logoColor=white' alt='Telegram Badge'/></a><a href='https://t.me/niko13teen_channel'><img src='https://img.shields.io/badge/Telegram_Channel-red?style=for-the-badge&logo=telegram&logoColor=white' alt='Telegram Badge'/></a></div>"
    )
    username: str = input(
        f"All Services: {len(services.service)}", placeholder="username...", type=TEXT
    )
    put_html(
        f"<br><div style='text-align: center;'><img src='https://media4.giphy.com/media/d3hGuic6x6e5mASmKR/giphy.gif' width='100'></div><br><br><h2> Found: </h2>"
    )
    popular_services(username)
    async with aiohttp.ClientSession() as session:
        for lists in services.service:
            try:
                async with session.get(lists + username) as response:
                    if response.status == 200:
                        put_html(
                            f"<div style='border: 1px solid black; padding: 15px; margin-top: 5px; background: #292929;'><a href='{lists}{username}' target='_blank' style='color: white;'>{lists}{username}</div></a>"
                        )
            except Exception as error:
                pass


if __name__ == "__main__":
    asyncio.run(main())
