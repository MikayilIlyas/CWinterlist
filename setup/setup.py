import os 
import sys

print("""
********************************************************************
Yazilimda kullanilar modul ve kutuphaneler bilgisayarinizda kurulu olmaya bilir. 
bu yuzden setup.py dosyasi bu kurulumu sizin icin yapacaktir. 
Bu islemler Linux (Kali, Ubuntu, Debian) uzerinde denenmistir. 
********************************************************************""")

haziriz = input("Kurulumlari kurmaya hazirmisiniz? E/h : ")

if haziriz == "e" or haziriz == "E" :
    print("kurulumlar baslatildi")
    print("--------------------------------------")
    os.system('sudo apt install python3-pip')
    os.system('pip3 install requests')
    os.system('pip3 install loads')
    os.system('pip3 install beautifulsoup4')
    os.system('pip3 install google-search')
    os.system('pip3 install googletrans2')
    os.system('pip3 install google')
    os.system('pip3 install googletranslate')   
    os.system('pip3 install pip install googletrans==3.1.0a0')
    os.system('pip3 install -r requirements.txt')
    os.system('clear')
    print("------------------------------------")
    print('kurulum basariyla tamamlandi')
    


else :
    print("Kurulum basarisiz")

