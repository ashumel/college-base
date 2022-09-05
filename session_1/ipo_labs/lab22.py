import requests, json

url_list = ['https://vk.com', 'https://www.youtube.com/cringe', 'https://api.github.com/user']
json_list = []
import numpy

for url in url_list:
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        pass
        #print(response.text)
        #print(response.headers['Content-Type'])
        print(response.headers)