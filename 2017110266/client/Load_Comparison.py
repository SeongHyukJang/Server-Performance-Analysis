import LoadMeasurements
import json
import requests

print("\n========== Load Comparison =========\n")

results = []

with open('LoadTestResult.json','r') as file:
    iterations = json.load(file)

OS = requests.get('http://localhost:8000/os').content.decode()
for server in iterations['OS'][OS]['Server']:
    for resource in iterations['OS'][OS]['Server'][server]['resource']:
        for method in iterations['OS'][OS]['Server'][server]['resource'][resource]['method']:
            results.append(LoadMeasurements.run(server, resource, method))
            LoadMeasurements.writeResults(OS,server,results,resource,method)
            results.clear()