import datetime
import sys
import os
import getopt
import requests
import islemler


# Cyber-Warrior icin QARAKURT tarafindan kodlanmistir.

def operation():
    banner = """\33[31m \33[1m 
   _______       __   _       __            ___      __ 
  / ____/ |     / /  (_)___  / /____  _____/ (_)____/ /_
 / /    | | /| / /  / / __ \/ __/ _ \/ ___/ / / ___/ __/
/ /___  | |/ |/ /  / / / / / /_/  __/ /  / / (__  ) /_  
\____/  |__/|__/  /_/_/ /_/\__/\___/_/  /_/_/____/\__/                                      
                                \33[5m                
[!] \33[0m Cyber-Warrior.org | Lojistik grup \33[31m \33[5m  \33[1m 

[!] \33[0m Mikayil Ilyasov (QARAKURT)    \33[31m \33[5m \33[1m 

[!] \33[0m parametreler ve detaylar icin -c h kullaniniz     \33[0m                                                                                                                                                                            
\33[91m*******************************************************************
\33[0m \33[1m \33[31m\33[0m """
    t = None  # target reverse ip
    d = None  # domain advanced scan
    o = None  # output
    c = None  # command
    k = None  # keyword
    s = None  # gosterilen sayisi

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "t:d:o:c:k:s:",
                                   ["target=", "domain=", "output=", "kelime=", "command=", "sayi="])
    except getopt.GetoptError as error:
        print(banner, "\n", error, """
        
    Parametre hatasi! Lutfen \33[31m python3 cwint.py -c h\33[0m komutu ile yardim almaya ne dersin? ;)
        """)

        sys.exit()

    for opt, arg in opts:
        if opt in ['-t', '--target']:
            t = arg
        elif opt in ['-d', '--domain']:
            d = arg
        elif opt in ['-o', '--output']:
            o = arg
        elif opt in ['-c', '--command']:
            c = arg
        elif opt in ['-k', '--kelime']:
            k = arg
        elif opt in ['-s', '--sayi']:
            s = arg
   # komut islemleri
    if c == "i" or c == "info":
        islemler.info()
        sys.exit()
    elif c == "h" or c == "help":
        islemler.help()
        sys.exit()

    # reverse ip 
    print(banner)
    if d:
        islemler.rev_ip(d)
    # google detayli domain arama
    if t:
        islemler.cw(t, s, o)

    # google anahtar kelime ile tarama
    if k:
        islemler.keywd(k, s, o)


operation()
