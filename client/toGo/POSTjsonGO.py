import requests
import json

headers = {
    'Content-Type': 'application/json',
}

data = '{ "userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25 }'

requests.post('http://localhost:8090/post', headers=headers, data=data)