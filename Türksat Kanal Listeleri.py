from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Driver yolu giris
browser = webdriver.Edge('msedgedriver.exe')

# Site giris
browser.get("https://uydu.turksat.com.tr/tr/turksat-frekans-listesi")
time.sleep(10)


# Listeyi bul
Kanal_Adi = browser.find_elements(By.CLASS_NAME, 'channel-name')
Kanal_Format = browser.find_elements(By.CLASS_NAME, 'channel-format')
Kanal_Frekans =browser.find_elements(By.CLASS_NAME, 'cell-frekans')
Kanal_Polarizasyon = browser.find_elements(By.CLASS_NAME, 'cell-polarizasyon')
Kanal_Kapsama = browser.find_elements(By.CLASS_NAME, 'cell-kapsama')
Kanal_SR = browser.find_elements(By.CLASS_NAME, 'cell-sembolOrani')
Kanal_FEC = browser.find_elements(By.CLASS_NAME, 'cell-FEC')
Kanal_V_PID = browser.find_elements(By.CLASS_NAME, 'cell-videoPid')
Kanal_A_PID = browser.find_elements(By.CLASS_NAME, 'cell-audioPid')
Kanal_Uydu = browser.find_elements(By.CLASS_NAME, 'cell-uydu')
time.sleep(5)



# Dosya adı
filename = 'turksat_frekans_listesi.txt'

# Verileri dosyaya kaydet
with open(filename, 'w') as file:
    for i in range(len(Kanal_Adi)):
        if "HD" in Kanal_Adi[i].text:
            file.write(Kanal_Adi[i].text.replace('HD', '') + '\t\t' +
                       Kanal_Format[i].text + '\t' +
                       Kanal_Frekans[i].text + '\t' +
                       Kanal_Polarizasyon[i].text + '\t' +
                       Kanal_Kapsama[i].text + '\t' +
                       Kanal_SR[i].text + '\t' +
                       Kanal_FEC[i].text + '\t' +
                       Kanal_V_PID[i].text + '\t' +
                       Kanal_A_PID[i].text + '\t' +
                       Kanal_Uydu[i].text + '\n')
            print(Kanal_Adi[i].text.replace('HD', ''), Kanal_Format[i].text, Kanal_Frekans[i].text, Kanal_Polarizasyon[i].text, Kanal_Kapsama[i].text, Kanal_SR[i].text, Kanal_FEC[i].text, Kanal_V_PID[i].text, Kanal_A_PID[i].text, Kanal_Uydu[i].text)
        else:
            file.write(Kanal_Adi[i].text + '\t' +
                       Kanal_Format[i].text + '\t' +
                       Kanal_Frekans[i].text + '\t' +
                       Kanal_Polarizasyon[i].text + '\t' +
                       Kanal_Kapsama[i].text + '\t' +
                       Kanal_SR[i].text + '\t' +
                       Kanal_FEC[i].text + '\t' +
                       Kanal_V_PID[i].text + '\t' +
                       Kanal_A_PID[i].text + '\t' +
                       Kanal_Uydu[i].text + '\n')
            print(Kanal_Adi[i].text, Kanal_Format[i].text, Kanal_Frekans[i].text, Kanal_Polarizasyon[i].text, Kanal_Kapsama[i].text, Kanal_SR[i].text, Kanal_FEC[i].text, Kanal_V_PID[i].text, Kanal_A_PID[i].text, Kanal_Uydu)
                
