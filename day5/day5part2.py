import re
import numpy as np
import io
import pandas as pd
#from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

def domap(numin,mapin):
    i = (numin >= mapin['Source']) & (numin < mapin['Source'] + mapin['Length'])
    if any(i):
        numout = (mapin[i]['Destination'] + numin - mapin[i]['Source']).values[0]
    else:
        numout = numin

    return(numout)

f = open('day5input.txt','r')
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]

seeds = np.array(re.findall('\d+',lines[0].split(':')[1]), dtype=int)
s2s = lines.index('seed-to-soil map:')
s2f = lines.index('soil-to-fertilizer map:')
f2w = lines.index('fertilizer-to-water map:')
w2l = lines.index('water-to-light map:')
l2t = lines.index('light-to-temperature map:')
t2h = lines.index('temperature-to-humidity map:')
h2l = lines.index('humidity-to-location map:')
s2smap = pd.read_csv(io.StringIO('\n'.join(lines[(s2s+1):(s2f-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
s2fmap = pd.read_csv(io.StringIO('\n'.join(lines[(s2f+1):(f2w-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
f2wmap = pd.read_csv(io.StringIO('\n'.join(lines[(f2w+1):(w2l-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
w2lmap = pd.read_csv(io.StringIO('\n'.join(lines[(w2l+1):(l2t-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
l2tmap = pd.read_csv(io.StringIO('\n'.join(lines[(l2t+1):(t2h-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
t2hmap = pd.read_csv(io.StringIO('\n'.join(lines[(t2h+1):(h2l-1)])),names=['Destination','Source','Length'], delim_whitespace=True)
h2lmap = pd.read_csv(io.StringIO('\n'.join(lines[(h2l+1):len(lines)])),names=['Destination','Source','Length'], delim_whitespace=True)

startseeds = seeds[np.array(range(int(len(seeds)/2)), dtype=int)*2]
seedranges = seeds[np.array(range(int(len(seeds)/2)), dtype=int)*2+1]

def dos2lmap(seed1):
    soil1 = domap(seed1,s2smap)
    fert1 = domap(soil1,s2fmap)
    water1 = domap(fert1,f2wmap)
    light1 = domap(water1,w2lmap)
    temp1 = domap(light1,l2tmap)
    hum1 = domap(temp1,t2hmap)
    loc1 = domap(hum1,h2lmap)

    return(loc1)


locations = []
seedout = []
#for seed1,seedrange1 in zip(startseeds, seedranges):
#    seed2 = seed1 + seedrange1-1
    
#    res = minimize_scalar(dos2lmap, bounds=(seed1,seed2), method='bounded')
#
#    locations.append(res.fun)
#    seedout.append(res.x)

#for s1,l1 in zip(seedout,locations):
#    print(s1,l1)

#smin = seedout[-1]
nels = 1000
#xx = np.linspace(int(smin)-nels,int(smin)+nels, dtype=int)
#yy = np.zeros(len(xx), dtype=int)
#for x,i in zip(xx,range(len(xx))):
#    yy[i] = dos2lmap(x)

#plt.plot(xx,yy)

location1=[]
location2=[]
for seed1,seed2 in zip(startseeds,startseeds + seedranges):
    location1.append(dos2lmap(seed1))
    location2.append(dos2lmap(seed2))


i=5
seed1 = startseeds[i]
seed2 = startseeds[i] + seedranges[i]
xx = np.linspace(seed1,seed2, nels, dtype=int)
yy = np.zeros(len(xx), dtype=int)
for x,i in zip(xx,range(len(xx))):
    yy[i] = dos2lmap(x)

#plt.plot(xx,yy)

seed1 = 1799900000+4000
seed2 = 1799900000+6000
xx = np.linspace(seed1,seed2, seed2-seed1, dtype=int)
yy = np.zeros(len(xx), dtype=int)
for x,i in zip(xx,range(len(xx))):
    yy[i] = dos2lmap(x)

print(yy.min())
