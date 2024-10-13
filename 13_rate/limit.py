import requests
import time

for i in range(3):
    r = requests.get("http://localhost:5000/")
    print(r.text)
    time.sleep(1)
