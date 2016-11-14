from urllib.request import urlopen

while(True):
    request = urlopen("YOUR URL")
    print("Status: ", request.status, request.reason)