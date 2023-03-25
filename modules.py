from requests_html import HTMLSession
from typing import NoReturn


def popular_services(username: str) -> NoReturn:
    session = HTMLSession()

    def telegram(username: str) -> str:
        service = "https://t.me/"
        response = session.get(service + username)
        result = response.html.find(".tgme_page_extra", first=True)
        if result:
            print(f"[+] Found: {service}{username}")
            
    telegram(username)

    def youtube(username: str) -> str:
        service = "https://youtube.com/@"
        response = session.get(service + username)
        if response.status_code == 200:
            print(f"[+] Found: {service}{username}")

    youtube(username)

    def steam(username: str) -> str:
        service = "https://steamcommunity.com/id/"
        response = session.get(service + username)
        result = response.html.find(".profile_header_badgeinfo", first=True)
        if result:
            print(f"[+] Found: {service}{username}")

    steam(username)
