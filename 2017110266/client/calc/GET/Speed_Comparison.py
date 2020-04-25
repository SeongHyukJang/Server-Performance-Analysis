import Measurements
import csv

print("\n========== Comparison =========")
print("GET calc")

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


with open('python_results.csv','w',newline='',encoding='utf-8') as file:
    w = csv.writer(file)
    for data in results:
        w.writerow(data)


# with open('js_results.csv','w',newline='',encoding='utf-8') as file:
#     w = csv.writer(file)
#     for data in results:
#         w.writerow(data)