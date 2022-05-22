import requests

url = "https://reqres.in/api/login"
myobj = {"email": "peter@klaven"}
x = requests.post(url,data=myobj)
print(x.text)

