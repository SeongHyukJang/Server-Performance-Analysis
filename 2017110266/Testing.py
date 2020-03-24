#!/usr/bin/env python
#import http
#import urllib
import requests

# http를 이용한 url 접근 속도 측정
#test_for_http = http.client.HTTPSConnection('www.khu.ac.kr')


# urllib을 이용한 url 접근 속도 측정
#test_for_urllib = urllib.request.urlopen('http://www.khu.ac.kr')


# requests를 이용한 url 접근 속도 측정
test_for_requests = requests.get('http://localhost:8080')

# modules = { "http" : test_for_http,
#             "urllib" : test_for_urllib,
#             "requests" : test_for_requests
# }

