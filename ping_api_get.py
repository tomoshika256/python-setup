import requests

url = "http://tk2-242-30965.vs.sakura.ne.jp:8080/02/ping"
payload = {"zn": "1310045"}
r = requests.get(url)
print(r.text)
