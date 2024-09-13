import bs4 as bs
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
URL="https://www.trendyol.com/apple/iphone-11-64-gb-beyaz-cep-telefonu-aksesuarsiz-kutu-apple-turkiye-garantili-p-65149494"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
sayfa=requests.get(URL,headers=headers)
icerik=BeautifulSoup(sayfa.text,"html.parser")
#print(icerik)
urun_ad = icerik.find("h1", class_="pr-new-br").find("span").get_text()
print(urun_ad)
urunF=icerik.find(class_="prc-dsc").get_text().replace(".","").replace(",",".").replace("TL","")
print(urunF)
urunFF=float(urunF)
if urunFF <= 23498:
    print(f"Fiyat Düştü: {float(urunFF)}")
    mesaj="Fiyat Düştü".format(urunFF)
elif urunFF == 23499:
    print(f"Fiyat Aynı: {float(urunFF)}")
    mesaj="Fiyat Aynı".format(urunFF)
else:
    print(f"Fiyat Arttı: {float(urunFF)}")
    mesaj = "Fiyat Arttı".format(urunFF)


