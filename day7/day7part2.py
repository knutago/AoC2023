import re
import numpy as np
import pandas as pd

df = pd.read_csv('day7input.txt', names = ['hand', 'bid'], sep=' ')

cardval = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14 }

def handrank(cards):
    h, bine = np.histogram(cards, bins = np.linspace(1,15,15, dtype=int))
    if 5 in h:
        rank = 7 #5K
    elif 4 in h:
        rank = 6 #4K
    elif (3 in h) & (2 in h):
        rank = 5 #FH
    elif (3 in h) & (1 in h):
        rank = 4 #3K
    elif len(h[h==2]) == 2:
        rank = 3 #2P
    elif (2 in h) & (len(h[h==1]) == 3):
        rank = 2 #1P
    else:
        rank = 1 # HC

    return(rank)
    
def wildrank(cards):
    wild = (cards==1)
    ranks = []
    for card in cardval:
        cards[wild] = cardval[card]
        ranks.append(handrank(cards))

    return(max(ranks))

def subrank(df):
    df.sort_values(['card1', 'card2', 'card3', 'card4', 'card5'], ascending = False, inplace=True, ignore_index=True)

    return(df)

for i in range(len(df)):
    df.loc[i, 'card1'] = cardval[df.loc[i, 'hand'][0]]
    df.loc[i, 'card2'] = cardval[df.loc[i, 'hand'][1]]
    df.loc[i, 'card3'] = cardval[df.loc[i, 'hand'][2]]
    df.loc[i, 'card4'] = cardval[df.loc[i, 'hand'][3]]
    df.loc[i, 'card5'] = cardval[df.loc[i, 'hand'][4]]
    if 'J' in df.loc[i, 'hand']:
        df.loc[i, 'handrank'] = wildrank(df.loc[i, 'card1':'card5'])
    else:
        df.loc[i, 'handrank'] = handrank(df.loc[i, 'card1':'card5'])

df5k = subrank(df[df['handrank']==7])
df4k = subrank(df[df['handrank']==6])
dffh = subrank(df[df['handrank']==5])
df3k = subrank(df[df['handrank']==4])
df2p = subrank(df[df['handrank']==3])
df2k = subrank(df[df['handrank']==2])
dfhc = subrank(df[df['handrank']==1])

dfout = pd.concat([df5k,df4k,dffh,df3k,df2p,df2k,dfhc], ignore_index=True)
dfout['rank']=np.flip(dfout.index+1)
winnings = dfout['rank']*dfout['bid']
print(winnings.sum())
