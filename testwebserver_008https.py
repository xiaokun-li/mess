import requests
import logging
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(filename='server_status_https_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Email credentials and recipient
email_sender = 'your_email@gmail.com'
email_password = 'your_password'  # Consider using an app password if 2FA is enabled
email_recipient = 'recipient_email@example.com'


def send_email_alert(subject, message):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, email_password)
    text = msg.as_string()
    server.sendmail(email_sender, email_recipient, text)
    server.quit()


def check_server_status(url):
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            logging.info(f"Server is up - Response time: {response.elapsed.total_seconds()} seconds")
        else:
            message = f"Server returned status code {response.status_code}"
            logging.warning(message)
            send_email_alert("Server Status Alert", message)
    except requests.exceptions.RequestException as e:
        message = f"Error connecting to the server: {e}"
        logging.error(message)
        send_email_alert("Server Status Alert", message)


if __name__ == "__main__":
    url = "https://eschenker.dbschenker.com"  # Change this to your server's URL
    while True:
        check_server_status(url)
        sleep(60)  # Wait for 60 seconds before checking again
