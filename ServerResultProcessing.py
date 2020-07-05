import os
import json
import statistics
from matplotlib import pyplot as plt

os.chdir('./server/Linux')

with open('ServerSpeedResult.json') as file:
    data = json.load(file)

py_data = data['ServerLanguage']['python']
js_data = data['ServerLanguage']['javascript']
languages = ['Python 3', 'JS (node)']

def makeData(resource,method):
    temp_py = py_data[resource][method]
    temp_js = js_data[resource][method]

    best = list(map(lambda x : float(format(x,'.2f')),[min(temp_py), min(temp_js)]))
    worst = list(map(lambda x : float(format(x,'.2f')),[max(temp_py), max(temp_js)]))
    median = list(map(lambda x : float(format(x,'.2f')),[statistics.median(temp_py), statistics.median(temp_js)]))

    return [best,worst,median]

def makePlot(fig,best,worst,median,title):
    fig.rcParams["figure.figsize"] = (8,8)
    width = 0.3

    index = [0,1]
    fig.barh(index, best, width)

    for i,v in enumerate(index):
        s = str(best[i])
        fig.text(best[i],v,s,horizontalalignment='left',verticalalignment='center')

    index = list(map(lambda x: x+width,index))
    fig.barh(index,worst,width)

    for i,v in enumerate(index):
        s = str(worst[i])
        fig.text(worst[i],v,s,horizontalalignment='left',verticalalignment='center')

    index = list(map(lambda x: x+width, index))
    fig.barh(index,median,width)

    for i,v in enumerate(index):
        s = str(median[i])
        fig.text(median[i],v,s,horizontalalignment='left',verticalalignment='center')

    fig.xlim(0,max(worst) + max(best) )
    fig.yticks([0.2,1.3],languages)
    fig.ylabel('Server')
    fig.xlabel('Time(ms)')
    fig.title(title, fontsize = 25, fontweight = "bold")
    fig.legend(['best','worst','median'])
    fig.savefig(title+'.png',dpi=300)
    fig.clf()

json_get = makeData('json','GET')
json_post = makeData('json','POST')
calc_get = makeData('calc','GET')
html_get = makeData('html','GET')

os.chdir('../../results/Server Speed')

makePlot(plt,json_get[0],json_get[1],json_get[2],'GET JSON')
makePlot(plt,json_post[0],json_post[1],json_post[2],'POST JSON')
makePlot(plt,calc_get[0],calc_get[1],calc_get[2],'GET Calc')
makePlot(plt,html_get[0],html_get[1],html_get[2],'GET HTML')