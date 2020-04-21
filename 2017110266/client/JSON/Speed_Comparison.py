import Measurements

print("\n========== Comparison =========")
print("Iterations : Python (8000)")
print("JSON")

print("============ HTTP GET =============")

languages = [
    #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
    ["Python 3", "python --version", "python GET/TestingGET.py"],
    ["JS (node)", "node --version", "node GET/TestingGET.js"],
    #["Bash", "bash --version", "souce GET/TestingGET.sh"]
]

for language in languages:
    Measurements.Measurement(*language).run()


print("============ HTTP POST ============")

languages = [
    #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
    ["Python 3", "python --version", "python POST/TestingPOST.py"],
    ["JS (node)", "node --version", "node POST/TestingPOST.js"],
]

for language in languages:
    Measurements.Measurement(*language).run()