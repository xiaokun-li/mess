import requests
import logging
from time import sleep

# Configure logging
logging.basicConfig(filename='server_status_https.log', level=logging.INFO, format='%(asctime)s %(message)s')

def check_server_status(url):
    try:
        # For demonstration, using verify=True which is the default behavior
        # Replace True with '/path/to/certificate.pem' if using a custom certificate
        # response = requests.get(url, verify='/path/to/certificate.pem')
        # response = requests.get(url, verify=False)
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            logging.info(f"Server{url} is up - Response time: {response.elapsed.total_seconds()} seconds")
        else:
            logging.warning(f"Server{url} returned status code {response.status_code}")
    except requests.exceptions.SSLError as ssl_error:
        logging.error(f"SSL Error connecting to the server: {ssl_error}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to the server: {e}")

if __name__ == "__main__":
    url = "https://eschenker.dbschenker.com"  # Change this to your server's URL
    while True:
        check_server_status(url)
        sleep(60)  # Wait for 60 seconds before checking again
