# CWinterlist
 Cyber-Warrior.org

 > Her seyin bir baslangici

ilk once setup klasoru dahilinde 'setup.py' dosyasini calistirip gerekli kurulumlarin kurulmasini gerceklestirmelisiniz. 

komut : 
    cd setup
    python3 setup.py

-yazilimi kotuye kullanip da misyonumuzu bozan insanlara,
-Bu vatanin bu topragin ekmegin yeyip ihanet askiyla yananlara
-Ve tum hainlere...
KESINLIKLE HAKKIMI   H E L A L  E T M I Y O R U M !!!

Kullanim klavuzu

Bilgilendirme :
    -c (--command=) :  Bu komut gerekli diger fonksiyon ve parametreleri calistirmak icin kullanilir
        Yardim :  Yardim al : python3 cwint.py -c help ve ya python3 cwint.py -c h
        Info :  Yazilim bilgilendirmesi : python3 cwint.py -c info ve ya python3 cwint.py -c i
        
    Kullanim ornegi:
    python3 cwint.py -c help (h da kullanila bilinir)
    ve ya  python3 cwint.py --command=help  

Reverse ip :
    -d (--domain=) :  parametre sonuna gerekli sitenin domainini ve ya IP adressini ekleyin [-d cyber-warrior.org]
   
    Kullanim ornegi :
    python3 cwint.py -d google.com
    python3 cwint.py --domain=google.com

Google detayli domain tarama :
    -t (--target=) :  listelemek istediginiz domain uzantisini belirleyin.[-t gov.gr]
    -s (--sayi=) :  Almak istediginiz sonuc sayinizi yazin. [-s 20] *
    -o (--output=) :  Alinan sonuclari dosya gibi saklayin [-o dosyaismi.txt] *

    Kullanim ornegi :
    python3 cwint.py -t [hedef_domain] -s [sayi] -o [sonuc.txt]
    ve ya python3 cwint.py --target=[hedef_domain] --sayi=[sayi] --output=[sonuc.txt]

google anahtar kelime ile tarama :
    -k (--kelime=) :  Taramak istediginiz kelimeni ekleyin [-k Akincilar]
    -s (--sayi=) :  Almak istediginiz sonuc sayinizi yazin.  [-s 20] 
    -o (--output=) :  Alinan sonuclari dosya gibi saklayin [-o dosyaismi.txt] *
    
    Kullanim ornegi :
    python3 cwint.py -k [cyber-warrior] -s [20] -o [sonuc.txt] 
    ve ya python3 cwint.py --kelime=[cyber-warrior] --sayi=[20] --output=[sonuc.txt]
    
    Onemli not: karsisinda * olan tum parametreler  yazilmadan da program calisacaktir. Detayli inceleme icin not dosyasina goz atin
*******************************************************************