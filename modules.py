from requests_html import HTMLSession
from colorama import init, Fore
import json
import requests

def popular_services(username):
	session = HTMLSession()
	
	def telegram(username):
		service = 'https://t.me/'
		response = session.get(service + username)
		result = response.html.find('.tgme_page_extra', first=True)
		if bool(result) != False:
			print(Fore.GREEN + f"[+] Found: {service}{username}")
		else:
			print(Fore.RED + f"[-] Not found: {service}{username}")
	
	telegram(username)
	
	def youtube(username):
		service = 'https://youtube.com/@'
		response = session.get(service + username)
		if response.status_code == 200:
			print(Fore.GREEN + f"[+] Found: {service}{username}")
		else:
			print(Fore.RED + f"[-] Not found: {service}{username}")		
		
	youtube(username)

	def steam(username):
		service = 'https://steamcommunity.com/id/'
		response = session.get(service + username)
		result = response.html.find('.profile_header_badgeinfo', first=True)
		if bool(result) != False:
			print(Fore.GREEN + f"[+] Found: {service}{username}")
		else:
			print(Fore.RED + f"[-] Not found: {service}{username}")
			
	steam(username)
	
	def search_email(username):
		service = 'https://emailrep.io/'
		headers = {'Key':'#'} #Free API key 'https://emailrep.io/'
		addrs = ['@gmail.com', '@yandex.ru', '@mail.ru', '@yahoo.com', '@outlook.com']
		for emails in addrs:
			response = requests.get(f"{service}{username}{emails}", headers=headers)
			data = response.json()
			try:
				if data['email'] == f"{username}{emails}":
					print(Fore.GREEN + f"[+] Found: {username}{emails}")
			except Exception as error:
				print(Fore.RED + f"[-] Not found (Or Daily Limit API): {username}{emails}")
			
	search_email(username)	
