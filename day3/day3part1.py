import numpy as np
import re

f = open('day3input.txt','r')
array = f.readlines()
f.close()

partnumbers = []
for row,i in zip(array,range(len(array))):
    numb_it = re.finditer(r'\d+',row)
    for match_obj in numb_it:
        goodpart = False
        span = match_obj.span()
        subrow0 = array[i][max(0,span[0]-1):min(len(row)-1,span[1]+1)]
        if span[0] > 0:
            if row[span[0]-1] != '.':
                goodpart = True
        if span[1] < (len(row)-1):
            if row[span[1]] != '.':
                goodpart = True
        if i > 0:
            subrowu = array[i-1][max(0,span[0]-1):min(len(row)-1,span[1]+1)]
            if subrowu != '':
                if subrowu != '.'*len(subrowu):
                    goodpart = True
                    
        if i < len(array)-1:
            subrowd = array[i+1][max(0,span[0]-1):min(len(row)-1,span[1]+1)]
            if subrowd != '':
                if subrowd != '.'*len(subrowd):
                    goodpart = True

        if not goodpart:
            if i>0:
                print(subrowu)
            print(subrow0)
            if i < len(array)-1:
                print(subrowd)
            print(goodpart,i,span)
            print('\n')
        if goodpart:
            partnumbers.append(match_obj.group())


print(np.array(partnumbers, dtype=int).sum())

        
