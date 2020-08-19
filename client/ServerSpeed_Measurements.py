import delegator
import lauda

def run(server, resource, method):

    print("\n=============================================\n\n")
    print("Server : ",server)
    print("resource : ", resource)
    print("method : ", method)

    if server == 'python':
        if resource == 'json':
            if method == 'GET':
                query = 'curl http://localhost:8000/server-speed/json'
            elif method == 'POST':
                query = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8000/server-speed/post'
        elif resource == 'calc':
            if method == 'GET':
                query = 'curl http://localhost:8000/server-speed/calc'
        elif resource == 'html':
            if method == 'GET':
                query = 'curl http://localhost:8000/server-speed/html'
    elif server == 'javascript':
        if resource == 'json':
            if method == 'GET':
                query = 'curl http://localhost:8080/server-speed/json'
            elif method == 'POST':
                query = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8080/server-speed/post'
        elif resource == 'calc':
            if method == 'GET':
                query = 'curl http://localhost:8080/server-speed/calc'
        elif resource == 'html':
            if method == 'GET':
                query = 'curl http://localhost:8080/server-speed/html'
    elif server == 'go':
        if resource == 'json':
            if method == 'GET':
                query = 'curl http://localhost:8090/server-speed/json'
            elif method == 'POST':
                query = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8090/server-speed/post'
        elif resource == 'calc':
            if method == 'GET':
                query = 'curl http://localhost:8090/server-speed/calc'
        elif resource == 'html':
            if method == 'GET':
                query = 'curl http://localhost:8090/server-speed/html'
                
    count = 0
    while count != 100:
        delegator.run(query)
        count += 1