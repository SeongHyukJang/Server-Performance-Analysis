import os
import json
import statistics
from matplotlib import pyplot as plt

os.chdir('./client')
with open('ResponseTimeResult.json') as file:
    data = json.load(file)

Linux_Python = data['Server']['python']
languages = ['Python 3', 'JS (node)', 'curl']

def makeData(resource,method):
    temp = Linux_Python['resource'][resource]['method'][method]

    py_temp = temp[0][1:]
    js_temp = temp[1][1:]
    curl_temp = temp[2][1:]

    best = [min(py_temp),min(js_temp),min(curl_temp)]
    worst = [max(py_temp),max(js_temp),max(curl_temp)]
    median = [statistics.median(py_temp),statistics.median(js_temp),statistics.median(curl_temp)]

    return [best,worst,median]

def makePlot(fig,best,worst,median,title):
    fig.rcParams["figure.figsize"] = (8,8)
    width = 0.3
    
    index = [0,1,2]
    fig.barh(index,best,width)
    for i,v in enumerate(index):
        s = str(best[i])
        fig.text(best[i],v,s,horizontalalignment='left',verticalalignment='center')

    index = list(map(lambda x : x+width,index))
    fig.barh(index,worst,width )
    for i,v in enumerate(index):
        s = str(worst[i])
        fig.text(worst[i],v,s,horizontalalignment='left',verticalalignment='center')

    index = list(map(lambda x : x+width,index))
    fig.barh(index,median,width)
    for i,v in enumerate(index):
        s = str(median[i])
        fig.text(median[i],v,s,horizontalalignment='left',verticalalignment='center')

    fig.xlim(0,max(worst)+30)
    fig.yticks([0.3,1.3,2.3],languages)
    fig.ylabel('Client')
    fig.xlabel('Time (ms)')
    fig.title(title, fontsize = 25, fontweight = "bold")
    fig.legend(['best','worst','median'])
    fig.savefig(title+'.png',dpi=300)
    fig.clf()
        
json_get = makeData('json','GET')
json_post = makeData('json','POST')
calc_get = makeData('calc','GET')
html_get = makeData('html','GET')

os.chdir('../results/Response Time')

makePlot(plt,json_get[0],json_get[1],json_get[2],'GET JSON')
makePlot(plt,json_post[0],json_post[1],json_post[2],'POST JSON')
makePlot(plt,calc_get[0],calc_get[1],calc_get[2],'GET Calc')
makePlot(plt,html_get[0],html_get[1],html_get[2],'GET HTML')