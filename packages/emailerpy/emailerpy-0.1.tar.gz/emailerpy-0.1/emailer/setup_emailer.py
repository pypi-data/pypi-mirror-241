import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def setup_email_server(server, port, sender_email, password):
    server = server
    port = port
    sender_email = sender_email
    password = password
    Data = {
        "server": server,
        "port": port,
        "sender_email": sender_email,
        "password": password,
    }

    return Data


def send_email(destinataire, subject, message_mail, server=None):
    message = MIMEMultipart()
    message["From"] = server["sender_email"]
    message["To"] = destinataire
    message["Subject"] = subject
    message.attach(MIMEText(message_mail, "plain"))
    connexion = None
    Data = server
    if Data is None:
        raise ("the configuration method was not properly configured")

    try:
        connexion = smtplib.SMTP(Data["server"], Data["port"])
        connexion.starttls()
        connexion.login(Data["sender_email"], Data["password"])

        connexion.send_message(message)

        print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
    finally:
        if connexion:
            connexion.quit()
