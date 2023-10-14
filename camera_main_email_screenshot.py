import smtplib
import imghdr
from email.message import EmailMessage
SENDER = 'carleyeshield21@gmail.com'
fast_food = 'wydzwtqjeeivhnoo'
RECEIVER = 'rus_greg@yahoo.com'

def send_email(image_fat):
    email_message = EmailMessage()
    email_message['Subject'] = 'May dumaang mumo'
    email_message.set_content('Merong na-detect ang iyong cctv camera')

    with open(image_fat, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype = 'image', subtype = imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, fast_food)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == '__main__':
    send_email(image_fat='detected_images/15.png')