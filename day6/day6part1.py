import re
import numpy as np

f = open('day6input.txt','r')
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]

times = np.array(re.findall('\d+',lines[0].split(':')[1]), dtype=int)
dists = np.array(re.findall('\d+',lines[1].split(':')[1]), dtype=int)

# d = v*t
# d = x*(t-x) --> -x**2 + xt - d =0
# x_root = (-t +/- sqrt(t**2 - 4*d)) / (-2)

x1 = (times - np.sqrt(times**2 - 4*dists))/2
x2 = (times + np.sqrt(times**2 - 4*dists))/2

n = x2.astype(int) - x1.astype(int)
print(np.prod(n))
