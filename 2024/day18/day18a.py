import sys

sys.setrecursionlimit(15000)

data = []
cols = 71
rows = 71
nr_bytes = 1024

# 0 = EAST    >
# 1 = SOUTH   v
# 2 = WEST    <
# 3 = NORTH   ^

map = []

def new_pos(r,c,dr):
    new_r = r
    new_c = c
    if dr == 0:  # EAST
        new_c = new_c + 1
    elif dr == 1: # SOUTH
        new_r = new_r + 1
    elif dr == 2: # WEST
        new_c = new_c - 1
    else: # NORTH
        new_r = new_r - 1 
    return new_r, new_c

def ch(r,c):
    if ((r >= 0) and (r < rows) and (c >= 0) and (c < cols)):
        return data[r][c]
    else:
        return "#"

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def init_map():
    global map
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append(-1)
        map.append(row)

def init_data():
    global data
    data = []
    for r in range(0,rows):
        row = "." * cols
        data.append(row)

def read_data(fname, cnt):
    global data
    init_data()
    n = 0
    f = open(fname,"r")
    for line in f:
        if n == cnt:
            break
        line = line.strip()
        words = line.split(',')
        c = int(words[0])
        r = int(words[1])
        set_ch(r,c,'#')
        n = n + 1
    f.close()

# returns True if not yet visited or lower count
def update_counts(r,c,dr,prev_cnt):
    global map
    better = False
    #print("r = " + str(r) + ", c = " + str(c) + ", dr = " + str(dr) + ", prev_cnt = " + str(prev_cnt))
    old_cnt = map[r][c]
    for d in range(0,4):
        new_cnt = prev_cnt + 1
        if old_cnt == -1:       # not yet visited, always better
            better = True
        elif new_cnt < old_cnt: # better path found
            better = True
        else:                   # not better, keep old path
            new_cnt = old_cnt
    map[r][c] = new_cnt
    return better


score = 0  # minimum steps needed

# returns True when end reached
def do_step(r,c,dr):
    global score
    prev_cnt = map[r][c]  # points accumulated sofar
    new_r, new_c = new_pos(r,c,dr)
    val = ch(new_r,new_c)
    if (new_r == rows-1) and (new_c == cols-1):  # lower right (end) reached
        total = map[r][c] + 1
        if score == 0:
            score = total
        elif total < score:
            score = total
        #print("End point reached! total = " + str(total))
    elif val != "#":  # no fence, so either '.' or 'O'
        if update_counts(new_r, new_c, dr, prev_cnt):
            for d in range(0,4):
                do_step(new_r, new_c, d)

def day18(fname):
    read_data(fname,nr_bytes)
    for row in data:
        print(row)
    init_map()
    map[0][0] = 0
    for dr in range(0,4):
        do_step(0,0,dr)
#    for row in map:
#        print(row)
    print("score = " + str(score))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day18(fname)
    else:
        print("Usage: python day18 input.txt")

