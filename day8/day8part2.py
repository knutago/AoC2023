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
lastletter = [ind[-1] for ind in df.index]
df['last'] = lastletter

cont=1
def doiter(starts,dirs,step):

    inds=starts
    for dir1 in dirs:
        nextinds = df.loc[inds, dir1]
        inds = nextinds
        if (df.loc[inds,'last']=='Z').all():
            cont = 0
            print('Completed in ', step)
            return(inds,step,cont)
        else:
            cont = 1
            step += 1

    return(inds,step,cont)

starts = df[df['last']=='A'].index
inds = starts
step=1
while cont:
    inds, step, cont = doiter(inds,dirs,step)
    print(df.loc[inds,'last'])
