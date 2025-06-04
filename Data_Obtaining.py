import requests
from bs4 import BeautifulSoup

r= requests.get("https://www.bbc.com/news")
soup= BeautifulSoup(r.text, 'html.parser')

headlines = soup.find('body').find_all('h2')

card_description = soup.find('body').find_all('p')

#for x in headlines:
    #print(x.text.strip())

#for headline, description in zip(headlines, card_description):
    #print(f"Başlık: {headline.text.strip()}")
    #print(f"Açıklama: {description.text.strip()}\n")

description_index = 0
for headline in headlines:
    print(f"Başlık: {headline.text.strip()}")
    
    # Eğer başlık 'card_headline' sınıfına sahipse, açıklama eklemiyoruz
    if 'card_headline' in headline.get('class', []):
        print("(Bu başlık için açıklama yok)\n")
    else:
        # Eğer açıklama varsa ekliyoruz
        if description_index < len(card_description):
            print(f"Açıklama: {card_description[description_index].text.strip()}\n")
            description_index += 1
