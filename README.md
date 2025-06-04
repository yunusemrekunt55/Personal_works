# 📰 1- Data_Obtaining.py
 I use bs4 for obtaining html values from a website in this project it is BBC News. By the way I am able to access breaking news as titles and subtitle.

# 🔐 2- K_log_v2.py
 I created a python code which recording the pushed button on the keyboard.

# 🎓 3- duyuru_kontrol.py 📢

A Python script to monitor university announcements and send email notifications if there are new updates.

## 🔍 Features

- 🕒 Checks if updates exist on the university website
- 📬 Sends email notifications when new announcements are found
- 📄 Logs activity with timestamps by using Windows Task Scheduler

# 4- 📝 PDF_manipulator.py
- Python script to extract and filter table data from PDF files using specific keywords. It uses pdfplumber to extract tables and pandas to organize and filter the results. This example focuses on retrieving rows related to "Electrical and Electronics Engineering" and "total quota" from 2023 and 2024 university placement documents.

## 🔍 Key Features:

  --Extracts tables from PDF files page by page

  --Filters rows based on given keywords (case-insensitive)

  --Combines filtered rows from all pages into a single DataFrame

  --Supports comparison across different years (e.g., 2023 vs 2024)

# 5- 🌻 proje4.py
- This Python script reads real-time sensor data from an ESP32 device via serial communication and sends it to a Google Sheet using a Web App URL. It collects data such as soil moisture levels, rain detection, temperature, humidity, water flow, and relay statuses, and sends a JSON payload every 30 seconds if all values are complete.

## 🔍 Key Features:

--Reads sensor data from ESP32 through the serial port (e.g., COM3)

--Parses lines based on expected sensor output format

--Supports multiple soil sensors, temperature, humidity, rain sensor, water flow sensors, and relays

--Sends the parsed data as JSON to a Google Sheets Web App endpoint

--Skips sending data if any field is missing to avoid partial/inaccurate records

# 🔑 securitymessage.py

-A lightweight Python script that sends an email notification when the computer boots up. It includes the machine's hostname, IP address, and the current timestamp. Useful for remote monitoring, server uptime tracking, or just keeping logs of machine startups.

## 🔍 Features
--Waits for internet connection before attempting to send

--Logs activity to a local .txt file

--Sends email via Gmail SMTP with:

--Hostname

--Local IP Address

--Current date and time
