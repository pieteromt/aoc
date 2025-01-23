import sys

import math

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
# direction d
# 0 = right
# 1 = up
# 2 = left
# 3 = down
def next_pos(d,t):
    r,c = t
    if d == 0:
        return r,c+1
    elif d == 1:
        return r-1,c
    elif d == 2:
        return r,c-1
    else:
        return r+1,c

# returns the coordinates of box 'goal'
def generate(goal):
    d = 0
    r,c = 0,0
    i = 0
    cache = {}
    t = (r,c)
    i += 1
    cache[t] = i
    while True:
        if i == goal:
            return t
        t1 = next_pos(d,t)
        if not t1 in cache:
            i += 1
            cache[t1] = i
            d = (d+1)%4  # rotate left
            t = t1
        else:
            d = (d+3)%4  # rotate back (keep same direction)

def process(data):
    for d in data:
        t = generate(d)
        r,c = t
        steps = abs(r) + abs(c)
        print("Square " + str(d) + " is carried in " + str(steps) + " steps.")

def day3(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

