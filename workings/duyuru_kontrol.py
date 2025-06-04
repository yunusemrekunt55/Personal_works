import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os

# Duyuruları saklamak için dosya adımız
FILE_NAME = "previous.txt"

# Web sitesinden duyuruları al
def get_current_announcements():
    url = "https://ee.mu.edu.tr/"  # URL'yi kendine göre güncelle
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 'duyuru_baslik' sınıfına sahip tüm duyuruları al
    announcements = soup.find_all('div', class_='duyuru_baslik')
    return [a.text.strip() for a in announcements]

# Daha önceki duyuruları dosyadan oku
def load_previous_announcements():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []

# Şu anki duyuruları dosyaya yaz
def save_current_announcements(announcements):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for ann in announcements:
            f.write(ann + "\n")

# Yeni duyuru varsa e-posta gönder
def send_email(new_announcements):
    sender_email = "beyy58097@gmail.com"
    sender_password = "uico ihqn bnsc ocds"
    recipient_email = "yunusemrekunt@posta.mu.edu.tr"

    subject = "Yeni Duyuru(lar) Var!"
    body = "Yeni duyurular:\n\n" + "\n".join(new_announcements)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Yeni duyuru bulundu ve e-posta gönderildi.")

# Ana kontrol fonksiyonu
def main():
    current = get_current_announcements()
    previous = load_previous_announcements()

    # Yeni olanları bul
    new_announcements = [ann for ann in current if ann not in previous]

    if new_announcements:
        send_email(new_announcements)
        save_current_announcements(current)
    else:
        print("Yeni duyuru yok.")

# Çalıştır
if __name__ == "__main__":
    main()
