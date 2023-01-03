from requests_html import HTMLSession
from colorama import init, Fore

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
	
	#TODO
