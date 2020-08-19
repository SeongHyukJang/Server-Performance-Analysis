# 프로그래밍 언어별 HTTP 프로토콜의 네트워크 측면 성능 평가
---
### 개요
- 최근 다양한 프로그래밍 언어들은 HTTP 프로토콜을 기반으로 하여 각자의 라이브러리로 서버를 설계할 수 있다. 하지만 그것들의 네트워크 측면의 성능 평가는 제대로 이루어지지 않았다

- client-server architecture를 기반으로 client 측면과 server 측면에서 프로그래밍 언어의 성능을 평가한다
---
### 수행방법
- server : Python, Javascript(node), Go
- client : Python, Javascript(node), curl
- resource : json, calculation, html
- networking : http(GET, POST)
---
### 시나리오
1. Response Time
    - client 측면에서의 성능 비교
    - 각 client마다 100번의 통신
    - os : linux
    - client : python, javascript(node), curl
    - server : python

2. Server Speed
    - server 측면에서의 성능 비교
    - 각 server마다 100번의 통신
    - os : linux
    - client : curl
    - server : python, javascript(node), go

3. Load Test
    - server 측면에서의 stress test 진행
    - 접속자의 수는 0명에서 시작하여 초당 10명씩 증가하여 1000명까지 증가한다
    - connection time 또는 response time이 10초를 초과하면 thread의 연결을 끊는다 (error로 분류)
    
    1. Concurrent Users
        - 동시접속자의 수의 증가에 따른 server간의 TPS 비교
        - os : linux
        - client : apache-jmeter
        - server : python, javascript(node), go

    2. CPU
        - 동시접속자의 수가 증가함에 따른 server간의 CPU 사용률을 비교
        - os : linux
        - client : apache-jmeter
        - server : python, javascript(node), go

    3. Memory
        - 동시접속자의 수가 증가함에 따른 server간의 메모리 사용률을 비교
        - os : linux
        - client : apache-jmeter
        - server : python, javascript(node), go
---
### 결과
1. [Response Time](https://github.com/SeongHyukJang/Server-Performance-Analysis/tree/master/results/Response%20Time)
2. [Server Speed](https://github.com/SeongHyukJang/Server-Performance-Analysis/tree/master/results/Server%20Speed)
3. Load Test
    1. [Concurrent Users](https://github.com/SeongHyukJang/Server-Performance-Analysis/tree/master/results/Concurrent%20Users)
    2. [CPU](https://github.com/SeongHyukJang/Server-Performance-Analysis/tree/master/results/CPU)
    3. [Memory](https://github.com/SeongHyukJang/Server-Performance-Analysis/tree/master/results/Memory)
