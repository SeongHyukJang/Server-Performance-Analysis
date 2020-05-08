#!/usr/bin/env python3
# requests를 이용한 url 접근 속도 측정
import requests
response = requests.get('http://localhost:8000/json')