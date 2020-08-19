import os
import csv

def postProcess(path):
    os.chdir('./' + path)

    py_cpu = []
    js_cpu = []
    go_cpu = []

    py_mem = []
    js_mem = []
    go_mem = []

    with open('go-cpu.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Go CPU'
            go_cpu.append(row)

    with open('go-memory.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Go Memory'
            go_mem.append(row)
                
    with open('javascript-cpu.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Javascript CPU'
            js_cpu.append(row)

    with open('javascript-memory.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Javascript Memory'
            js_mem.append(row)

    with open('python-cpu.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Python CPU'
            py_cpu.append(row)
            
    with open('python-memory.csv') as f:
        myreader = csv.reader(f)
        for row in myreader:
            if row[2] != 'label':
                row[2] = 'Python Memory'
            py_mem.append(row)

            
    cpu_time_py =  int(py_cpu[1][0]) - int(go_cpu[1][0])
    cpu_time_js =  int(js_cpu[1][0]) - int(go_cpu[1][0])
            
    for i in range(1,len(py_cpu)):
        py_cpu[i][0] = str(int(py_cpu[i][0]) - cpu_time_py)

    for i in range(1,len(js_cpu)):
        js_cpu[i][0] = str(int(js_cpu[i][0]) - cpu_time_js)
        
    mem_time_py = int(py_mem[1][0]) - int(go_mem[1][0])
    mem_time_js = int(js_mem[1][0]) - int(go_mem[1][0])

    for i in range(1, len(py_mem)):
        py_mem[i][0] = str(int(py_mem[i][0]) - mem_time_py)
        
    for i in range(1, len(js_mem)):
        js_mem[i][0] = str(int(js_mem[i][0]) - mem_time_js)


    with open('cpu-usage.csv','w') as f:
        mywriter = csv.writer(f)
        for row in py_cpu:
            mywriter.writerow(row)
        for row in js_cpu:
            if row[0] != 'timeStamp':
                mywriter.writerow(row)
        for row in go_cpu:
            if row[0] != 'timeStamp':
                mywriter.writerow(row)

    with open('memory-usage.csv', 'w') as f:
        mywriter = csv.writer(f)
        for row in py_mem:
            mywriter.writerow(row)
        for row in js_mem:
            if row[0] != 'timeStamp':
                mywriter.writerow(row)
        for row in go_mem:
            if row[0] != 'timeStamp':
                mywriter.writerow(row)

    os.chdir('../')

os.chdir('./jmeter/cpu&memory')

postProcess('get-json')
postProcess('get-calc')
postProcess('get-html')
postProcess('post-json')