#import requests library for making REST calls
import requests
import json

#specify url
url = 'my URL'

token = "my token"

data = {
        "agentName": "myAgentName",
        "agentId": "20",
        "description": "Changed Description",
        "platform": "Windows"
        }

headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", data:data}

#Call REST API
response = requests.put(url, data=data, headers=headers)

#Print Response
print(response.text)
