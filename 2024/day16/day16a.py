import sys

sys.setrecursionlimit(15000)

data = []
cols = 0
rows = 0

map = []

score = 0

# 0 = EAST    >
# 1 = SOUTH   v
# 2 = WEST    <
# 3 = NORTH   ^

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

def init_map():
    global map
    map = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append([-1,-1,-1,-1])
        map.append(row)

def read_data(fname):
    global data, cols, rows
    data = []
    cols = 0
    rows = 0
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if cols == 0:
            cols = len(line)
        data.append(line)
    f.close()
    rows = len(data)

def find_deer():
    for r in range(0,rows):
        for c in range(0,cols):
            if data[r][c] == "S":
                return r, c
    return 0,0

# deltas: 0, 1000, 2000, 1000
def get_delta(dr,d):
    delta = 0
    s = (4 + dr - d)%4
    if s == 0:  # no rotation needed
        delta = 0
    elif s == 1: # rotate once
        delta = 1000
    elif s == 2: # rotate twice
        delta = 2000
    else:        # rotate counterwise
        delta = 1000
    #print("get_delta: dr = " + str(dr) + ", d = " + str(d) + ", s = " + str(s) + ", delta = " + str(delta))
    return delta

def get_deltas(dr, add):
    deltas = []
    for d in range(0,4):
       delta = get_delta(dr,d) + add
       deltas.append(delta)
    return deltas

# returns True if not yet visited or lower count
def update_counts(r,c,dr,prev_cnt):
    global map
    better = False
    #print("r = " + str(r) + ", c = " + str(c) + ", dr = " + str(dr) + ", prev_cnt = " + str(prev_cnt))
    deltas = get_deltas(dr, 1)
    old_cnts = map[r][c]
    new_cnts = [] 
    for d in range(0,4):
        old_cnt = old_cnts[d]
        new_cnt = prev_cnt + deltas[d]
        if old_cnt == -1:       # not yet visited, always better
            better = True
        elif new_cnt < old_cnt: # better path found
            better = True
        else:                   # not better, keep old path
            new_cnt = old_cnt
        new_cnts.append(new_cnt)
    map[r][c] = new_cnts
    return better

def do_step(r,c,dr):
    global score
    prev_cnt = map[r][c][dr]  # points accumulated sofar
    new_r, new_c = new_pos(r,c,dr)
    val = data[new_r][new_c]
    if val == 'E':
        minimum = min(map[r][c]) + 1
        if score == 0:
            score = minimum
        elif minimum < score:
            score = minimum
        #print("End point reached! map = " + str(map[r][c]) + ", minimum = " + str(minimum))
    elif val != "#":  # no fence, so either '.' or 'E'
        if update_counts(new_r, new_c, dr, prev_cnt):
            for d in range(0,4):
                do_step(new_r, new_c, d)

def day16(fname):
    read_data(fname)
    for row in data:
        print(row)
    print("cols = " + str(cols) + ", rows = " + str(rows))
    init_map()
    cr, cc = find_deer()
    dr = 0  # EAST
    #print("cr = " + str(cr)+ ", cc = " + str(cc))
    map[cr][cc] = get_deltas(dr,0)
    #print(map[cr][cc])
    for dr in range(0,4):
        do_step(cr,cc,dr)
    #for row in map:
    #    print(row)
    print("score = " + str(score))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day16(fname)
    else:
        print("Usage: python day16 input.txt")
