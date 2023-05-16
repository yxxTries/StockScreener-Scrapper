from Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

# selenium screenshot initiation 
ob = Screenshot.Screenshot()

#arguments for chrome webdriver
opt = Options()
opt.add_argument('--no-sandbox')
opt.add_argument('--start-maximized')
opt.add_argument('--headless')
opt.add_argument("window-size=1440, 1500")
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

#activating webdriver and opening webpage
def web_scrapper(): 
    
    driver = webdriver.Chrome(options = opt, executable_path='chromedriver.exe')
    driver.get('https://www.screener.in/screens/743398/stock-go-up/')

    #screenshoting the selenium webpage
    img=ob.full_Screenshot(driver, save_path=r'D:/coding stuff/stock gappers', image_name="gappers.jpg")
    img1 = Image.open('D:\coding stuff\stock gappers\gappers.jpg')
    # img1.show()

    driver.quit()

    #############################        PT 2         ####################################
    ################## sending screener info to personal email ###########################

    fromaddr = sender_email
    toaddr = receiver_email
    apppass = mailpass

    fromaddr = "from@gmail.com"
    toaddr = "receive@gmail.com"
    apppass = "hpbbfiafalubtlvz"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "STOCKS BE GETTING GAPPED HOLY"

    # string to store the body of the mail
    body = "WAKEY WAKEY GRINDSET TIME"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "gappers.jpg"
    attachment = open("D:\coding stuff\stock gappers\gappers.jpg", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, apppass)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    try:
        s.sendmail(fromaddr, toaddr, text)
        print(f"Mail sent to {toaddr} successfully !")
    except:
        print("Mail not sent !!")

    # terminating the session
    s.quit()
    
keep_alive()
schedule.every(10020).seconds.do(web_scrapper)

while 1:
    schedule.run_pending()
    time.sleep(1)

