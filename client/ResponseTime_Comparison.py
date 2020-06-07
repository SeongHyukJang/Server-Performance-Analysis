import ResponseTime_Measurements
import json
import requests

print("\n========== Response Times Comparison =========\n")

results = []

with open('ResponseTimeResult.json','r') as file:
    iterations = json.load(file)

OS = requests.get('http://localhost:8000/os').content.decode()
for server in iterations['OS'][OS]['Server']:
    for resource in iterations['OS'][OS]['Server'][server]['resource']:
        for method in iterations['OS'][OS]['Server'][server]['resource'][resource]['method']:
            languages = ResponseTime_Measurements.selectIterations(server,resource,method)
            for language in languages:
                results.append(ResponseTime_Measurements.Measurement(*language).run())
            ResponseTime_Measurements.writeResults(OS,server,results,resource,method)
            results.clear()