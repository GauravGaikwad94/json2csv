import pandas as pd
import json
from pandas.io.json import json_normalize


#a_dict = {'a': 'a value', 'b': {'b.1': 'b.1 value'}}
with open('sample.json') as f:
    a_dict = json.load(f)
data = [{},{}]
def iterate(dictionary,key1,p):
    
    for key, value in dictionary.items():
        if isinstance(value, dict):
            iterate(value,key1+key+'_',p)
            continue
        elif isinstance(value, list):
            k = 0
            for i in value:
                iterate(i,key1+key+'_',k)
                k+=1
                #print("i",i)
        else :
            print('key {!r} -> value {!r}'.format(key, value))
            print()
            data[p][key1+key]=value
    print("data",data)
    #print('key {!r} -> value {!r}'.format(key, value))
    #print()
 
iterate(a_dict,'',0)
#d=json_normalize(a_dict)
#print(type(d))	
#df = pd.DataFrame.from_dict(data, orient='index').T.to_csv('data.csv', index=False)
df=pd.DataFrame(data)
df.to_csv('n.csv')
#d.to_csv('new.csv')
