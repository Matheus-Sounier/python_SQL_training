import requests

## Analisar o get request, se foi tudo ok ou não
# url = ('https://github.com/psf/requests')
# r = requests.get(url)
# print(r.status_code)
# 200

## Abaixar a lib request pelo pip
# pip install request


## Atribuitos e métodos para se ver em um objeto
# print(dir(r))
## mais detalhado
# print(dir(r))

## Resposta de conteúdo unicode
# print(r.text)

## Pegar imagem de um site e colocar a imagem num arquivo
# url_image = ('https://i.ytimg.com/vi/IdviYZIQLlA/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD8dij7qVFg1TO3tm2A-ZHN7x2_kg')
# image = requests.get(url_image)

# with open('good_video.png', 'wb') as cute_image:
#     cute_image.write(image.content)
    ## Isso mostra o retorno da conexão
    # print(image.status_code)
    ## Mostra o cabeçalhio que tem no site
    # print(image.headers)

## 200 = sucesso
## 300 = redirecionamento
## 400 = Erros de clientes acessando a página
## 500 = Erros de servers


## Valores do parametro
payload = {
    'page': 2,
    'count': 5
}

## Requisitar o site para uma váriavel dando paramatros adicionais
httpbin = requests.get('http://httpbin.org/get', params=payload)

## Verificar resposta do httpbin (site)
# print(httpbin.text)

## Url que foi requisitada com parametros
print(httpbin.url) # output = http://httpbin.org/get?page=2&count=5