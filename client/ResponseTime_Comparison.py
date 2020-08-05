import ResponseTime_Measurements
import json
import requests

print("\n========== Response Times Comparison =========\n")

results = []

with open('ResponseTimeResult.json','r') as file:
    iterations = json.load(file)

for server in iterations['Server']:
    for resource in iterations['Server'][server]['resource']:
        for method in iterations['Server'][server]['resource'][resource]['method']:
            languages = ResponseTime_Measurements.selectIterations(server,resource,method)
            for language in languages:
                results.append(ResponseTime_Measurements.Measurement(*language).run())
            ResponseTime_Measurements.writeResults(server,results,resource,method)
            results.clear()