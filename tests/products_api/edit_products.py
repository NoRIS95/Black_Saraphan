import requests
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
HOST_URL = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
	headers = {'Admin_token': ADMIN_TOKEN}
	files = {'image_small': open('versachi_small.jpeg','rb').read(), 
		'image_medium': open('versachi_medium.jpg','rb').read(),
		'image_large': open('versachi_large.jpg','rb').read(), }
	subcategory_id = 1
	product_id = 1
	name = "Пиджак Versachi"
	slug_name = 'coat_versachi'
	response = requests.put(f'{HOST_URL}/products',headers=headers,files=files,
		params={'subcategory_id': subcategory_id, 'id': product_id, 'name': name, 'slug_name': slug_name, 'files': files})
	print(response)
