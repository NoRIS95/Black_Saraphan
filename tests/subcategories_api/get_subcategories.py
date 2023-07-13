import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == '__main__':
	headers = {
		"Admin_token": ADMIN_TOKEN
	}
	per_page = 10
	response = requests.get(f'{HOST_URL}/subcategories', headers=headers, params={'per_page':per_page})
	print(response)
	if response.status_code == 200:
		print(response.json())
