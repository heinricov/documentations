import network
import time
import machine
import dht
import urequests
import json
import os

# -------------------------------
# Konfigurasi WiFi & API
# -------------------------------
SSID = 'Wokwi-GUEST'           # Ganti dengan SSID kamu
PASSWORD = ''                  # Password kosong untuk Wokwi-GUEST
API_URL = 'https://terra369.vercel.app/api/dth22'  # Ganti URL ini
UNIT_NAME = 'Unit-01'
MAX_LOG_SIZE = 10

# -------------------------------
# Koneksi ke WiFi (versi diperbarui)
# -------------------------------
def connect_wifi():
    print("Connecting to WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        sta_if.connect(SSID, PASSWORD)
        retry = 0
        while not sta_if.isconnected() and retry < 50:
            print(".", end="")
            time.sleep(0.1)
            retry += 1
    if sta_if.isconnected():
        print(" Connected!")
        print("IP:", sta_if.ifconfig()[0])
        return True
    else:
        print(" Failed!")
        return False

# -------------------------------
# Simpan data offline
# -------------------------------
def simpan_offline(data):
    try:
        log = []
        if "log_offline.jsonl" in os.listdir():
            with open("log_offline.jsonl", "r") as f:
                log = f.readlines()
        if len(log) < MAX_LOG_SIZE:
            with open("log_offline.jsonl", "a") as f:
                f.write(json.dumps(data) + "\n")
            print("Data disimpan offline.")
        else:
            print("File log penuh, data tidak disimpan.")
    except Exception as e:
        print("Gagal simpan offline:", e)

# -------------------------------
# Kirim data ke API
# -------------------------------
def kirim_data(data):
    headers = {"Content-Type": "application/json"}
    try:
        response = urequests.post(API_URL, headers=headers, data=json.dumps(data))
        print("Status:", response.status_code)
        print("Respon:", response.text)
        response.close()
        return True
    except Exception as e:
        print("Gagal kirim API:", e)
        return False

# -------------------------------
# Sinkronisasi data offline
# -------------------------------
def sinkron_offline():
    if "log_offline.jsonl" not in os.listdir():
        return
    try:
        with open("log_offline.jsonl", "r") as f:
            lines = f.readlines()

        success_count = 0
        for line in lines:
            try:
                data = json.loads(line)
                if kirim_data(data):
                    success_count += 1
                else:
                    break
            except:
                continue

        if success_count == len(lines):
            os.remove("log_offline.jsonl")
            print("Semua data offline berhasil disinkron.")
        else:
            with open("log_offline.jsonl", "w") as f:
                for line in lines[success_count:]:
                    f.write(line)
            print(f"{success_count} data offline terkirim, sisanya tersimpan.")
    except Exception as e:
        print("Gagal sinkron offline:", e)

# -------------------------------
# Loop utama
# -------------------------------
def main():
    online = connect_wifi()
    sensor = dht.DHT22(machine.Pin(14))

    if online:
        sinkron_offline()

    while True:
        try:
            sensor.measure()
            suhu = sensor.temperature()
            kelembapan = sensor.humidity()
            data = {
                "unit_name": UNIT_NAME,
                "suhu": suhu,
                "kelembapan": kelembapan
            }
            print("Data:", data)

            if connect_wifi():
                if kirim_data(data):
                    sinkron_offline()
                else:
                    simpan_offline(data)
            else:
                simpan_offline(data)

        except OSError as e:
            print("Gagal baca sensor:", e)

        time.sleep(10)

main()
