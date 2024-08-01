import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
r=sr.Recognizer()

class SesliAsistan:

    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr",slow=False)
        dosya = str(random.randint(0, 10000000000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def mikrofon(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum..")
            listen=r.listen(kaynak)
            ses=""
            try:
                ses=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("ne dediğinizi anlayamadım")
            return ses.lower()

    def ses_karslik(self,gelen_Ses):
        if(gelen_Ses in "programı kapat"):
           self.seslendirme("program kapatılıyor")
           exit()
        elif(gelen_Ses in "merhaba"):
            self.seslendirme("size de merhabalar")
        elif(gelen_Ses in "nasılsın"):
            self.seslendirme("iyiyim sizler nasılsınız")
        elif(gelen_Ses in "video aç" or gelen_Ses in "müzik aç"):
            try:
             self.seslendirme("ne açmamı istersiniz ")
             cevap=self.mikrofon()

             url="https://www.youtube.com/results?search_query="+cevap
             tarayici=webdriver.Chrome()
             tarayici.get(url)

             
             ilk_video=tarayici.find_element(By.XPATH,"//*[@id='video-title']/yt-formatted-string").click()
             time.sleep(5)


             self.seslendirme("İstediğiniz içerik bu mu")   
             cevap2=self.mikrofon().lower()
             if (cevap2 in "hayır"):
              sayac=2
              tarayici.back()
              while (sayac<5):
                diger_video=tarayici.find_elements(By.XPATH,"//*[@id='items']/ytd-video-renderer[{}]".format(sayac)).click()
                time.sleep(10)
                self.seslendirme("İstediğiniz içeri bu mu")   
                cevap2=self.mikrofon().lower()
                if (cevap2 in "evet"):
                   self.seslendirme("keyifli vakit geçirmeler...")
                   break
                else:
                   self.seslendirme("o zaman diğer videolara bakalım")
                   tarayici.back()
                   sayac+=1
             else:
                self.seslendirme("keyifli vakit geçirmeler")
                time.sleep(60) 
                tarayici.quit()      
            except:
               self.seslendirme("Bir hatayla karşılaşıldı lüften daha sonra tekrar deneyin")
        elif(gelen_Ses in "google aç" or gelen_Ses in "googleda arama yap" or gelen_Ses in "film aç"):     
      
              self.seslendirme("aramamı isteiğiniz içerigi söyleyin")
              arama=self.mikrofon().lower()

              google_url="https://www.google.com/search?q="+arama
              tarayici=webdriver.Chrome()
              tarayici.get(google_url)

              self.seslendirme("{} ile ilgili içerikler".format(arama))
              
              site=tarayici.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/div/span/a/h3").click()


        elif(gelen_Ses in "film öner" or gelen_Ses in "film önerisi yap"):
             google_url="https://sinemalar.com/filmler"
             tarayici=webdriver.Chrome()
             tarayici.get(google_url)
             yer=[]
             self.seslendirme("haftanın popüler filmleri bunlar hangi tür film izlemek istiyorsunuz")
             cevap3=self.mikrofon()
             if(cevap3.find(" ")==-1):
              google_url=  "https://www.sinemalar.com/filmler/en-iyi-{}-filmleri".format(cevap3)
              tarayici=webdriver.Chrome()
              tarayici.get(google_url)
             
             
             elif(cevap3 in "3 Boyutlu"):
              google_url=  "https://www.sinemalar.com/filmler/en-iyi-3-boyutlu-filmler"
              tarayici=webdriver.Chrome()
              tarayici.get(google_url)

             
           

             elif(cevap3 != ""):
              
              yer1 = cevap3.replace(' ','-')
              
              google_url=  "https://www.sinemalar.com/filmler/en-iyi-{}-filmleri".format(yer1)
              tarayici=webdriver.Chrome()
              tarayici.get(google_url)

            
        elif(gelen_Ses in "fotograf çek"):
            self.seslendirme("kameranızı açıyorum ")

            kamera=cv2.VideoCapture(0)
            kontrol,resim=kamera.read()  
            self.seslendirme("gülümseyin çekiyorum")
            cv2.imwrite("resim.jpg",resim)
            kamera.release()
            
            time.sleep(3)
            self.seslendirme("Fotografınızı görmek istiyor musunuz ")
            cevap=self.mikrofon()

            if cevap in "evet":
                resim=cv2.inread("resim.jpg")
                cv2.inshow("Resim",resim)
                cv2.destroyAllWindows()

         
        elif(gelen_Ses in "drive aç"):
           self.seslendirme("drivenız açılıyor..")
           google_url="https://drive.google.com/drive/my-drive"
           tarayici=webdriver.Chrome()
           tarayici.get(google_url)


        time.sleep(10)
        tarayici.quit()   
         

    

    def uyanma_fonksiyonu(self,gelen_Ses):
        if(gelen_Ses in "hey siri"):
            self.seslendirme("dinliyorum...")
            ses=self.mikrofon()
            if(ses!=""):
                self.ses_karslik(ses)



asistan = SesliAsistan()

while True:
    gelen_Ses=asistan.mikrofon().lower()
    if(gelen_Ses!=""):
        print(gelen_Ses)
      
        
        asistan.uyanma_fonksiyonu(gelen_Ses)


