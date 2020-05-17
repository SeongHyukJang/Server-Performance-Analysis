import requests
import json

headers = {
    'Content-Type': 'application/json',
}

data = '{ "userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25 }'

requests.post('http://localhost:8080/', headers=headers, data=data)