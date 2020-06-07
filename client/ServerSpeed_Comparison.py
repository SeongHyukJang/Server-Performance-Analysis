import ServerSpeed_Measurements
import json
import requests

print("\n========== Server Speed Comparison =========\n")

with open('ResponseTimeResult.json','r') as file:
    iterations = json.load(file)

OS = requests.get('http://localhost:8000/os').content.decode()
for server in iterations['OS'][OS]['Server']:
    for resource in iterations['OS'][OS]['Server'][server]['resource']:
        for method in iterations['OS'][OS]['Server'][server]['resource'][resource]['method']:
            ServerSpeed_Measurements.run(server,resource,method)