import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import socket
import time
import sys

log_path = "C:\\Users\\emre\\Desktop\\yazilar\\startup_log.tx"
sys.stdout = open(log_path, "a")
sys.stderr = sys.stdout

print("\n--- Script Başladı ---")
print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def wait_for_network(timeout=60):
    start = time.time()
    while time.time() - start < timeout:
        try:
            # Google DNS'e ping gibi: ağ varsa çalışır
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            time.sleep(2)
    return False

if wait_for_network():
    print("Ağ bağlantısı kuruldu, e-posta gönderiliyor.")
else:
    print("Ağ bağlantısı kurulamadı, e-posta gönderilmeyecek.")
    exit()

# Ayarlar
gmail_user = 'beyy58097@gmail.com'
gmail_password = 'ftad scpz mqeo dulj'  # Normal şifre değil! Uygulama şifresi kullan.
to = 'yemre_8@hotmail.com'

# Sistem bilgisi
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Mail içeriği
subject = f"[BİLGİSAYAR AÇILDI] - {hostname}"
body = f"""
Bilgisayar açıldı!

Tarih/Saat: {zaman}
Kullanıcı: {hostname}
IP Adresi: {ip_address}
"""

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = gmail_user
msg['To'] = to

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, msg.as_string())
    server.quit()
    print("E-posta gönderildi.")
except Exception as e:
    print("E-posta gönderilemedi:", str(e))
