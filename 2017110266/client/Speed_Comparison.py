import Measurements
import csv
import json
import os

print("\n========== Comparison =========")
print("GET calc")

server = input("Select server : ")
resource = input("Select resource : ")
method = input("Select method : ")


if server == "py":
    if resource == "calc":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GETcalc.py"],
                ["JS (node)", "node --version", "node GETcalc.js"],
                ["curl", "curl --version", "./GETcalc.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][0]['Python'][1]['calc'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

    elif resource == "json":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GETjson.py"],
                ["JS (node)", "node --version", "node GETjson.js"],
                ["curl", "curl --version", "./GETjson.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][0]['Python'][0]['JSON'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

        elif method == "post":
            print("============ HTTP POST ============")

            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python POSTjson.py"],
                ["JS (node)", "node --version", "node POSTjson.js"],
                ["curl", "curl --version", "./POSTjson.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json', 'r') as file:
                data = json.load(file)
            
            data[0]['language'][0]['Python'][0]['JSON'][0]['POST'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)
    
    elif resource == "html":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GEThtml.py"],
                ["JS (node)", "node --version", "node GEThtml.js"],
                ["curl", "curl --version", "./GEThtml.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][0]['Python'][2]['html'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

            


elif server == "js":
    if resource == "calc":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GETcalc.py"],
                ["JS (node)", "node --version", "node GETcalc.js"],
                ["curl", "curl --version", "./GETcalc.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][1]['JavaScript'][1]['calc'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

    elif resource == "json":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GETjson.py"],
                ["JS (node)", "node --version", "node GETjson.js"],
                ["curl", "curl --version", "./GETjson.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][1]['JavaScript'][0]['JSON'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

        elif method == "post":
            print("============ HTTP POST ============")

            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python POSTjson.py"],
                ["JS (node)", "node --version", "node POSTjson.js"],
                ["curl", "curl --version", "./POSTjson.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json', 'r') as file:
                data = json.load(file)
            
            data[0]['language'][1]['JavaScript'][0]['JSON'][0]['POST'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)
    
    elif resource == "html":
        if method == "get":
            print("============ HTTP GET =============")
            languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python GEThtml.py"],
                ["JS (node)", "node --version", "node GEThtml.js"],
                ["curl", "curl --version", "./GEThtml.sh"]
            ]

            results = [['Language', 'best', 'worst', 'median']]

            for language in languages:
                results.append(Measurements.Measurement(*language).run())

            print("Writing in python results")
            os.chdir('/home/jsh/GitHub/SWCON_Project/2017110266')
            with open('results.json','r') as file:
                data = json.load(file)
            
            data[0]['language'][1]['JavaScript'][2]['html'][0]['GET'] = str(results)

            with open('results.json','w') as file:
                json.dump(data,file,ensure_ascii=False,indent=4)