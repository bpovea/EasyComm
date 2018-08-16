import requests
import json 
session = requests.Session()
data = {
    "username": "mauricio",
    "password": "a1234567890"
}
#response = session.post('http://localhost:8001/api/login/', json=data)
#{"non_field_errors":["Staff users can not log in via the rest api"]} 				no funciona: next >  crear otro usuario y probar no statff

def load_clases(url,session,file):
	file = open(file, 'r')
	json_data = json.load(file)
	for data in json_data:
		response = session.post(url, json=data)
		print(response.content)
	file.close()

def cargar_categorias(url,session,file):
	file = open(file, 'r')
	json_data = json.load(file)
	for data in json_data:
		response = session.post(url, data=data,files={'image':open(data['image'], 'rb')} )
		print(response.content)
	file.close()

def cargar_productos(url,session,file):
	file = open(file, 'r')
	json_data = json.load(file)
	for data in json_data:
		categories = data.pop('categories')
		stock = data.pop("stockrecords")
		data['categories'] = []
		for category in categories:
			response = session.get('http://127.0.0.1:8000/api/products-categories/' + str(category) + '/')
			data['categories'].append(json.loads(response.content))
		for image in data['images']:
			image['original'] = open(image['original'], 'rb')
		images = data.pop('images')
		response = session.post(url, data=data)
		print(response.content)
	file.close()
load_clases('http://localhost:8000/api/products-class/',session,"clases.json")
cargar_categorias('http://localhost:8000/api/products-categories/',session,"categorias.json")
# no funciona aun cargar_productos('http://localhost:8000/api/products/',session,"products.json")
