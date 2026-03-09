import requests

# update_coins = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# print(update_coins.json())
# dict = update_coins.json()
# print(dict['BTCBRL']['name'])

# return_last_days = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
# dict = return_last_days.json()
# print(help(dict))
# print(help(dict))

# url_awesome = ('https://docs.awesomeapi.com.br/api-de-moedas')
# awesome_site = requests.get(url_awesome)

# if awesome_site == 200 and awesome_site.text:
#     dictio = awesome_site.json()
#     print(dictio)
# else:
#     print(f'Error: {awesome_site.status_code}')
#     print(f'Response: {awesome_site.text}')

# url_photo = ('https://m.media-amazon.com/images/I/715vwvP5ZEL.png')

# some_photo = requests.get(url_photo)
# print(some_photo.headers)

# with openython/some_("json_photo.png", 'wb') as file:
#     file.write(some_photo.content)



# def fetch_data(endpoint, filter={}):
url_series = 'https://rickandmortyapi.com/api/character'
resposta = requests.get(url_series).json()
    # return respostak.json() if resposta.status_code == 200 else None

# personagem = fetch_data('character', {'name': 'Rick'})

# if personagem:
#     print(personagem)
# else:
#     print('Falha no fetch!')

for informacoes in resposta['results']:
    nome = informacoes['name']
    id = informacoes['id']
    url = informacoes['url']
    image_series = informacoes['image']
    print (f'Nomes: {nome} \t id: {id}  \t {url}  \t {image_series}')