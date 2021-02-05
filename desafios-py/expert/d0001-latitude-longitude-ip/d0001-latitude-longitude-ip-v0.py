# terminal pip install requests
import requests

ip=input("Prezado(a) usuário(a), informe seu ip: ")

#o key é desnecessário é so colar url ja com a chave obtida no site https://ipstack.com/quickstart
#ex http://api.ipstack.com/{ip}?access_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
key=input("Informar chave de acesso no site ipstack: ")

request=requests.get(f"http://api.ipstack.com/{ip}?access_key={key}")

location=request.json()

print('Latitude:',location['latitude'])
print('Longitude:',location['longitude'])
