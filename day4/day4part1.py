import re
import numpy as np

f = open('day4input.txt','r')
lines = f.readlines()
f.close()

scores = []
for line in lines:
    str = line.split(':')
    card = int(re.findall('\d+',str[0])[0])
    nums = str[1].split('|')
    win_nums = np.array(re.findall('\d+',nums[0]), dtype=int)
    pick_nums = np.array(re.findall('\d+',nums[1]), dtype=int)

    #print(card,len(pick_nums),len(np.unique(pick_nums)),pick_nums.min(),pick_nums.max())
    
    h, bine = np.histogram(np.concatenate([win_nums, pick_nums]), bins = np.linspace(1,100, 100, dtype=int))
    
    nmatch = len(h[h > 1])
    if nmatch > 0:
        score = 2**(nmatch-1)
    else:
        score = 0

    scores.append(score)

print(np.array(scores, dtype=int).sum())
