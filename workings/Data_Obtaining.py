import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# BBC'den veri çek
r = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(r.text, 'html.parser')

headlines = soup.find('body').find_all('h2')
card_description = soup.find('body').find_all('p')

# Veritabanı bağlantısı
conn = sqlite3.connect("bbc_news.db")
cursor = conn.cursor()

# Tablo oluştur (varsa tekrar oluşturmaz)
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT,
    description TEXT,
    scraped_at TEXT
)
""")

# Veri ekleme
description_index = 0
for headline in headlines:
    title = headline.text.strip()
    desc = ""
    if 'card_headline' not in headline.get('class', []):
        if description_index < len(card_description):
            desc = card_description[description_index].text.strip()
            description_index += 1
    
    # Veritabanına ekle
    cursor.execute("INSERT INTO news (headline, description, scraped_at) VALUES (?, ?, ?)", 
                   (title, desc, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

conn.commit()

print("✅ Veriler SQLite veritabanına kaydedildi.\n")
