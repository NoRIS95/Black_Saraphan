import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image': open('leg_shini_logo.jpg','rb').read()}
	name = "Шины"
	slug_name = 'tires'
	response = requests.post(f'{HOST_URL}/categories',headers=headers,files=files, params={'name': name, 'slug_name': slug_name})
	print(response)

