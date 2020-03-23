import lauda
import urllib
import requests
import http

stopWatch_for_http = lauda.StopWatch()
stopWatch_for_urllib = lauda.StopWatch()
stopWatch_for_requests = lauda.StopWatch()

# http를 이용한 url 접근 속도 측정
stopWatch_for_http.start()

test_for_http = http.client.HTTPSConnection('www.khu.ac.kr')
test_for_http.connect()

stopWatch_for_http.stop()

# urllib을 이용한 url 접근 속도 측정
stopWatch_for_urllib.start()

test_for_urllib = urllib.request.urlopen('http://www.khu.ac.kr')

stopWatch_for_urllib.stop()


# requests를 이용한 url 접근 속도 측정
stopWatch_for_requests.start()

test_for_requests = requests.get('http://www.khu.ac.kr')

stopWatch_for_requests.stop()

print('{}ms 경과'.format(round(stopWatch_for_http.elapsed_time * 1000)))
print('{}ms 경과'.format(round(stopWatch_for_urllib.elapsed_time * 1000)))
print('{}ms 경과'.format(round(stopWatch_for_requests.elapsed_time * 1000)))