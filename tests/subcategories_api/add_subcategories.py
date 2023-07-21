import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image': open('letnie_shini.jpeg','rb').read()}
	category_id = 1
	name = "Летние шины"
	slug_name = 'summer_tires'
	response = requests.post(f'{HOST_URL}/subcategories', headers=headers,files=files, params={'category_id': category_id, 'name': name, 'slug_name': slug_name})
	print(response)