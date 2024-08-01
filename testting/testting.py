import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

ser=Service("./chromedriver.exe") 
driver=webdriver.Chrome(service=ser)
driver.get("web sitesi adresi")
iletisim=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div/div/div/section[14]").click()
ad="asfdsgfhgjgkhkj"
site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[1]/label/span/input").send_keys(ad)
print(ad)
mail="1122256 et gmail.com"
mail_düzenleme=mail
son_et=mail_düzenleme.rfind("et")
mail_düzenleme = (mail_düzenleme[:son_et].strip() + "@" + mail_düzenleme[son_et+2:].strip())
site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/input").send_keys(mail_düzenleme)
print(mail_düzenleme)
telefon="342567"
site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[3]/label/span/input").send_keys(telefon)    
print(telefon)
ileti="sadsasfasfsdfa "
site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/textarea").send_keys(ileti)
print("From gönderiliyor")
site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[5]/input").click()
time.sleep(5)
##hata kontrol kısmı

## genel hata kontrolü
mesaj=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/div[2]")
time.sleep(3)
## ileti dogru iletildiyse
iletildi=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/div[2]")
time.sleep(3)
## ad kısmındaki boşluk hatası 
mesaj1=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div/div/div/section[14]/div/div/div/div/div/section/div/div/div[2]/div/div/div/div/div/div/form/p[1]/label/span/span")
time.sleep(3)
## e posta kısmındaki boşluk hatası
mesaj2=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/span")
time.sleep(3)
## ileti kısmındaki boşluk hatası
mesaj3=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/span")
time.sleep(3)
##geçersiz mail hata mesajı
mail_Hata=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/span")
time.sleep(3)
## tüm alan boşsa
if mesaj1 and mesaj2 and mesaj3 in "Bu alan zorunludur." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("alan boş hataları doğru çalışıyor")
else:
    print ("Alan boş hataları hatalı çalışıyor")

## ad ksmı dolu diğerleri boşsa
if  mesaj2 and mesaj3 in "Bu alan zorunludur." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("alan boş hataları doğru çalışıyor")
else:
    print ("Alan boş hataları hatalı çalışıyor")

## sadece ileti kısmı boşsa
if   mesaj3 in "Bu alan zorunludur." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("alan boş hataları doğru çalışıyor")
else:
    print ("Alan boş hataları hatalı çalışıyor")

## mail kısmı hatalıysa 

if   mail_Hata in "Girilen e-posta adresi geçersiz." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("Geçersiz mail kısmı doğru çalışıyor")
else:
    print ("Geçersiz mail kısmı hatalı çalışıyor")

## mail kısmı hatalı ad kısmı boşsa

if mesaj1 in "Bu alan zorunludur." and mail_Hata in "Girilen e-posta adresi geçersiz." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("Geçersiz mail kısmı doğru çalışıyor")
else:
    print ("Geçersiz mail kısmı hatalı çalışıyor")

##  mail kısmı hatalı ileti kısmı boşsa

if mesaj3 in "Bu alan zorunludur." and mail_Hata in "Girilen e-posta adresi geçersiz." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("Geçersiz mail kısmı doğru çalışıyor")
else:
    print ("Geçersiz mail kısmı hatalı çalışıyor")

## mail geçersiz diğer alanlar boşsa


if   mesaj1 and mesaj3 in "Bu alan zorunludur." and mail_Hata in "Girilen e-posta adresi geçersiz." and mesaj in "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin.":
    print("Geçersiz mail kısmı doğru çalışıyor")
else:
    print ("Geçersiz mail kısmı hatalı çalışıyor")

## ileti dogruysa
if  iletildi in "Mesajınız bize ulaştı. En kısa sürede dönüş sağlayacağız.":
    print("alan boş hataları doğru çalışıyor")
else:
    print ("Alan boş hataları hatalı çalışıyor")










