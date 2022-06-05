from urllib.parse import urlparse, urlunparse

url = urlparse('http://www.youtube.com/watch?v=-ybKsFjHPe4')
tuple(url)
print(f'scheme = {url[0]}')
print(f'netloc = {url[1]}')
print(f'path = {url[2]}')
print(f'params = {url[3]}')
print(f'query = {url[4]}')

url = '{scheme}://www.youtube.com/{path}?v=-ybKsFjHPe4'.format(
    scheme = 'http',
    path = 'watch' )

print(f'''---- Задание 2 ----\n{urlparse(url)}''')

url_paths = ['http', 'www.youtube.com', '/watch', 'v=-ybKsFjHPe4']
youtube_url = urlunparse((url_paths[0], url_paths[1], url_paths[2], None, url_paths[3], None))
print(f'---- Задание 3 ----\n{youtube_url}')