import delegator
import lauda
import json

def run(server, resource, method):

    print("\n=============================================\n\n")
    print("Server : ",server)
    print("resource : ", resource)
    print("method : ", method)

    times = []
    user = 1
    request = ''
    stopwatch = lauda.StopWatch()

    if server == 'python':
        if resource == 'json':
            if method == 'GET':
                query = 'curl http://localhost:8000/json'
            elif method == 'POST':
                query = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8000'
        elif resource == 'calc':
            if method == 'GET':
                query = 'curl http://localhost:8000/calc'
        elif resource == 'html':
            if method == 'GET':
                query = 'curl http://localhost:8000/html'
    elif server == 'javascript':
        if resource == 'json':
            if method == 'GET':
                query = 'curl http://localhost:8080/json'
            elif method == 'POST':
                query = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8080'
        elif resource == 'calc':
            if method == 'GET':
                query = 'curl http://localhost:8080/calc'
        elif resource == 'html':
            if method == 'GET':
                query = 'curl http://localhost:8080/html'

    while user != 50:
        request += query

        stopwatch.start()
        delegator.run(request)
        stopwatch.stop()

        times.append(int(stopwatch.elapsed_time * 1000))
        request += ' & '
        user += 1
    print('\n')
    return times

def writeResults(OS, server, results, resource, method):
    with open('LoadTestResult.json','r') as file:
        data = json.load(file)
    
    data['OS'][OS]['Server'][server]['resource'][resource]['method'][method] = list(results)

    with open('LoadTestResult.json','w') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)