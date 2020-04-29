import requests
import json

headers = {
    'Content-Type': 'application/json',
}

data = '{ "userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25 }'

response = requests.post('http://localhost:8000/', headers=headers, data=data)