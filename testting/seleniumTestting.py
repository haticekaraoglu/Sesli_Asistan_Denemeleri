from selenium.webdriver.chrome.service import Service
from selenium import webdriver


ser=Service("./chromedriver.exe") 
driver=webdriver.Chrome(service=ser)

driver.get("https://www.google.com.tr")
link=driver.current_url
baslık=driver.title
if "google.com" in link:
  print ("google başarılı bi şekilde açıldı") 
  driver.maximize_window()

driver.get("https://drive.google.com/")
link=driver.current_url
baslık=driver.title
if "drive.google.com" in link:
  print ("drive başarılı bi şekilde açıldı") 
  driver.maximize_window()

driver.get("https://mail.google.com")
link=driver.current_url
baslık=driver.title
if "mail.google.com" in link:
  print ("mail başarılı bi şekilde açıldı") 
  driver.maximize_window()

driver.get("https://aaaa.com/")
link=driver.current_url
baslık=driver.title
if "aaaa.com" in link:
  print ("aaaa web sayfası başarılı bi şekilde açıldı") 
  driver.maximize_window()

driver.quit()
 




 

"""
#genel mesaj

mesaj=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/div[2]")
#ad kısmı boşsa hata testi
mesaj1=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[1]/label/span/span")
if("Bu alan zorunludur." in mesaj1  and "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
 print("Ad kısmı boş olmaz alanı doğru çalışıyor..")
else:
 print ("Ad kısmı boş olmaz alanı yanlış calışıyor..")
#e posta adresi boşsa hata testi
mesaj2=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/span")

if("Bu alan zorunludur." in mesaj2  and "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
 print("Eposta kısmı boş olmaz alanı doğru çalışıyor..")
else:
 print ("Eposta kısmı boş olmaz alanı yanlış calışıyor..")

#ileti adresi boşsa hata testi
mesaj3=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/span")
if("Bu alan zorunludur." in mesaj3 and "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
 print("İleti kısmı boş olmaz alanı doğru çalışıyor..")
else:
 print ("İleti kısmı boş olmaz alanı yanlış calışıyor..")

#Hatalı e posta adresi 
mesaj4=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/span")
if "Girilen e-posta adresi geçersiz." in mesaj4:    
 print ("Eposta geçersiz hatası doğru çalışıyor...")
else:
 print ("Eposta geçersiz hatası çalışmıyor ")
"""
