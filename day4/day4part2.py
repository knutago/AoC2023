import re
import numpy as np
import pandas as pd

f = open('day4input.txt','r')
lines = f.readlines()
f.close()

scores = []
cards = []
matches = []
for line in lines:
    str = line.split(':')
    card = int(re.findall('\d+',str[0])[0])
    cards.append(card)
    nums = str[1].split('|')
    win_nums = np.array(re.findall('\d+',nums[0]), dtype=int)
    pick_nums = np.array(re.findall('\d+',nums[1]), dtype=int)

    #print(card,len(pick_nums),len(np.unique(pick_nums)),pick_nums.min(),pick_nums.max())
    
    h, bine = np.histogram(np.concatenate([win_nums, pick_nums]), bins = np.linspace(1,100, 100, dtype=int))
    
    nmatch = len(h[h > 1])
    matches.append(nmatch)
    if nmatch > 0:
        score = 2**(nmatch-1)
    else:
        score = 0

    scores.append(score)


df = pd.DataFrame(list(zip(cards, matches)), columns = ['Number','Matches'])
df['Copies'] = 0

window = 10
for i in range(len(df)):
    df.loc[i, 'Copies'] += 1
    nextra = 0
    if i>0:
        dfp = df.loc[max(0,i-window):i-1]
        keep = dfp['Matches'] - np.flip(np.array(range(len(dfp)))+1) >= 0
        nextra = dfp.loc[keep,'Copies'].sum()
        df.loc[i, 'Copies'] += nextra
    #print('Processed card',i+1)

print(df['Copies'].sum())
