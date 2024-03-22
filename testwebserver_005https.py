import http.client
import time

def check_server_status(host, port=443):
    conn = None
    try:
        conn = http.client.HTTPSConnection(host, port, timeout=10)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        if response.status == 200:
            print(f"Server {host}:{port} is accessible.")
        elif response.status == 302:
            print(f"Server {host}:{port} is accessible, but redirected to: {response.headers['Location']}")
        else:
            print(f"Server {host}:{port} returned status code: {response.status}")
    except ConnectionRefusedError:
        print(f"Connection to {host}:{port} refused.")
    except TimeoutError:
        print(f"Connection to {host}:{port} timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Hostname and port of the web server you want to monitor
    # Default HTTPS port is 443
    server_host = "ebusiness.schenker.com.hk"
    server_port = 443

    # Interval between checks (in seconds)
    check_interval = 60

    while True:
        check_server_status(server_host, server_port)
        time.sleep(check_interval)
