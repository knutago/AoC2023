import numpy as np
import re
import itertools

f = open('day12input.txt','r')
lines = f.readlines()
f.close()


countall = 0
for line in lines:
    str1 = line.split(' ')
    pattern = str1[0]
    sz=np.array(str1[1].strip().split(','), dtype=int)
    length = len(pattern)

    dd = length - np.sum(sz)
    spaces = [range(0,dd)] + [range(1,dd+1)]*(len(sz)-1)
    inds = []
    strs = []
    inds = [c for c in itertools.product(*spaces) if np.sum(c) <= dd]
    for ind in inds:
        str1=''
        for ii,sz1 in zip(ind,sz):
            str1 += ('.'*ii + '#'*sz1)
        str1 = str1.ljust(length,'.')
        strs.append(str1)


    count1 = 0
    matches = []
    for str1 in strs:
        ok=[]
        for s in range(len(pattern)):
            if pattern[s] != '?':
                if pattern[s] == str1[s]:
                    ok.append(1)
                else:
                    ok.append(0)
        if np.array(ok).all():
            count1 += 1
            matches.append(str1)
    #print(line,count1)
            
    countall += count1

print(countall)
