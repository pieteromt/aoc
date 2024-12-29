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

def process(data):
    r = 0
    c = 0
    add_visit((r,c))   # first house
    for d in data:
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
        add_visit((r,c))  # next house

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

