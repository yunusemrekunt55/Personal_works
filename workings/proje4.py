import serial
import time
import requests

# ESP32 seri port bağlantısı
ser = serial.Serial('COM3', 115200, timeout=1)

# Google Web App URL'in
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbxRM1pxc3AkRvm7f_qumRJrHREJiZHJbG4aYqLJUIQNtzrw2lzp6GPZT25j_ubZ6ph5zw/exec"

def veriyi_ayristir(line):
    try:
        if "Sensor 1:" in line:
            return "soil1", int(line.split(":")[1].strip())
        elif "Sensor 2:" in line:
            return "soil2", int(line.split(":")[1].strip())
        elif "Sensor 3:" in line:
            return "soil3", int(line.split(":")[1].strip())
        elif "Sensor 4:" in line:
            return "soil4", int(line.split(":")[1].strip())
        elif "Sensor 5:" in line:
            return "soil5", int(line.split(":")[1].strip())
        elif "Sensor 6:" in line:
            return "soil6", int(line.split(":")[1].strip())
        elif "Yağmur Durumu:" in line:
            return "rain", 1 if "YAĞIYOR" in line else 0

        elif "Sıcaklık:" in line:
            return "temp", float(line.split(":")[1].replace("°C", "").strip())
        elif "Nem:" in line:
            return "humidity", float(line.split(":")[1].replace("%", "").strip())
        elif "Su Akış 1" in line:
            return "flow1", float(line.split(":")[1].replace("L/dk", "").strip())
        elif "Su Akış 2" in line:
            return "flow2", float(line.split(":")[1].replace("L/dk", "").strip())
        elif "Su Akış 3" in line:
            return "flow3", float(line.split(":")[1].replace("L/dk", "").strip())
        elif "Röle 1 Durum:" in line:
            return "relay1", int(line.split(":")[1].strip())
        elif "Röle 2 Durum:" in line:
            return "relay2", int(line.split(":")[1].strip())
        elif "Röle 3 Durum:" in line:
            return "relay3", int(line.split(":")[1].strip())

    except:
        return None, None

    return None, None




while True:
    payload = {
    "soil1": None, "soil2": None, "soil3": None,
    "soil4": None, "soil5": None, "soil6": None,
    "rain": None, "temp": None, "humidity": None,
    "flow1": None, "flow2": None, "flow3": None,
    "relay1": None, "relay2": None, "relay3": None
}


    start_time = time.time()

    while time.time() - start_time < 5:  # 5 saniyede veri bloğu oku
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        key, value = veriyi_ayristir(line)
        if key:
            payload[key] = value

    if all(v is not None for v in payload.values()):
        response = requests.post(GOOGLE_SHEET_URL, json=payload)
        print("✅ Veri gönderildi:", payload)
    else:
        print("⚠️ Eksik veri atlandı:", payload)

    time.sleep(30)  # 30 saniyede bir gönder
