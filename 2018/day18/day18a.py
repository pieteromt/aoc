import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def valid(r,c,h,w):
    return (r>=0) and (r < h) and (c>=0) and (c < w)

def neighbour_range(r,c,h,w):
    for dr in range(-1,2):
        for dc in range(-1,2):
            if (dr == 0) and (dc == 0):
                continue
            if valid(r+dr,c+dc,h,w):
                yield r+dr,c+dc

def calc(data, r, c):
    h = len(data)
    w = len(data[0])
    gr = 0
    tr = 0
    lu = 0
    for t in neighbour_range(r,c,h,w):
        r1,c1 = t
        ch = data[r1][c1]
        if (ch == "."):
            gr += 1
        elif (ch == "|"):
            tr += 1
        else:
            lu += 1
    ch = data[r][c]
    if ch == ".":
        if tr >= 3:
            return "|"
    elif ch == "|":
        if lu >= 3:
            return "#"
    else: # ch == "#":
        if (lu == 0) or (tr == 0):
            return "."
    return ch

def step(data):
    grid = []
    for r in range(len(data)):
        row = ""
        for c in range(len(data[0])):
            row += calc(data, r, c)
        grid.append(row)
    return grid
    
def show(data):
    for d in data:
        print(d)
    print("")

def count(data):
    tr = 0
    lu = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            ch = data[r][c]
            if ch == "|":
                tr += 1
            elif ch == "#":
                lu += 1
    res = tr * lu
    print("Resource value: " + str(res))

def process(data):
    show(data)
    for i in range(10):
        print("After " + str(i+1) + " minutes:")
        data = step(data)
        show(data)
    count(data)

def day18(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18 input.txt") 
    else:
    	day18(sys.argv[1])
