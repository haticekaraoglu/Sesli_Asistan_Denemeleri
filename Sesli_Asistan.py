import datetime
import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

   
## Asistan uyunama fonksiyonu 

r=sr.Recognizer()


class SesliAsistan:

    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr",slow=False)
        dosya = str(random.randint(0, 10000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def mikrofon(self):
        with sr.Microphone() as kaynak:
            
            print("Sizi dinliyorum beni başlatmak istiyorsanız asistan demeniz yeterli olacaktır ..")
            ##r.recognizer_instance.adjust_for_ambient_noise(kaynak, duration = 1)
            ##Recognizer'ın çevredeki gürültü seviyesine göre enerji eşiğini ayarlamasına izin vermek için bir saniye bekleme 
            ##r.recognizer_instance.dynamic_energy_threshold = False
            listen=r.listen(kaynak)
            ses=" "
            try:
                ses=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("sesiniz anlaşılmadı lütfen tekrar edin")
            return ses.lower()



    def uyanma_fonksiyonu(self,gelen_Ses):
 
        if(gelen_Ses!=""):
            if(gelen_Ses in "asistan"):
                    self.saat=datetime.datetime.now().hour
                    if self.saat>=0 and self.saat<=12:
                        self.seslendirme("günaydın ben Sesli Asistanınız sizi dinliyorum...")
                        self.seslendirme("benim hakkımda bilgi almak istiyorsanız lütfen evet istemiyorsanız hayır demeniz yeterli olacaktır")
                        cevap=self.mikrofon().lower()
                        if(cevap in "evet"):
                            self.seslendirme("Umarım gününüz güzel geçiyordur .... ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaa web sitesini açmamı istiyorsanız aaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
                            self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                            ses=self.mikrofon().lower()
                        else:
                                self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                                ses=self.mikrofon().lower()
                            
                    elif self.saat>=12 and self.saat<=18:
                        self.seslendirme("iyi günler ben Sesli Asistanınız sizi dinliyorum...")
                        self.seslendirme("benim hakkımda bilgi almak istiyorsanız lütfen evet diyin istemiyorsanız hayır ")
                        cevap=self.mikrofon().lower()
                        if(cevap in "evet"):
                            self.seslendirme("Umarım gününüz güzel geçiyordur ..... ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaa web sitesini açmamı istiyorsanız aaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
                            self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                            ses=self.mikrofon().lower()
                        else:
                                self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                                ses=self.mikrofon().lower()
                    elif self.saat>=18 and self.saat<=24:
                        self.seslendirme("iyi akşamlar ben Sesli Asistanınız sizi dinliyorum...")
                        self.seslendirme("benim hakkımda bilgi almak istiyorsanız lütfen evet diyin istemiyorsanız hayır ")
                        cevap=self.mikrofon().lower()
                        if(cevap in "evet"):
                            self.seslendirme("Umarım gününüz güzel geçiyordur aaaaa ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaaa web sitesini açmamı istiyorsanız aaaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
                            self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                            ses=self.mikrofon().lower()
                        else:
                                self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                                ses=self.mikrofon().lower()
           
            if(ses!=""):   
              self.ses_karslik(ses)
 
            else:
              self.seslendirme("ne dediğiniz anlasılmadı işleme devam etmek istiyorsanız lütfen devam etmek istiyorum diyin ")
              ses=self.mikrofon().lower()
              if(ses in " devam etmek istiyorum"):
                self.seslendirme(" yapmak istediğiniz işlemi belirtiniz")
                ses=self.mikrofon().lower()
                self.ses_karslik(ses)
              else:
                 self.seslendirme("program kapatılıyor")
                 exit()

        
        else:
            self.seslendirme("sesiniz anlaşılmadı lütfen devam etmek istiyorsanız tekrar asistan diyin")
            ses=self.mikrofon().lower()
            if(ses==""):
                 self.seslendirme("program kapatılıyor")
                 exit()


## Asistanın uyanması için çağrıldığı kısım
asistan = SesliAsistan()
       
while True:
    gelen_Ses=asistan.mikrofon().lower()
    if(gelen_Ses!=" "):
        print(gelen_Ses)

    
    asistan.uyanma_fonksiyonu(gelen_Ses)












