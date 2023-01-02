import requests
import argparse
import services
from modules import popular_services
from colorama import init, Fore


def main(username: str):
	services.init()
	print(f"\n\n[*] All Services: {len(services.service)}\n[?] TG Author: https://t.me/niko13teen\n\n")
	popular_service(username)
	for lists in services.service:
		try:
			response = requests.get(lists + username)
			if response.status_code == 200:
				print(Fore.GREEN + f"[+] Found: {lists}{username}")
			else:
				print(Fore.RED + f"[-] Not found: {lists}")
		except Exception as error:
			pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', '-u',
                        action='store',
                        dest='username',
                        help='write username')
    args = parser.parse_args()
    main(args.username)
