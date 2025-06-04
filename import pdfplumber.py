import pdfplumber
import pandas as pd
import re


def extract_table_data(pdf_path, keywords):
    
    extracted_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Tabloyu PDF'den çıkar
            tables = page.extract_tables()
            for table in tables:
                # Her tabloyu bir DataFrame'e dönüştür
                df = pd.DataFrame(table)
                
                # Anahtar kelimelerle eşleşen satırları filtrele
                for keyword in keywords:
                    filtered_rows = df.applymap(lambda x: bool(re.search(keyword, str(x), re.IGNORECASE)))
                    if filtered_rows.any().any():
                        # Eşleşen satırları kaydet
                        extracted_data.append(df[filtered_rows.any(axis=1)])
    
    # Tüm verileri birleştir
    if extracted_data:
        result = pd.concat(extracted_data, ignore_index=True)
    else:
        result = pd.DataFrame()
    
    return result

# Kullanım
pdf_path_2023 = "C:/Users/Emre/OneDrive/Desktop/working/27101748_2023ylsytercihtablosuguncel.pdf"
pdf_path_2024 = "C:/Users/Emre/OneDrive/Desktop/working/2024ylsytercihtablosu.pdf"
keywords = ["Elektrik Elektronik Mühendisliği", "toplam kontenjan"]

# 2023 PDF dosyasını analiz et
data_2023 = extract_table_data(pdf_path_2023, keywords)
print("2023 Verileri:")
print(data_2023)

# 2024 PDF dosyasını analiz et
data_2024 = extract_table_data(pdf_path_2024, keywords)
print("2024 Verileri:")
print(data_2024)
