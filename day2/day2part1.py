import re
import pandas as pd

f = open('day2input.txt','r')
lines = f.readlines()
f.close()

sum = 0
cube_dict = {
    'red': 0,
    'green': 0,
    'blue': 0,
    }
cube_max = {
    'red': 12,
    'green': 13,
    'blue': 14,
    }

df = pd.DataFrame(data = {'id' : 0,'red': 0,'green': 0,'blue': 0}, index = range(100))
sum=0
for line,i in zip(lines,range(len(lines))):
    gamebool = True
    str = line.split(':')
    game = int(re.findall(r'\d+',str[0])[0])
    sets = str[1].split(';')
    df['id'].loc[i] = game
    for set in sets:
        cube_dict = dict.fromkeys(cube_dict, 0)
        pulls = set.split(',')
        for pull in pulls:
            number = re.findall(r'\d+',pull)
            color = re.findall(r'red|green|blue',pull)
            cube_dict[color[0]] = int(number[0])
        
        for key in cube_dict.keys():
            if cube_dict[key] > df[key].iloc[i]:
                df[key].iloc[i] = cube_dict[key]
            if cube_dict[key] > cube_max[key]:
                print(key,cube_dict[key],cube_max[key])
                gamebool = False
    if gamebool:
        sum += game

    print(line,game,gamebool)

print(sum)
dfok = df[(df['red']<=12) & (df['green']<=13) & (df['blue']<=14)]
dfbad = df[(df['red']>12) | (df['green']>13) | (df['blue']>14)]
print(dfbad)
print(dfok['id'].sum())
