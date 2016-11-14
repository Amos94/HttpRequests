import threading
from urllib.request import urlopen
import time


urls = ["your html page"]

def fetch_url(url):
    request = urlopen(urls[0])
    print("Status:", request.status, request.reason)

while(True):
    threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()