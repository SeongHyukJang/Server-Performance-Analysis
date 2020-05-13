import delegator
import lauda
import logging
import statistics
import json

class Measurement:

    def __init__(self, _language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False):
        self.language = _language
        self.version_cmd = _version_cmd
        self.run_cmd = _run_cmd
        self.compile_cmd = _compile_cmd
        self.debug = _debug

    def run(self):

        print(f"[{self.language}]")

        if self.compile_cmd:
            cmd_compile = delegator.run(self.compile_cmd)  
            if self.debug or cmd_compile.return_code is not 0:
                logging.info(cmd_compile.out)

        print(f"Version :  {delegator.run(self.version_cmd).out.splitlines()[0]}")

        times = []
        count = 0

        while count < 10:
            count += 1

            stopWatch = lauda.StopWatch()
            stopWatch.start()
            delegator.run(self.run_cmd)
            stopWatch.stop()
            times.append(int(stopWatch.elapsed_time * 1000))

        print('\n')

        result = [self.language]
        result.extend(times)
        return result

def selectIterations(server,resource,method):

    print("\n=============================================\n\n")
    print("Server : ",server)
    print("resource : ", resource)
    print("method : ", method)

    if server == "python":
        folder = "toPython"
        end = 'PY'
    elif server == 'javascript':
        folder = "toJavascript"
        end = 'JS'

    languages = [
                #_language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False
                ["Python 3", "python --version", "python " + folder + "/" + method + resource + end + ".py"],
                ["JS (node)", "node --version", "node " + folder + "/" + method + resource + end + ".js"],
                ["curl", "curl --version", folder + "/" + method + resource + end + ".sh"]
            ]
    return languages
    


def writeResults(server, results,resource, method):
    with open('clientResults.json','r') as file:
        data = json.load(file)

    data['ServerLanguage'][server][resource][method] = list(results)

    with open('clientResults.json','w') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)