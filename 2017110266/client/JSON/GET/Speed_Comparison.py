import Measurements
import csv

print("\n========== Comparison =========")
print("GET JSON")

server = input("Select server : ")

print("============ HTTP GET =============")

languages = [
    #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
    ["Python 3", "python --version", "python TestingGET.py"],
    ["JS (node)", "node --version", "node TestingGET.js"],
    ["curl", "curl --version", "./TestingGET.sh"]
]

results = [['Language', 'best', 'worst', 'median']]

for language in languages:
    results.append(Measurements.Measurement(*language).run())

if server == "py":
    with open('python_results.csv','w',newline='',encoding='utf-8') as file:
        w = csv.writer(file)
        for data in results:
            w.writerow(data)

elif server == "js":
    with open('js_results.csv','w',newline='',encoding='utf-8') as file:
        w = csv.writer(file)
        for data in results:
            w.writerow(data)