import Measurements

print("\n========= Comparison =========")
print("Iterations : localhost:8080")

languages = [
    #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
    ["Python 3", "python --version", "python Testing.py"],
    #["JS (node)", "node --version", "node Testing.js"],
    #["C++", "g++ --version", "./Testing", "g++ Testiing.cpp -o Testing"],
    #["C", "gcc --version", "./Testing", "gcc Testing.c -o Testing"],
    #["C#", ]
]

for language in languages:
    Measurements.Measurement(*language).run()