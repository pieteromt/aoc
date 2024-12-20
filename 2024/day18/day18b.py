import sys

sys.setrecursionlimit(15000)

coor = []   # x,y coordinates of the bytes

data = []

map = []

show = False  # print coordinates when adding a byte

#cols = 7   # test data
#rows = 7
#nr_bytes = 12

cols = 71   # real data
rows = 71
nr_bytes = 1024

score = 0   # minimum number of steps to reach endpoint

# 'dr' value:
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

# guard against looking outside the data grid
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
    global map, score
    score = 0
    map = []
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

def add_byte(idx):
    c,r = coor[idx]
    if show:
        print("add_byte: ("+str(c)+","+str(r)+")")
    set_ch(r,c,'#')

def set_data(cnt):
    global data
    init_data()
    for n in range(0,cnt):
        add_byte(n)

def read_data(fname):
    global coor
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        words = line.split(',')
        c = int(words[0])
        r = int(words[1])
        coor.append((c,r))
    f.close()

# returns True if not yet visited or lower count
# with True meaning: "Yes, you need to seach further!"
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

# returns True when End point reached; we're not interested in the optimum path anymore
def do_step(r,c,dr):
    global score
    end_seen = False
    #print("do_step: r = " + str(r) + ", c = " + str(c) + ", dr = " + str(dr))
    prev_cnt = map[r][c]  # steps accumulated sofar
    new_r, new_c = new_pos(r,c,dr)
    val = ch(new_r,new_c)
    # check if lower right (endpoint) reached
    if (new_r == rows-1) and (new_c == cols-1):  
        steps = map[r][c] + 1
        if score == 0:
            score = steps
        elif steps < score:
            score = steps
        #print("End point reached! steps = " + str(steps))
        end_seen = True
    elif val != "#":  # not a fence
        if update_counts(new_r, new_c, dr, prev_cnt): # if True, search deeper
            for d in range(0,4):
                if do_step(new_r, new_c, d):
                    end_seen = True
                    break
    return end_seen

def day18(fname):
    global show
    read_data(fname)
    set_data(nr_bytes)
    #for row in data:
    #    print(row)

    show = False
    for idx in range(nr_bytes,len(coor)):
        add_byte(idx)
        init_map()
        r = 0  # start position upper left
        c = 0
        map[r][c] = 0
        for dr in range(0,4):
            do_step(r,c,dr)
        #print("score = " + str(score))
        if score == 0:
            print("Answer: " + str(coor[idx][0]) + "," + str(coor[idx][1]))
            break

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day18(fname)
    else:
        print("Usage: python day18 input.txt")

