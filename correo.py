import sys
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP y credenciales
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # El puerto puede variar según el proveedor de correo
smtp_username = 'ninovargas@gmail.com'
smtp_password = 'hzvv tzhs lgch wrrr'

# Configuración del mensaje
sender_email = 'ninovargas@gmail.com'
receiver_email = 'ninovargas@yopmail.com'
subject = 'Correo de Prueba'
body = 'Este es un correo de prueba para automatizar envio de correo con Python en Jenkins'

# Construcción del mensaje
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Adjuntar el cuerpo del mensaje
message.attach(MIMEText(body, 'plain'))

# Establecer la conexión al servidor SMTP y enviar el mensaje
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    print('Correo enviado exitosamente.')
except Exception as e:
    print(f'Error al enviar el correo: {e}')
