import urllib.request 

url = "http://www.google.com"
#url = "http://github.com/santakd"

n = 9

for i in range(n):
    print("ping counter: " + str(i))
    urllib.request.urlopen(url).read()