import requests
import time

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server {url} is accessible.")
        else:
            print(f"Server {url} returned status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Server {url} is unreachable.")

if __name__ == "__main__":
    # URL of the web server you want to monitor
    server_url = "https://ebusiness.schenker.com.hk/Portal/hpmcd/invsum.html"

    # Interval between checks (in seconds)
    check_interval = 60

    while True:
        check_server_status(server_url)
        time.sleep(check_interval)
