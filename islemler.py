from urllib.parse import urlencode
from urllib.request import urlopen, Request, URLError, HTTPError
from json import loads
import google
from googlesearch import search
from googletrans import Translator
from bs4 import BeautifulSoup

def info():  # info en basa terefe kececekdir :)
    print("""
        \33[32m\33[1m

                   .-:-.`                             
               `:+o/.                                 
             -+oo+.       ..`                         
           -oooo-     `-/:`      ``                   
         `+soso.    `:o/`     `. ```:.  `             
        .ososo.    .oo:        .      `/o-            
       -ossos-    .os+         `.       .` `          
      .oosooo    `ooo-            `--    `/.          
      +sssss/    -soo.        `-/ooo`     `-          
     .ssssso:    :soo-    .-/ososso- ..   ``          
     :sossso/    :ooo+.:+ooo+/--oo/    ````    `      
     /sssssso`   .osssso+:.`  `+oo`           .-      
     :ossssss:    /o/:.       :oo-           -+`      
     .oosssoso.              .os/          .+o.    `  
      +ssssssso.             +so`      `-/os+`    `:  
      .ossssssso:           :soo+++++ooooo+-     .+.  
       -ossssssos+.        .ossssoooso+/-`     `/o-   
        -osssssssss+-`      `.......`        ./oo-    
         .+sssssssssoo/-.                `-/ooo+.     
          `:ososssssssssso+/:-......--:/oossoo-       
            `:oossssssssssssssssosossssosos+-`        
               .:+oossssssssssssssssssso+:.           
                  `-:+oooosssssooooo/:-`              
                        `..----..`  \33[0m

        \33[32m\33[1m[\33[0m     \33[32m\33[1m\33[5mCyber-Warrior.org | Lojistik Group\33[0m     \33[32m\33[1m] \33[0m           

    \33[31m\33[1m\33[3mInformation...\33[0m 

    \33[32m\33[1m [>] Coded by : \33[0m Mikayil Ilyasov (QARAKURT)
    \33[32m\33[1m [>] Contact  : \33[0m illegal_coder[at]protonmail.com
    \33[32m\33[1m [>] Website  : \33[0m Cyber-Warrior.org | Turkish Cyber Army
    \33[32m\33[1m [>] Yasal uyari : \33[0m Bu yazilim tamamen Cyber-Warrior.org icin kodlanmistir. Izinsiz kullanim ve github kimi platformlarda paylasilmasi Yasakdir.
    \33[32m\33[1m [>] Our mission  : \33[0m https://www.cyber-warrior.org/Misyon.asp
    \33[32m\33[1m [>] Message to all : \33[0mNe mutlu Turkum diyene! Respects to all \33[4mTurkish\33[0m and \33[4mAzerbaijani\33[0m hackers. 
    \33[32m\33[1m [>] Loves    : \33[0m To \33[37m\33[1m\33[33m GALATA\33[31mSARAY

    \33[31m*******************************************************************\33[0m""")


# Reverse domain islemi
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
url = 'https://domains.yougetsignal.com/domains.php'


class reverse_ip(object):
    # Kimsenin hakkina girilmez. Bu class (reverse_ip) icindeki kodlarin bir kismi alintidir.
    # Acik kaynak kutuphaneleri kullanilmis, ve uzerinde gerekli duzenlemeler aparilmisdir.

    def __init__(self, domain):
        self.domain = domain
        self.check()

    def check(self):
        values = urlencode({'remoteAddress': self.domain, 'key': ''}).encode('utf-8')
        try:
            req = Request(url, values, header)
            res = urlopen(req)
        except HTTPError:
            exit('HTTP Error')
        except URLError:
            exit('URL Error')
        else:
            self.data = loads(res.read())

    def info(self):
        if self.data['status'] != 'Success':
            if "Invalid remote address." in self.data['message']:
                print('\33[31m Biseyler yanlis gitti...\33[0m ')
                print('\33[1m Hata mesaji : Yazilan domain adressi hatali.\33[0m ')
                print("\33[31m*****************************************\33[0m ")
            exit()
        else:
            print('\33[1m\33[91mDomain:\33[0m ' + self.data['remoteAddress'])
            print('\33[1m\33[91mIp:\33[0m ' + self.data['remoteIpAddress'])
            print('\33[1m\33[91mToplam domain:\33[0m ' + str(self.data['domainCount']) + '\n')

            for domain in self.data['domainArray']:
                print(domain[0])
                file = open("ips.txt", "a", encoding="utf-8")
                file.write(domain[0]+"\n")
                file.close()
            print("\n Dosya ips.txt Kaydedildi...")



# Domain search
def rev_ip(domain):
    result = reverse_ip(domain)

    result.info()



# Google search domain
def cw(a=None, b=None, o=None):
    # Klons'un hayelleri
    query = "site:" + a
    print("\33[1m Arama baslatildi !\33[0m ")
    print("\33[31m\33[1m sorgu :\33[0m  {}".format(query))
    print("\33[31m*****************************************\33[0m ")

    def terc(a):
        translator = Translator()
        tr1 = translator.translate(a, dest='tr')
        return tr1.text

    for i in search(query, num=int(b)+1, stop=int(b)+1, pause=5, verify_ssl=True):
        while i:
            site = Request(i, headers=header)
            page = urlopen(site)
            html = BeautifulSoup(page.read().decode(encoding="utf-8"), "html.parser")
            metatags = html.find_all('meta', attrs={'name': 'description'})
            for j in metatags:
                ti = html.find_all('title')
                tit = str(ti[0]).replace('<title>', '').replace('</title>', '')
                titlemiz = terc(tit)
                conte = j.get('content')
                contentimiz = str(terc(conte))
                print("""\33[1m\33[92m[>]\33[0m\33[1m site :\33[0m {}				
\33[1m\33[92m[>]\33[0m\33[1m title :\33[0m {}
\33[1m\33[92m[>]\33[0m\33[1m content :\33[0m {}
\33[1m\33[31m*****************************************	""".format(i, titlemiz, contentimiz))
                if o is not None:
                    file = open(o, "a", encoding="utf-8")
                    file.write("""
[>] site : {}				
[>] title : {}
[>] content : {}
*****************************************	""".format(i, titlemiz, contentimiz))
                    file.close()
                    
            break


def keywd(kelime=None, b=None, o=None):
    if kelime and b :
        query = "link:" + kelime + " -wikipedia.org -en.wikipedia.org -youtube.com -facebook.com -twitter.com"  
        print('\33[1m\33[91mTarama baslatildi...\33[0m')
        print("\33[1m\33[91msorgu : \33[0m" + kelime)
        print("\33[1m\33[42m*****************************************\33[0m"+"\n")
        for i in search(query, num=int(b), stop=int(b), pause=5, verify_ssl=True):
            print(i)
            
            if o is not None:
                file = open(o, "a", encoding="utf-8")
                file.write(""""
Kaydedildi
*****************************************
{}
                """.format(i))
        print("\33[1m Tarama bitdi...\33[0m")


def help():
    print("""
\33[31m\33[1m\33[3mKullanim klavuzu\33[0m

\33[1mBilgilendirme :\33[0m
    \33[32m-c (--command=) : \33[0m Bu komut gerekli diger fonksiyon ve parametreleri calistirmak icin kullanilir
        \33[32mYardim : \33[0m Yardim al : python3 cwint.py -c help ve ya python3 cwint.py -c h
        \33[32mInfo : \33[0m Yazilim bilgilendirmesi : python3 cwint.py -c info ve ya python3 cwint.py -c i
        
    \33[1mKullanim ornegi:\33[0m
    python3 cwint.py -c help (h da kullanila bilinir)
    ve ya  python3 cwint.py --command=help  

\33[1mReverse ip :\33[0m
    \33[32m-d (--domain=) : \33[0m parametre sonuna gerekli sitenin domainini ve ya IP adressini ekleyin [-d cyber-warrior.org]
   
    \33[1mKullanim ornegi :\33[0m
    python3 cwint.py -d google.com
    python3 cwint.py --domain=google.com

\33[1mGoogle detayli domain tarama :\33[0m
    \33[32m-t (--target=) : \33[0m listelemek istediginiz domain uzantisini belirleyin.[-t gov.gr]
    \33[32m-s (--sayi=) : \33[0m Almak istediginiz sonuc sayinizi yazin. [-s 20] \33[31m*\33[0m
    \33[32m-o (--output=) : \33[0m Alinan sonuclari dosya gibi saklayin [-o dosyaismi.txt] \33[31m*\33[0m

    \33[1mKullanim ornegi :\33[0m
    python3 cwint.py -t [hedef_domain] -s [sayi] -o [sonuc.txt]
    ve ya python3 cwint.py --target=[hedef_domain] --sayi=[sayi] --output=[sonuc.txt]

\33[1mgoogle anahtar kelime ile tarama :\33[0m
    \33[32m-k (--kelime=) : \33[0m Taramak istediginiz kelimeni ekleyin [-k Akincilar]
    \33[32m-s (--sayi=) : \33[0m Almak istediginiz sonuc sayinizi yazin.  [-s 20] 
    \33[32m-o (--output=) : \33[0m Alinan sonuclari dosya gibi saklayin [-o dosyaismi.txt] \33[31m*\33[0m
    
    \33[1mKullanim ornegi :\33[0m
    python3 cwint.py -k [cyber-warrior] -s [20] -o [sonuc.txt] 
    ve ya python3 cwint.py --kelime=[cyber-warrior] --sayi=[20] --output=[sonuc.txt]
    
    \33[1m\33[31mOnemli not:\33[0m karsisinda \33[31m*\33[0m olan tum parametreler  yazilmadan da program calisacaktir. Detayli inceleme icin not dosyasina goz atin
*******************************************************************\33[0m 


""")
