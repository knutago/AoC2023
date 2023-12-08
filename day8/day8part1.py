import re
import numpy as np
import pandas as pd

f = open('day8input.txt','r')
line = f.readline()
f.close()

dirs = line.strip()

df = pd.read_csv('day8input.txt', names = ['start', 'L', 'R'], sep='\s+\=|,', skiprows=1, index_col = 'start')
for i in df.index:
    df.loc[i, 'L'] = df.loc[i, 'L'][2:]
    df.loc[i, 'R'] = df.loc[i, 'R'][1:-1]

df['i']=np.arange(786,dtype=int)

def doiter(start,dirs,step):

    ind=start
    for dir in dirs:
        nextind = df.loc[ind, dir]
        ind = nextind
        if ind=='ZZZ':
            print('Completed in ',step)
            return(ind,step)
        step += 1
    return(ind,step)

ind = 'AAA'
step=1
els=[df.loc[ind,'i']]
steps=[step]
for i in range(100):
    ind, step = doiter(ind,dirs,step)
    els.append(df.loc[ind,'i'])
    steps.append(step)

