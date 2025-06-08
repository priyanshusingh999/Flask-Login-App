import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_ID, PASSWORD_ID

def send_yandex_email(receiver_email, password):
    try:
        # Yandex SMTP Configuration
        smtp_server = "smtp.yandex.com"
        port = 465  # SSL ke liye
        sender_email = f"{EMAIL_ID}"
        sender_password = f"{PASSWORD_ID}"  # Yandex password
        
        subject = "Password Reset Email"
        body = f"""
        <html>
        <body>
            <h2 style="color: #0077cc;">Hello from Python!</h2>
            <p>This is a <b>HTML-formatted</b> email sent using <i>Yandex SMTP</i>.</p>
            <p>Your Password: {password}</p>
            <p>Have a nice day! 🌟</p>
        </body>
        </html>
        """
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        # Connect and send (using SSL)
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        
        print("Email safaltapoorvak bhej diya gaya!")
        return True
    
    except smtplib.SMTPAuthenticationError:
        print("Truti: Authentication fail - kripya Yandex mail settings mein SMTP access chalu karein")
        return False
    except Exception as e:
        print(f"Anya truti: {str(e)}")
        return False
