import json

new_data = {
    'id' : 2,
    'usrID' : '2017000000',
    'usrPW' : '3221',
    'name' : '홍길동',
    'age': 23
}
j_data = new_data


with open('data.json','a') as f:
    json.dump(j_data, f, ensure_ascii=False, indent = 4)
    #print('type = ', type(s))

'''
try:
    with open('data.json', 'r') as f:
        s = json.load(f)
except:
    s = []
s.append(j_data)


with open('data.json', 'w') as f:
    json.dump(s,f, ensure_ascii=False, indent=4)
'''


'''
[
    {
        "id": 1, 
        "usrID": "2017110266",
        "usrPW": "1234",
        "name": "장성혁",
        "age": 25
    }
]
'''