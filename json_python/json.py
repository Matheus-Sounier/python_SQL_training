import requests

requisicoes = requests.get("https://economia.awesomeapi.com.br/json/last/:moedas")
print(requisicoes)