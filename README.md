# 프로그래밍 언어별 HTTP 프로토콜의 네트워크 측면 성능 평가

1. 개요
    - 최근 다양한 프로그래밍 언어들은 HTTP 프로토콜을 기반으로 하여 각자의 라이브러리로 서버를 설계할 수 있다. 하지만 그것들의 네트워크 측면의 성능 평가는 제대로 이루어지지 않았다

    - client-server architecture를 기반으로 client 측면과 server 측면에서 프로그래밍 언어의 성능을 평가한다

2. 수행방법
    - server : Python, Javascript(node), Go
    - client : Python, Javascript(node), curl
    - resource : json, calculation, html
    - networking : http(GET, POST)

3. 시나리오
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
        
        1. Concurrent Users
            - 동시접속자의 수의 증가에 따른 server간의 TPS 비교
            - 접속자의 수는 0명에서 시작하여 초당 10명씩 증가하여 1000명까지 증가한다
            - connection time 또는 response time이 10초를 초과하면 thread의 연결을 끊는다 (error로 분류)
            - os : linux
            - client : apache-jmeter
            - server : python, javascript(node), go

        2. CPU
            - 동시접속자의 수가 증가함에 따른 server간의 CPU 사용률을 비교
            - 제한 조건은 Concurrent Users와 같다
            - os : linux
            - client : apache-jmeter
            - server : python, javascript(node), go

        3. Memory
            - 동시접속자의 수가 증가함에 따른 server간의 메모리 사용률을 비교
            - 제한 조건은 Concurrent Users와 같다
            - os : linux
            - client : apache-jmeter
            - server : python, javascript(node), go

4. 결과
    1. Response Time
        - GET-JSON
        <img src="results/Response Time/GET JSON.png">
        - GET-Calc
        <img src="results/Response Time/GET Calc.png">
        - GET-HTML
        <img src="results/Response Time/GET HTML.png">
        - POST-JSON
        <img src="results/Response Time/POST JSON.png">
    
    2. Server Speed
        - GET-JSON
        <img src="results/Server Speed/GET JSON.png">
        - GET-Calc
        <img src="results/Server Speed/GET Calc.png">
        - GET-HTML
        <img src="results/Server Speed/GET HTML.png">
        - POST-JSON
        <img src="results/Server Speed/POST JSON.png">

    3. Load Test
        2. Concurrent Users
            - GET-JSON
            <img src="results/Concurrent Users/GET_json.png">
            - GET-Calc
            <img src="results/Concurrent Users/GET_calc.png">
            - GET-HTML
            <img src="results/Concurrent Users/GET_html.png">
            - POST-JSON
            <img src="results/Concurrent Users/POST_json.png">

        2. CPU
            - GET-JSON
            <img src="results/CPU/get-json-cpu.png">
            - GET-Calc
            <img src="results/CPU/get-calc-cpu.png">
            - GET-HTML
            <img src="results/CPU/get-html-cpu.png">
            - POST-JSON
            <img src="results/CPU/post-json-cpu.png">
        3. Memory
            - GET-JSON
            <img src="results/Memory/get-json-mem.png">
            - GET-Calc
            <img src="results/Memory/get-calc-mem.png">
            - GET-HTML
            <img src="results/Memory/get-html-mem.png">
            - POST-JSON
            <img src="results/Memory/post-json-mem.png">
        