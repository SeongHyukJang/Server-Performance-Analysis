import SpeedMeasurements
import json
import requests

print("\n========== Speed Comparison =========\n")

results = []

with open('ResponseTimeResult.json','r') as file:
    iterations = json.load(file)

OS = requests.get('http://localhost:8000/os').content.decode()
for server in iterations['OS'][OS]['Server']:
    for resource in iterations['OS'][OS]['Server'][server]['resource']:
        for method in iterations['OS'][OS]['Server'][server]['resource'][resource]['method']:
            languages = SpeedMeasurements.selectIterations(server,resource,method)
            for language in languages:
                results.append(SpeedMeasurements.Measurement(*language).run())
            SpeedMeasurements.writeResults(OS,server,results,resource,method)
            results.clear()                