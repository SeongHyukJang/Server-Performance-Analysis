import Measurements
import json
import requests

print("\n========== Comparison =========\n")

results = []

with open('clientResults.json','r') as file:
    iterations = json.load(file)

OS = requests.get('http://localhost:8000/os').content.decode()
for server in iterations['OS'][OS]['Server']:
    for resource in iterations['OS'][OS]['Server'][server]['resource']:
        for method in iterations['OS'][OS]['Server'][server]['resource'][resource]['method']:
            languages = Measurements.selectIterations(server,resource,method)
            for language in languages:
                results.append(Measurements.Measurement(*language).run())
            Measurements.writeResults(OS,server,results,resource,method)
            results.clear()                