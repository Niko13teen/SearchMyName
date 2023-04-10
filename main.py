import argparse
from requests_html import HTMLSession
from modules import popular_services, banner, singleton
from services import service
from typing import NoReturn


@singleton
class SearchName(object):
    def __init__(self, username: str):
        self.username = username
        self.session = HTMLSession()
        print(
            f"{banner}\n\nSearchMyName by Niko13Teen: https://t.me/niko13teen \nAll Services: {len(service) + 3}\n"
        )

    def __repr__(self):
        return f"Username: {self.username}"

    def search(self):
        for url_address in service:
            try:
                response = self.session.get(url_address + self.username)
                if response.status_code == 200:
                    title: str = response.html.find("title", first=True)
                    print(
                        f"[+] Found: {response.url} [{title.text}]"
                        if title and len(title.text) < 120
                        else f"[+] Found: {response.url}"
                    )
            except Exception as error:
                print(f"[?] Failed: {response.url}")
                continue


def run_search(username: str) -> NoReturn:
    payload = SearchName(username)
    try:
        popular_services(username)
        payload.search()
    except Exception as error:
        return f"[!] Failed! Please, report author."


if __name__ == "__main__":
    parser: object = argparse.ArgumentParser()
    parser.add_argument(
        "--username",
        "-u",
        action="store",
        dest="username",
        help="Input username",
        default="example",
    )

    args: str = parser.parse_args()
    run_search(args.username)
