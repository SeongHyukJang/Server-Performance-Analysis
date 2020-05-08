import Measurements

print("\n========== Comparison =========")
print("GET calc")

server = input("Select server (python/javascirpt) : ")
resource = input("Select resource (json/calc/html) : ")
method = input("Select method (get/post) : ")

results = []

languages = Measurements.selectIterations(server,resource,method)
for language in languages:
    results.append(Measurements.Measurement(*language).run())

Measurements.writeResults(server,results,resource,method)