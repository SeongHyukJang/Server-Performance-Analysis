#!/usr/bin/env python3


# http를 이용한 url 접근 속도 측정
# import http
# test_for_http = http.client.HTTPSConnection('http://localhost:8000')


# urllib을 이용한 url 접근 속도 측정
# import urllib
# test_for_urllib = urllib.request.urlopen('http://localhost:8000')


# requests를 이용한 url 접근 속도 측정
import requests
response = requests.get('http://localhost:8000/data')