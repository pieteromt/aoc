import sys

visit = {}  # histogram of locations (row,col)

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        for d in line:
            data.append(d)  # direction
    f.close()
    return data

def add_visit(t):
    global visit
    if t in visit:
        visit[t] += 1
    else:
        visit[t] = 1

def new_pos(r,c,d):
    if d == '>':
        c += 1
    elif d == '<':
        c -= 1
    elif d == 'v':
        r += 1
    elif d == '^':
        r -= 1
    else:
        print("error: " + d)
        exit()
    return r,c 

def process(data):
    r0,c0 = 0,0
    r1,c1 = 0,0
    add_visit((r0,c0))   # first house
    add_visit((r1,c1))   # first house
    santa = True
    for d in data:
        if santa:
            r0, c0 = new_pos(r0,c0,d)
            add_visit((r0,c0))  # next house
        else:
            r1, c1 = new_pos(r1,c1,d)
            add_visit((r1,c1))  # next house
        santa = not santa

def day3(fname):
    data = read_data(fname)
    process(data)
    for t in visit:
        print(str(t) + " : " + str(visit[t]))
    print("#houses: " + str(len(visit)))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

