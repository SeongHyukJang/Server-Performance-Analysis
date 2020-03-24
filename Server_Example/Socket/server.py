#-*- coding: utf-8-*-
import socket

# 접속할 서버 주소
HOST = '127.0.0.1'

# 클라이언트 접속을 대기하는 포트 번호
PORT = 9999

# 소켓 객체 생성
# 주소 체계(address family)로 IPv4, 소켓 타입은 TCP 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는 WinError 10048 에러 해결을 위한 코드
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용
# HOST는 hostname, ip address, 빈 문자열 ""가능
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속 허용
# PORT는 1-65535 사이의 숫자 사용
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용
server_socket.listen()

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴함
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소
print('Connected by', addr)

# 무한루프를 돌면서
while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프를 중지함
    if not data:
        break

    # 수신받은 문자열을 출력
    print('Recived from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송 (echo)
    client_socket.sendall(data)

# 소켓을 닫음
client_socket.close()
server_socket.close()

