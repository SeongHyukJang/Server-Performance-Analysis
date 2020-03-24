#-*- coding: utf-8-*-
import socket

# 서버의 주소
HOST = '127.0.0.1'

# 서버에서 지정한 포트번호
POST = 9999

# 소켓 객체를 생성
# 주소 체계(address family)로 IPv4, 소켓 타입은 TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버에 접속
client_socket.connect((HOST,POST))

# 메시지를 전송
client_socket.sendall('Hello World'.encode())

# 메시지를 수신
data = client_socket.recv(1024)
print("Recieved", repr(data.decode()))

# 소켓을 닫음
client_socket.close()