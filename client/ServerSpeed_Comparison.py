import ServerSpeed_Measurements
import json
import requests

print("\n========== Server Speed Comparison =========\n")

with open('ResponseTimeResult.json','r') as file:
    iterations = json.load(file)

for server in iterations['Server']:
    for resource in iterations['Server'][server]['resource']:
        for method in iterations['Server'][server]['resource'][resource]['method']:
            ServerSpeed_Measurements.run(server,resource,method)