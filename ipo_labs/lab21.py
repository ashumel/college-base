import requests
import os

#*GET запрос
url = 'http://vk.com'
headers = {'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'path' : '/method/account.getToggles?v=5.133&client_id=6287487',
           'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
response = requests.get(url, headers = headers)
print(response.json())


#*POST запрос
response = requests.post('http://vk.com', data = {'content-length' : '105'})
print(response)

#*OPTIONS запрос
os.system('curl -X OPTIONS http://vk.com -i')