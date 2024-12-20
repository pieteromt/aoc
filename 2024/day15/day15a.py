import sys

data = []
cols = 0
rows = 0

rr = 0  # robot position
cr = 0

moves = []

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def ch(r,c): 
    if (r >= 0) and (r < rows) and (c >= 0) and (c < cols):
        return data[r][c]
    else:
        return "_"  # outside

def find_robot():
    global rr, cr
    for r in range(0,rows):
        for c in range(0,cols):
            if ch(r,c) == "@":
                rr = r
                cr = c
                return

def dr_dc(m):
    dr = 0
    dc = 0
    if m == '^':
        dr = -1
    elif m == '>':
        dc = 1
    elif m == 'v':
        dr = 1
    elif m == '<':
        dc = -1
    return dr,dc

def show():
    for row in data:
        print(row)
    print(" ")

# r,c has a box
def find_free(r,c,dr,dc):
    free_r = -1
    free_c = -1
    while True:
        r = r + dr
        c = c + dc
        val = ch(r,c)
        if val == ".":  # free slot found
            free_r = r
            free_c = c
            break
        elif val == "#": # wall
            break
        else:  # box
            pass
    return free_r, free_c

def do_move(m):
    global rr, cr
    dr, dc = dr_dc(m)
    #print("m = " + m + ", dr = " + str(dr) + ", dc = " + str(dc))
    new_r = rr + dr
    new_c = cr + dc
    val = ch(new_r,new_c)
    # first check if the robot can move to a free slot
    if val == ".":
        set_ch(rr, cr, ".")
        set_ch(new_r, new_c, "@")
        rr = new_r
        cr = new_c
    elif val == "#":  # wall
        pass # do nothing
    else: # box
        free_r, free_c = find_free(new_r, new_c, dr, dc)
        if free_r != -1:  # found
            set_ch(rr, cr, ".")
            set_ch(new_r, new_c, "@")
            set_ch(free_r, free_c, "O")
            rr = new_r
            cr = new_c
    #show()

def count():
    sum = 0
    for r in range(0,rows):
        for c in range(0,cols):
            if ch(r,c) == "O":
                sum = sum + 100*r + c
    print("sum = " + str(sum))

def process():
    #show()
    for m in moves:
        do_move(m)
    show()
    count()

def read_data(fname):
    global data, cols, rows, moves
    f = open(fname,"r")
    state = 0
    data = []
    moves = []
    for line in f:
        line = line.strip()
        if len(line) == 0:
            state = 1
            rows = len(data)
        else:
            if state == 0:
                if cols == 0:
                    cols = len(line)
                data.append(line)    
            else:
                for m in line:
                    moves.append(m)
    f.close()

def day15(fname):
    read_data(fname)
    find_robot()
    #print("robot: r = " + str(rr) + ", c = " + str(cr))
    #print(moves)
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])

