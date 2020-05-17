import lauda
import delegator

request = 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8080'

request += ' & '

request += 'curl -d ' + "'" + '{"userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25}' + "'" + ' -H "Content-Type: application/json" http://localhost:8080'
delegator.run(request)