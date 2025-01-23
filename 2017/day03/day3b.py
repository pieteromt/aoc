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

def calc_value(cache, t):
    r,c = t
    sum = 0
    for dr in range(-1,2):
        for dc in range(-1,2):
            if (dr == 0) and (dc == 0): # redundant, since (r,c) not in cache yet...
                continue
            if (r+dr,c+dc) in cache:
                sum += cache[(r+dr,c+dc)]
    return sum

# returns the first value written larger than 'goal'
def generate(goal):
    d = 0
    r,c = 0,0
    i = 0
    cache = {}
    t = (r,c)
    i += 1
    cache[t] = i
    while True:
        if i > goal:
            return i
        t1 = next_pos(d,t)
        if not t1 in cache:
            i = calc_value(cache, t1)
            cache[t1] = i
            d = (d+1)%4  # rotate left
            t = t1
        else:
            d = (d+3)%4  # rotate back (keep same direction)

def process(data):
    for d in data:
        i = generate(d)
        print("First value written larger than " + str(d) + " is " + str(i))

def day3(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

