import urllib.request
import time

url = "http://www.google.com"
n = 9

for i in range(n):
    print("ping counter: " + str(i))
    try:
        urllib.request.urlopen(url).read()
        print(f"Ping " + str(i) + " successful.")
    except Exception as e:
        print(f"Ping " + str(i) + " failed: " + {str(e)})
    time.sleep(3)