#import requests library for making REST calls
import requests
import json

#specify url
url = 'www.eboxx.com.br/pub/MedChain/ledger'

token = "742974fnsjh380vn38fnl4238vhn488v0s0nnrdhf83nl8yc38cn3"

data = {
        "agentName": "MedChain",
        "mosaicId": "20hgfdsk3kbnhg453bkg45",
        "description": "DataIN",
        "msg": "onoononoonononooonononono"
        "frameid": "1x300"
        }

headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", data:data}

#Call REST API
response = requests.put(url, data=data, headers=headers)

#Print Response
print(response.text)
