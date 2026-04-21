import requests
headers = {"User-Agent": "Hello World/1.1"}
response = requests.get("https://httpbin.org/user-agent", headers = headers)
print(response.text)