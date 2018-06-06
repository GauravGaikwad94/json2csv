import pandas as pd
import json


#a_dict = {'a': 'a value', 'b': {'b.1': 'b.1 value'}}
with open('sample.json') as f:
    a_dict = json.load(f)
data = {}
def iterate(dictionary,key1):
    
    for key, value in dictionary.items():
        if isinstance(value, dict):
            iterate(value,key1+key+'_')
            continue
        elif isinstance(value, list):
            for i in value:
                iterate(i,key1+key+'_')
                #print("i",i)
        else :
            print('key {!r} -> value {!r}'.format(key, value))
            print()
            data[key1+key]=value
    print("data",data)
    #print('key {!r} -> value {!r}'.format(key, value))
    #print()
 
iterate(a_dict,'')
df = pd.DataFrame.from_dict(data, orient='index').T.to_csv('data.csv', index=False)