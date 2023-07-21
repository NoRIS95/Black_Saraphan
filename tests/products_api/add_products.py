import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image_small': open('michelin_small.jpg','rb').read(), 'image_medium': open('shiny-michelin_medium.jpg','rb').read(), 'image_large': open('Michelin-Pilot-Sport-large.jpg','rb').read(), }
	subcategory_id = 1
	name = "Шины Michelen"
	slug_name = 'tires_michelen'
	response = requests.post(f'{HOST_URL}/products',headers=headers,files=files, params={'subcategory_id': subcategory_id, 'name': name, 'slug_name': slug_name, 'files': files})
	print(response)
