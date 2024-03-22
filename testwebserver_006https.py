import requests
import logging
from time import sleep

# Configure logging
logging.basicConfig(filename='server_status.log', level=logging.INFO, format='%(asctime)s %(message)s')

def check_server_status(url):
    try:
        response = requests.get(url)
        # Check if the server is up
        if response.status_code == 200:
            logging.info(f"Server is up - Response time: {response.elapsed.total_seconds()} seconds")
        else:
            logging.warning(f"Server returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to the server: {e}")

if __name__ == "__main__":
    url = "https://www.baidu.com"  # Change this to your server's URL
    while True:
        check_server_status(url)
        sleep(60)  # Wait for 60 seconds before checking again
