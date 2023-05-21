from requests_html import HTMLSession
from typing import NoReturn


banner = """
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███╗   ███╗██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║████╗ ████║╚██╗ ██╔╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
███████╗█████╗  ███████║██████╔╝██║     ███████║██╔████╔██║ ╚████╔╝ ██╔██╗ ██║███████║██╔████╔██║█████╗  
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╔╝██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚═╝ ██║   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"""


def popular_services(username: str) -> str:
    service = {
        "telegram": "https://t.me/",
        "youtube": "https://youtube.com/@",
        "steam": "https://steamcommunity.com/id/",
    }
    session = HTMLSession()

    def telegram(username: str) -> NoReturn:
        response = session.get(service["telegram"] + username)
        result = response.html.find(".tgme_page_extra", first=True)
        if result:
            title: str = response.html.find("title", first=True)
            print(
                f"[+] Found: {response.url} [{title.text}]"
                if title and len(title.text) < 120
                else f"[+] Found: {response.url}"
            )

    def youtube(username: str) -> NoReturn:
        response = session.get(service["youtube"] + username)
        if response.status_code == 200:
            title: str = response.html.find("title", first=True)
            print(
                f"[+] Found: {response.url} [{title.text}]"
                if title and len(title.text) < 120
                else f"[+] Found: {response.url}"
            )

    def steam(username: str) -> NoReturn:
        response = session.get(service["steam"] + username)
        result = response.html.find(".profile_header_badgeinfo", first=True)
        if result:
            title: str = response.html.find("title", first=True)
            print(
                f"[+] Found: {response.url} [{title.text}]"
                if title and len(title.text) < 120
                else f"[+] Found: {response.url}"
            )

    return telegram(username), youtube(username), steam(username)


def singleton(class_: object):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance
