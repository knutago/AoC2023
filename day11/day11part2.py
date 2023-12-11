import numpy as np
import re
import pandas as pd
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

f = open('day11input.txt','r')
lines = f.readlines()
f.close()

imap = np.empty((len(lines[0])-1,len(lines)), dtype=str_)
for i,line in zip(range(len(lines)), lines):
    imap[i,:] = list(line.strip())

emptyrows=[]
emptycols=[]
expand = 1000000-1

for i in range(imap.shape[0]):
    if np.all(imap[i,:] == '.'):
        emptyrows.append(i)
for j in range(imap.shape[1]):
    if np.all(imap[:,j] == '.'):
        emptycols.append(j)

emptyrows = np.array(emptyrows)
emptycols = np.array(emptycols)
#gmap = np.insert(imap,emptyrows,'.',axis=0)
#gmap = np.insert(gmap,emptycols,'.',axis=1)

ii,jj = np.where(imap=='#')

for ind,i,j in zip(range(len(ii)),ii,jj):
    ii[ind] += len(emptyrows[i > emptyrows])*expand
    jj[ind] += len(emptycols[j > emptycols])*expand

    
d = {'num': np.array(range(1,len(ii)+1)),'x': jj, 'y': ii}
df = pd.DataFrame(data=d)


for i in range(len(df)):
    x0 = df.loc[i, 'x']
    y0 = df.loc[i, 'y']
    dx = df['x'] - x0
    dy = df['y'] - y0
    dist = np.abs(dx) + np.abs(dy)
    for ind,dd in zip(dist.index,dist):
        df.loc[i, str(ind+1)] = dd


print(df.loc[:, '1':].sum().sum()/2)


#9918828.0
