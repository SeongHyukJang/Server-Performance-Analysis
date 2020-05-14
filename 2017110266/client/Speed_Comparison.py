import Measurements
import json

print("\n========== Comparison =========\n")

results = []

with open('clientResults.json','r') as file:
    iterations = json.load(file)

for server in iterations['ServerLanguage']:
    for resource in iterations['ServerLanguage'][server]:
        for method in iterations['ServerLanguage'][server][resource]:
            languages = Measurements.selectIterations(server,resource,method)
            for language in languages:
                results.append(Measurements.Measurement(*language).run())
            Measurements.writeResults(server,results,resource,method)
            results.clear()