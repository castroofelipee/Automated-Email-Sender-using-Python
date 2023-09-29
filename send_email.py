import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv 

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

if __name__ == '__main__':
    load_dotenv()  

    user = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSWORD")
    to_email = os.getenv("TO_EMAIL")

    msg = EmailMessage()
    msg.set_content("Este é um e-mail de teste")

    msg['Subject'] = "Assunto do e-mail"
    msg['From'] = formataddr(('Remetente', user))
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(EMAIL_SERVER, PORT)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")
