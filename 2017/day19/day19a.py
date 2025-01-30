import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.replace('\n','')
        data.append(line)
    f.close()
    return data
    
# direction
# 0 = down (south)
# 1 = left (west)
# 2 = up (north)
# 3 = right (east)

# returns (row,col,dir)
def get_startpos(data):
    row = data[0]
    for i in range(len(row)):
        if row[i] == '|':
            return (0,i,0)
    return (0,0,0) # error

# returns the next position
def get_next(data, t):
    r,c,d = t
    ch0 = data[r][c]
    if d == 0:
        r += 1
    elif d == 1:
        c -= 1
    elif d == 2:
        r -= 1
    else: # d == 3
        c += 1
    ch1 = data[r][c]
    if ch1 == ' ':
        # we're done
        r,c,d = 0,0,0
    elif (ch1 == '|') or (ch1 == '-'):
        pass # keep on going
    elif (ch1 == '+'):  # change dir
        if (d == 0) or (d == 2):
            if data[r][c-1] != ' ':
                d = 1
            else:
                d = 3
        else: # d == 1 or 3
            if data[r-1][c] != ' ':
                d = 2
            else:
                d = 0
    else: # letter
        print(ch1,end='')
    return (r,c,d)

def walk(data):
    t = get_startpos(data)
    print("Letters: ",end='')
    nr = 0
    while t != (0,0,0):
        t = get_next(data, t)
        nr += 1
    print("")
    print("Steps: " + str(nr))

def process(data):
    walk(data)

def day19(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])
