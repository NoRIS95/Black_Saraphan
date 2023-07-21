import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image': open('mens_coats.jpg','rb').read()}
	subcategory_id = 1
	category_id = 1
	new_name = 'Пиджаки'
	slug_name = 'summer_tires'
	response = requests.put(f'{HOST_URL}/subcategories',headers=headers,files=files, params={'category_id': category_id, 'id': subcategory_id, 'slug_name': slug_name, 'name': new_name})
	print(response)
