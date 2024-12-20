import sys

sys.setrecursionlimit(15000)

data = []
cols = 0
rows = 0
re = 0  # end position
ce = 0

# 0 = EAST    >
# 1 = SOUTH   v
# 2 = WEST    <
# 3 = NORTH   ^

map = []

score = 0  # minimum steps needed

# real puzzle: 9504 steps
hist_size = 10000
hist = [0] * hist_size

cheats = {}

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

def find_pos(val):
    for r in range(0,rows):
        for c in range(0,cols):
            if ch(r,c) == val:
                return r,c
    print("error: " + val)
    exit()

def chm(r,c):
    if ((r >= 0) and (r < rows) and (c >= 0) and (c < cols)):
        return data[r][c]
    else:
        return -1

def init_map():
    global map
    map = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append(-1)
        map.append(row)

def read_data(fname):
    global data, rows, cols
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            if cols == 0:
                cols = len(line)
            data.append(line)
    f.close()
    rows = len(data)


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

# returns True when end reached
def do_step(r,c,dr):
    global score
    prev_cnt = map[r][c]  # points accumulated sofar
    new_r, new_c = new_pos(r,c,dr)
    val = ch(new_r,new_c)
    if (new_r == re) and (new_c == ce):  # end reached
        total = map[r][c] + 1
        map[new_r][new_c] = total
        if score == 0:
            score = total
        elif total < score:
            score = total
        #print("End point reached! total = " + str(total))
    elif val != "#":  # no fence, so either '.' or 'O'
        if update_counts(new_r, new_c, dr, prev_cnt):
            for d in range(0,4):
                do_step(new_r, new_c, d)

def solve():
    global score
    score = 0
    init_map()
    map[rs][cs] = 0
    for dr in range(0,4):
        do_step(rs,cs,dr)
    #for row in map:
    #    print(row)
    #print("score = " + str(score))
    return score

def find_next(r,c):
    val = map[r][c]
    for dr in range(0,4):
        new_r, new_c = new_pos(r,c,dr)
        if map[new_r][new_c] == val+1:
            return new_r, new_c
    print("error: r = " + str(r) + ", c = " + str(c))
    exit()

def valid_row(r):
    return ((r >= 0) and (r < rows))

def valid(r,c):
    return ((r >= 0) and (r < rows) and (c >= 0) and (c < cols))

def calc_gain(r0,c0,rr,cc):
    org_cnt = map[r0][c0]
    new_cnt = map[rr][cc]
    steps = abs(rr-r0) + abs(cc-c0)
    gain = new_cnt - (org_cnt+steps)
    if gain > 0:
        return gain
    else:
        return 0

def calc_cheat(r0,c0,psec):
    rmin = r0 - psec
    rmax = r0 + psec
    cmin = c0 - psec
    cmax = c0 + psec
    for rr in range(rmin,rmax+1):
        if not valid_row(rr):
            continue
        for cc in range(cmin,cmax+1):
            if not valid(rr,cc):
                continue
            steps = abs(rr-r0) + abs(cc-c0)
            if steps <= psec:
                gain = calc_gain(r0,c0,rr,cc)
                if gain > 0:
                    #print("cheat: r = " + str(r0) + ", c = " + str(r0) + ", r = " + str(rr) + ", c = " + str(cc) + ", gain = " + str(gain))
                    if not (r0,c0,rr,cc) in cheats:
                        cheats[(r0,c0,rr,cc)] = gain


def calc_hist():
    for cheat in cheats:
        gain = cheats[cheat]
        hist[gain] = hist[gain] + 1

def walk_map(r,c,psec):
    #print("r = " + str(r) + ", c = " + str(c) + ", val = " + str(map[r][c]))
    #set_ch(r,c,"O")
    if (r == re) and (c == ce):
        print("end reached, val = " + str(map[r][c]))
    else:
        #print("calc_cheat: r = " + str(r) + ", c = " + str(c))
        calc_cheat(r,c,psec)
        r,c = find_next(r,c)
        walk_map(r,c,psec)

def day20(fname):
    global rs,cs,re,ce
    read_data(fname)
    #for row in data:
    #    print(row)
    rs,cs = find_pos('S')
    re,ce = find_pos('E')
    print("start: r = " + str(rs) + ", c = " + str(cs))
    print("end:   r = " + str(re) + ", c = " + str(ce))
    steps = solve()
    #for row in map:
    #    print(row)
    walk_map(rs,cs,20)
    #for row in data:
    #    print(row)
    calc_hist()
    sum = 0
    for i in range(0,hist_size):
        val = hist[i]
        #if val != 0:
        #    print(str(i) + " : " + str(val))
        if i >= 100:
            sum = sum + val
    print("sum = " + str(sum))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day20(fname)
    else:
        print("Usage: python day20 input.txt")

