import requests
# POST
data = {"title" : "Hello", "body" : "World", "userId" : 101}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)
print(response.status_code)
print(response.json())