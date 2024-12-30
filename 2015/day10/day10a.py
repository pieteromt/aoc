import sys

from itertools import groupby

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def calc_next(s):
    a = [''.join(g) for _,g in groupby(s)]
    result = ""
    for d in a:
        result += str(len(d)) + d[0]
    return result
        
def do_loop(s,nr):
    for i in range(nr):
        s = calc_next(s)
    print(len(s))

def process(data):
    for s in data:
        do_loop(s,40)
    
def day10(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])

