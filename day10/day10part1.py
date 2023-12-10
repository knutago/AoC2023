import numpy as np
import re

f = open('day10input.txt','r')
lines = f.readlines()
f.close()

imap = np.empty((len(lines[0])-1,len(lines)), dtype=str_)
for i,line in zip(range(len(lines)), lines):
    imap[i,:] = list(line.strip())

start = np.where(imap=='S')
y=start[0][0]
x=start[1][0]

#tile = {
#    'x': start[0][0],
#    'y': start[1][0],
#    'o': 'S',
#    'N': imap[y,x-1], 
#    'S': imap[y,x+1],
#    'E': imap[y+1,x],
#    'W': imap[y-1,x]
#}

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = ''
        self.W = imap[y,x-1] 
        self.E = imap[y,x+1]
        self.S = imap[y+1,x]
        self.N = imap[y-1,x]
        self.orig = imap[y,x]
        self.distance = 0

    def update(self):
        if self.x > 0:
            self.W = imap[self.y,self.x-1]
        else:
            self.W = '.'
        if self.x < imap.shape[1]-1:
            self.E = imap[self.y,self.x+1]
        else:
            self.E = '.'
        if self.y < imap.shape[0]-1:
            self.S = imap[self.y+1,self.x]
        else:
            self.S = '.'
        if self.y > 0:
            self.N = imap[self.y-1,self.x]
        else:
            self.N = '.'
        self.orig = imap[self.y,self.x]
    
    def move(self,direction):
        match direction:
            case 'N':
                self.y -= 1
                self.direction = 'N'
            case 'S':
                self.y += 1
                self.direction = 'S'

            case 'E':
                self.x += 1
                self.direction = 'E'
                
            case 'W':
                self.x -= 1
                self.direction = 'W'
                
            case _:
                print('Direction mu be N, S, E, or W')

        self.update()
        self.distance += 1
        
    def legalpipesN(self):
        if self.orig == '|':
            pipes = ['|','7','F','S']
        
    def legalmoves(self):
        moves = []
        origs = ['|','L','J','S']
        dests = ['|','7','F','S']
        if (self.orig in origs) & (self.N in dests) & (self.direction != 'S'):
            moves.append('N')
        origs = ['|','7','F','S']
        dests = ['|','L','J','S']
        if (self.orig in origs) & (self.S in dests) & (self.direction != 'N'):
            moves.append('S')
        origs = ['-','F','L','S']
        dests = ['-','7','J','S']
        if (self.orig in origs) & (self.E in dests) & (self.direction != 'W'):
            moves.append('E')
        origs = ['-','7','J','S']
        dests = ['-','F','L','S']
        if (self.orig in origs) & (self.W in dests) & (self.direction != 'E'):
                moves.append('W')

        return(moves)

tile = Tile(x,y)
tile.move('S') # initial move

while tile.orig != 'S':
    #print(tile.legalmoves())
    #print(tile.distance)
    tile.move(tile.legalmoves()[0])

print(tile.distance/2)
