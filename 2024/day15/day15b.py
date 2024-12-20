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


# r,c = "[",  r,c+1 = "]"
def move_box(r,c,dr,dc):
    #print("move box: r = " + str(r) + ", c = " + str(c) + ", dr = " + str(dr) + ", dc = " + str(dc))
    if dr == 0:
        if dc == -1: # move box to left
            set_ch(r, c-1, "[")
            set_ch(r, c,   "]")
            set_ch(r, c+1, ".")
        else:        # move box to right
            set_ch(r, c,   ".")
            set_ch(r, c+1, "[")
            set_ch(r, c+2, "]")
    else:
        set_ch(r,    c,   ".")
        set_ch(r,    c+1, ".")
        set_ch(r+dr, c,   "[")
        set_ch(r+dr, c+1, "]")
        
    #show()

# r,c = "[",  r,c+1 = "]"
def try_move(r,c,dr,dc,doit):
    # horizontal
    if dr == 0:
        new_r = r
        if dc == -1:  # left
            new_c = c - 1
        else:  # right
            new_c = c + 2
        val = ch(new_r, new_c)
        if val == ".":
            if doit:
                move_box(r,c,dr,dc)
            return True
        elif val == "#":
            return False
        else:  # another box
            if val == "]":   # normalize
                new_c = new_c - 1
            can_move = try_move(new_r, new_c, dr, dc, doit)
            if can_move and doit:
                move_box(r,c,dr,dc)
            return can_move
    else: # vertical
        new_r = r + dr
        new_c = c
        val0 = ch(new_r, new_c)
        val1 = ch(new_r, new_c+1)
        if (val0 == ".") and (val1 == "."):
            if doit:
                move_box(r,c,dr,dc)
            return True
        elif (val0 == "#") or (val1 == "#"):
            return False
        elif (val0 == "]") and (val1 == "."):
            can_move = try_move(new_r, new_c-1, dr, dc, doit)
            if can_move and doit:
                move_box(r,c,dr,dc)
            return can_move
        elif (val0 == "[") and (val1 == "]"):
            can_move = try_move(new_r, new_c, dr, dc, doit)
            if can_move and doit:
                move_box(r,c,dr,dc)
            return can_move
        elif (val0 == ".") and (val1 == "["):
            can_move = try_move(new_r, new_c+1, dr, dc, doit)
            if can_move and doit:
                move_box(r,c,dr,dc)
            return can_move
        elif (val0 == "]") and (val1 == "["):
            can_move1 = try_move(new_r, new_c-1, dr, dc, doit)
            can_move2 = try_move(new_r, new_c+1, dr, dc, doit)
            can_move = can_move1 and can_move2
            if can_move and doit:
                move_box(r,c,dr,dc)
            return can_move
        else:
            print("error: val0 = " + val0 + ", val1 = " + val1)
            exit()


# left, right, up, down
# dr,dc =  0,-1   val = "]"
# dr,dc =  0, 1   val = "["
# dr,dc = -1, 0   val = "[" or "]"
# dr,dc =  1, 0   val = "[" or "]"
def do_box(val, r, c, dr, dc):
    # normalize box coords (r,c is "[")
    if val == "]":
        c = c - 1
    can_move = try_move(r,c,dr,dc,False)
    if can_move:
        #print("moving box(es)...")
        try_move(r,c,dr,dc,True)
        #print("done moving box(es).")
    return can_move


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
        #print("could move robot")
    elif val == "#":  # wall
        #print("could not move robot")
        pass # do nothing
    else: # box "[" or "]"
        if do_box(val,new_r,new_c,dr,dc):  # did move
            #print("could move robot")
            set_ch(rr, cr, ".")
            set_ch(new_r, new_c, "@")
            rr = new_r
            cr = new_c
        else:
            #print("could not move robot / box")
            pass
    #show()

def count():
    sum = 0
    for r in range(0,rows):
        for c in range(0,cols):
            if ch(r,c) == "[":
                sum = sum + 100*r + c
    print("sum = " + str(sum))

def expand():
    global data, cols
    for r in range(0,rows):
        row = data[r]
        new_row = ""
        for c in range(0,cols):
            val = row[c]
            if val == "#":
                new_row = new_row + "##"
            elif val == "O":
                new_row = new_row + "[]"
            elif val == ".":
                new_row = new_row + ".."
            elif val == "@":
                new_row = new_row + "@."
        data[r] = new_row
    cols = 2*cols            

def process():
    #show()
    expand()
    find_robot()
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
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])

