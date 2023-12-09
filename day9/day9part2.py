import re
import numpy as np

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
        
def pderiv(arr):
    newarr=[0]
    for i in range(1,len(arr)):
        sumval = arr[i]-newarr[-1]
        newarr.append(sumval)
    return(np.array(newarr))
           
preds = []
for line in lines:
    arr = np.array(re.findall(r'-?\d+',line),dtype=int)
    
    cont = 1
    firstnum=[arr[0]]
    #print(arr)
    while cont:
        narr = deriv(arr)
        firstnum.append(narr[0])
        if (narr==0).all():
            cont=0
        else:
            arr=narr
    predarr = pderiv(np.flip(firstnum))
    preds.append(predarr[-1])
    
print(np.array(preds).sum())
