import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	category_id = 1
	response = requests.delete(f'{HOST_URL}/categories',headers=headers, params={'id': category_id})
	print(response)

