import Measurements
import csv

print("\n========== Comparison =========")
print("Iterations : Python (8000)")
print("JSON")

print("============ HTTP POST ============")

languages = [
    #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
    ["Python 3", "python --version", "python TestingPOST.py"],
    ["JS (node)", "node --version", "node TestingPOST.js"],
    ["curl", "curl --version", "./TestingPOST.sh"]
]

results = [['Language', 'best', 'worst', 'median']]

for language in languages:
    results.append(Measurements.Measurement(*language).run())

with open('results.csv','w',newline='',encoding='utf-8') as file:
    w = csv.writer(file)
    for data in results:
        w.writerow(data)
