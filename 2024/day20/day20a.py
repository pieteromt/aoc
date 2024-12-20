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

def calc_cheat(r,c):
    cnt = map[r][c]
    for dr in range(0,4):
        new_r, new_c = new_pos(r,c,dr)
        val = ch(new_r, new_c)
        if val == "#":  # can cheat
            rr,cc = new_pos(new_r, new_c, dr)
            if ch(rr,cc) != "#":
                new_cnt = map[rr][cc]
                gain = new_cnt - (cnt+2)
                if gain > 0:
                    #print("cheat: r = " + str(new_r) + ", c = " + str(new_c) + ", gain = " + str(gain))
                    hist[gain] = hist[gain] + 1


def walk_map(r,c):
    #print("r = " + str(r) + ", c = " + str(c) + ", val = " + str(map[r][c]))
    #set_ch(r,c,"O")
    if (r == re) and (c == ce):
        print("end reached, val = " + str(map[r][c]))
    else:
        calc_cheat(r,c)
        r,c = find_next(r,c)
        walk_map(r,c)

def cheat(steps):
    print("Now with cheating...")
    #for step in range(0,steps):
    #    solve()

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
    walk_map(rs,cs)
    #for row in data:
    #    print(row)
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

