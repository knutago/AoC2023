import re
import numpy as np
#import pandas as pd

f = open('day9input.txt','r')
#f = open('day9test.txt','r')
lines = f.readlines()
f.close()

def deriv(arr):
    newarr = []
    for i in range(len(arr)-1):
        diff = arr[i+1]-arr[i]
        newarr.append(diff)
    return(np.array(newarr))
        
def ideriv(arr):
    newarr=[0]
    for i in range(1,len(arr)):
        sumval = arr[i]+newarr[-1]
        newarr.append(sumval)
    return(np.array(newarr))
           
preds = []
for line in lines:
    arr = np.array(re.findall(r'-?\d+',line),dtype=int)
    
    cont = 1
    lastnum=[arr[-1]]
    #print(arr)
    while cont:
        narr = deriv(arr)
        lastnum.append(narr[-1])
        if (narr==0).all():
            cont=0
        else:
            arr=narr
        #print(narr)
    predarr = ideriv(np.flip(lastnum))
    preds.append(predarr[-1])
    #print(lastnum)
    
print(np.array(preds).sum())
