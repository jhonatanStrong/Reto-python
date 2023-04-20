import requests as r

response = r.get('http://127.0.0.1:8000/api/v1/valores')

#https://www.sii.cl/valores_y_fechas/uf/uf2023.htm

#http://127.0.0.1:8000/

a = response.headers
b =response.headers['Content-Type']
json_response = response.json()


repository = json_response[0][0]['fecha']
#b = dict(a)

print((a))
print((b))
print(repository)