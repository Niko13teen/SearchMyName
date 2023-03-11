from requests_html import HTMLSession
from pywebio.output import put_html


def popular_services(username):
    session = HTMLSession()

    def telegram(username):
        service = "https://t.me/"
        response = session.get(service + username)
        result = response.html.find(".tgme_page_extra", first=True)
        if bool(result):
            put_html(
                f"<div style='border: 1px solid black; padding: 15px; margin: 5px; background: #292929;'><a href='{service}{username}' target='_blank' style='color: white;'>{service}{username} </div></a>"
            )

    telegram(username)

    def youtube(username):
        service = "https://youtube.com/@"
        response = session.get(service + username)
        if response.status_code == 200:
            put_html(
                f"<div style='border: 1px solid black; padding: 15px; margin: 5px; background: #292929;'><a href='{service}{username}' target='_blank' style='color: white;'>{service}{username} </div></a>"
            )

    youtube(username)

    def steam(username):
        service = "https://steamcommunity.com/id/"
        response = session.get(service + username)
        result = response.html.find(".profile_header_badgeinfo", first=True)
        if bool(result):
            put_html(
                f"<div style='border: 1px solid black; padding: 15px; margin: 5px; background: #292929;'><a href='{service}{username}' target='_blank' style='color: white;'>{service}{username}</div></a>"
            )

    steam(username)
