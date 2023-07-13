import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	category_id = 1
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image': open('mens_clothes.jpeg','rb').read()}
	name = "Мужская Одежда"
	slug_name = 'mens_cloth'
	response = requests.put(f'{HOST_URL}/categories',headers=headers,files=files, params={'name': name, 'slug_name': slug_name, "id": category_id})
	print(response)
