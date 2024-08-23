import requests
import json
from PIL import Image

#937

count = 0


for i in range(937):

    req = requests.get(f'https://api.magicthegathering.io/v1/cards?page={i}')

    all_cards = json.loads(req.text)

    for card in all_cards['cards']:
        if 'imageUrl' in card:
            print(card['imageUrl'])

            card_url = card['imageUrl']

            response = requests.get(card_url)
            
            with open(f'Images/card{count}N.jpg','wb') as file:
                file.write(response.content)

            n_image = Image.open(f'Images/card{count}N.jpg')

            # West
            w_image = n_image.rotate(90, expand=True)

            w_image.save(f'Images/card{count}W.jpg')

            w_image = Image.open(f'Images/card{count}W.jpg')

            # South
            s_image = w_image.rotate(90, expand=True)

            s_image.save(f'Images/card{count}S.jpg')    

            s_image = Image.open(f'Images/card{count}S.jpg')      

            # East
            e_image = s_image.rotate(90, expand=True)

            e_image.save(f'Images/card{count}E.jpg')       
            
            count += 1
        
