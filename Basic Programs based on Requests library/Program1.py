import requests
url = "https://assets.mixkit.co/active_storage/sfx/213/213.wav"
r = requests.get(url)
with open("audio file.wav", "wb") as f:
    f.write(r.content)
    