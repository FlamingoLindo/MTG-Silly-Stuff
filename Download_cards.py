import requests

# URL da imagem que você quer baixar
url = 'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=130985&type=card'

# Envie uma solicitação HTTP GET para a URL
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Abra um arquivo local no modo 'wb' (escrita em binário)
    with open('image.jpg', 'wb') as file:
        # Escreva o conteúdo da resposta no arquivo
        file.write(response.content)
    print('Imagem baixada com sucesso!')
else:
    print('Falha ao baixar a imagem. Código de status:', response.status_code)
