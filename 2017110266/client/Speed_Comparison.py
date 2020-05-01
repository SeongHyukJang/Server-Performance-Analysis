import Measurements

print("\n========== Comparison =========")
print("GET calc")

server = input("Select server : ")
resource = input("Select resource : ")
method = input("Select method : ")

results = []

languages = Measurements.selectIterations(server,resource,method)
for language in languages:
    results.append(Measurements.Measurement(*language).run())

Measurements.writeResults(server,results,resource,method)