import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
from collections import Counter

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


conn = sqlite3.connect("bbc_news.db")
cursor = conn.cursor()

print("📊 En uzun başlık:")
cursor.execute("SELECT headline, LENGTH(headline) as len FROM news ORDER BY len DESC LIMIT 1")
print(cursor.fetchone())

print("\n📌 En sık tekrar eden başlıklar:")
cursor.execute("""
SELECT headline, COUNT(*) as count 
FROM news 
GROUP BY headline 
HAVING count > 1 
ORDER BY count DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n📅 Tarihe göre haber gruplama:")
cursor.execute("""
SELECT DATE(scraped_at) as tarih, COUNT(*) as adet 
FROM news 
GROUP BY tarih
""")
for row in cursor.fetchall():
    print(row)

# Kelime sıklığı analizi (basit örnek)


cursor.execute("SELECT headline FROM news")
headlines = [row[0] for row in cursor.fetchall()]
words = " ".join(headlines).lower().split()
word_freq = Counter(words)

print("\n🔠 En çok geçen kelimeler (ilk 10):")
for word, count in word_freq.most_common(10):
    print(f"{word}: {count}")
