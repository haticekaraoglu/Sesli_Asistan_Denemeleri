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



##ser=Service("./chromedriver.exe") 
#driver=webdriver.Chrome(service=ser)


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

    def ses_karslik(self,gelen_Ses):
     
              
        if(gelen_Ses in "programı kapat"):
            self.seslendirme("program kapatılıyor")
            exit()
## GOOGLE AÇ FONKSİYONU
        if(gelen_Ses in "google aç" or gelen_Ses in "google'da arama yap" ):     
              driver=webdriver.Chrome()
              driver.get("https://www.google.com")
              link=driver.current_url
              baslık=driver.title
              
              if "google.com" in link:
               print ("google başarılı bi şekilde açıldı") 
               driver.maximize_window()
               
              self.seslendirme("aramamı istediğiniz içerigi söyleyin")
              arama=self.mikrofon().lower()
              aramakutusu=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
              aramakutusu.send_keys(arama)
              aramakutusu.send_keys(Keys.ENTER)
              aranan_icerik=arama
              self.seslendirme("{} ile ilgili içerikler".format(aranan_icerik))
              
              ##site=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/div/span/a/h3").click()

 ### DRİVE AÇ FONKSİYONU
        elif(gelen_Ses in "drive aç"):
           self.seslendirme("drivenız açılıyor..")
           driver=webdriver.Chrome()
           google_url="https://drive.google.com/"
           driver.get(google_url)
           link=driver.current_url
           baslık=driver.title
           if "drive.google.com" in link:
            print ("drive başarılı bi şekilde açıldı") 
            driver.maximize_window()



## MAİL AÇ FONKSİYONU
        elif(gelen_Ses in "mail aç"):
           self.seslendirme("mailiniz açılıyor..")
           driver=webdriver.Chrome()
           google_url="https://mail.google.com/"
           driver.get(google_url)
           link=driver.current_url
           baslık=driver.title
           if "mail.google.com" in link:
            print ("mail başarılı bi şekilde açıldı") 
            driver.maximize_window()

## AAAAA WEB SAYFASI AÇILIMI         
        elif(gelen_Ses in "web sitesi"):
           self.seslendirme("web sitesi açılıyor..")
          
           google_url="https://aaaaa.com/"
           driver=webdriver.Chrome()
           driver.get(google_url)
           link=driver.current_url
           baslık=driver.title
           if "aaaa.com" in link:
            print ("web sayfamız başarılı bi şekilde açıldı") 
            driver.maximize_window()

           self.seslendirme("bize ulaşmak ister misiniz")
           cevap4=self.mikrofon()
           if(cevap4 in "evet"):
            self.seslendirme("Adresimiz Malatya Teknopark  ...... Mail Adresimiz aaaaa.com ........Telefon +90.......")
            


           self.seslendirme("yapmamı istediğiniz işlemi belirtiniz")  
           cevap4=self.mikrofon().lower()
           time.sleep(5)
           if():
               print
           elif(cevap4 in "iletişim formunu doldur " or cevap4 in "iletişim formu "):

            self.seslendirme("iletişim sayfası açılıyor..")
            try:    
            
                    iletisim=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div/div/div/section[14]").click()
                    self.seslendirme("form doldurmaya başlamamı istiyorsanız evet demeniz yeterli olacaktır")
                    cevap4=self.mikrofon().lower()
                    if(cevap4 in "evet"):
                            self.seslendirme("adınızı söyler misiniz")
                            cevap4=self.mikrofon().lower()
                            site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[1]/label/span/input").send_keys(cevap4)
                  
                            
                            
                            self.seslendirme("e posta adresinizi söyler misiniz")
                            cevap4=self.mikrofon().lower()
                            if "gmail.com" in cevap4 or "hotmail.com" in cevap4 :
                               mail_düzenleme=cevap4
                               son_et=mail_düzenleme.rfind("et")
                               mail_düzenleme = (mail_düzenleme[:son_et].strip() + "@" + mail_düzenleme[son_et+2:].strip())
                          

                            site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/input").send_keys(mail_düzenleme)
                            print(mail_düzenleme)
                            
                    
                    
                            self.seslendirme("telefon numarınız girmek ister misiniz ")
                            cevap4=self.mikrofon().lower()
                            if(cevap4 in"evet"):
                                self.seslendirme("telefon numaranızı söyler misiniz")
                                cevap4=self.mikrofon()
                                site=driver.findS_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[3]/label/span/input").send_keys(cevap4)

                            self.seslendirme("iletiniz nedir") 
                            cevap4=self.mikrofon().lower()
                            site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/textarea").send_keys(cevap4)

                            



                            self.seslendirme("formu göndermemi ister misin")
                            cevap4=self.mikrofon().lower()
                            if(cevap4 in "evet"):
                                
                                site=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[5]/input").click()
                            
                            #genel mesaj
                            mesaj=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/div[2]")
                          #ad kısmı boşsa hata testi
                            mesaj1=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[1]/label/span/span")
                          
                            if("Bu alan zorunludur." in mesaj1  or "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
                                print("Ad kısmı boş olmaz alanı doğru çalışıyor..")
                            else:
                                print ("Ad kısmı boş olmaz alanı yanlış calışıyor..")

                           #e posta adresi boşsa hata testi
                            mesaj2=driver.find_element(By.XPATH,"//*[ @id='wpcf7-f6-p158-o1']/form/p[2]/label/span/span")
                            if("Bu alan zorunludur." in mesaj2  or "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
                                print("Eposta kısmı boş olmaz alanı doğru çalışıyor..")
                            else:
                                print ("Eposta kısmı boş olmaz alanı yanlış calışıyor..")


                           #ileti adresi boşsa hata testi
                            mesaj3=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[4]/label/span/span")
                            if("Bu alan zorunludur." in mesaj3 or "Bir veya daha fazla alanda hata bulundu. Lütfen kontrol edin ve tekrar deneyin." in mesaj):
                                print("İleti kısmı boş olmaz alanı doğru çalışıyor..")
                            else:
                                print ("İleti kısmı boş olmaz alanı yanlış calışıyor..")

                            #Hatalı e posta adresi 
                            mesaj4=driver.find_element(By.XPATH,"//*[@id='wpcf7-f6-p158-o1']/form/p[2]/label/span/span")
                            if "Girilen e-posta adresi geçersiz." in mesaj4:    
                                print ("Eposta geçersiz hatası doğru çalışıyor...")
                            
                            else:
                                print ("Eposta geçersiz hatası çalışmıyor ")




                            self.seslendirme("tarayıcıdan çıkmak ister misiniz")
                            cevap4=self.mikrofon().lower()
                            if(cevap4 in "evet"):
                                 self.seslendirme("tarayıcıdan çıkılıyor...")
                                 driver.quit()
           
                   
                                   
            except :
                self.seslendirme("hata ile karşılaşıldı")    
    

        self.seslendirme("sayfayı ve programı kapatmamı ister misiniz ")
        cevap4=self.mikrofon().lower()
        if(cevap4 in "evet "):
          driver.quit()
          exit()

        time.sleep(50)
        driver.quit()   
         

    
## Asistan uyunama fonksiyonu 
    def uyanma_fonksiyonu(self,gelen_Ses):
 
        if(gelen_Ses!=""):
            if(gelen_Ses in "asistan"):
                    self.saat=datetime.datetime.now().hour
                    if self.saat>=0 and self.saat<=12:
                        self.seslendirme("günaydın ben Sesli Asistanınız sizi dinliyorum...")
                        self.seslendirme("benim hakkımda bilgi almak istiyorsanız lütfen evet istemiyorsanız hayır demeniz yeterli olacaktır")
                        cevap=self.mikrofon().lower()
                        if(cevap in "evet"):
                            self.seslendirme("Umarım gününüz güzel geçiyordur aaaaaa ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaaaaaa web sitesini açmamı istiyorsanız aaaaaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
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
                            self.seslendirme("Umarım gününüz güzel geçiyordur aaaaaaa ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaaaa web sitesini açmamı istiyorsanız aaaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
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
                            self.seslendirme("Umarım gününüz güzel geçiyordur aaaaaa ailesi olarak bizlerle olmanızdan mutluluk duyuyorum")   
                            self.seslendirme("lütfen bana yapmamı istediğiniz işlemi sessiz bir ortamda ve anlaşılır bi şekilde belirtiniz")
                            self.seslendirme("sizin için yapabileceğim işlemler sırasıyla google açmak ve arama yapmak eğer bu işlemi istiyorsanız google aç demeniz, drivenızı veya mailinizi açmamı istiyorsanız drive aç veya mail aç demeniz, aaaaaaaa web sitesini açmamı istiyorsanız aaaaaaaaa web sitesi demeniz, sitede bulunan ulaşım formunu doldurmamı istiyorsanız iletişim formunu doldur demeniz yeterli olacaktır yada beni kapatmak istiyorsanız programı kapat demeniz yeterli olacaktır")
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












