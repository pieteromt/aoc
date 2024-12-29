import sys

sys.setrecursionlimit(15000)

codes = []
cache = {}

# numeric keypad
# 
#  +---+---+---+
#  | 7 | 8 | 9 |
#  +---+---+---+
#  | 4 | 5 | 6 |
#  +---+---+---+
#  | 1 | 2 | 3 |
#  +---+---+---+
#      | 0 | A |
#      +---+---+

# if True, we need to mind the gap
def mind_numeric_gap(r0, c0, r1, c1):
    if c0 == 0 and r1 == 3:
        return True
    if r0 == 3 and c1 == 0:
        return True
    return False

def get_numeric_pos(val):
    if val == "7":
        return 0,0
    elif val == "8":
        return 0,1
    elif val == "9":
        return 0,2
    elif val == "4":
        return 1,0
    elif val == "5":
        return 1,1
    elif val == "6":
        return 1,2
    elif val == "1":
        return 2,0
    elif val == "2":
        return 2,1
    elif val == "3":
        return 2,2
    elif val == "0":
        return 3,1
    elif val == "A":
        return 3,2
    else:
        print("get_numeric_pos error: " + val)
        exit()

def get_horz_moves(dc):
    moves = ""
    if dc<0:
        ch = "<"
    else:
        ch = ">"
    dc = abs(dc)
    for i in range(0,dc):
        moves = moves + ch
    return moves

def get_vert_moves(dr):
    moves = ""
    if dr<0:
        ch = "^"
    else:
        ch = "v"
    dr = abs(dr)
    for i in range(0,dr):
        moves = moves + ch
    return moves

# 0  2  9    A
# <A ^A >^^A vvvA 
# <A ^A ^>^A vvvA 
# <A ^A ^^>A vvvA
def calc_numeric_moves(r0, c0, r1, c1):
    #print("r,c = ("+str(r0)+","+str(c0)+")  -->  ("+str(r1)+","+str(c1)+")")
    moves = []
    dr = r1 - r0
    dc = c1 - c0
    vert_moves = get_vert_moves(dr)
    horz_moves = get_horz_moves(dc)
    if dr == 0:
        moves.append(horz_moves + "A")
    elif dc == 0:
        moves.append(vert_moves + "A")
    else:
        mind_gap = mind_numeric_gap(r0, c0, r1, c1)
        if mind_gap:
            if dr < 0:  # prevent gap
                moves.append(vert_moves + horz_moves + "A")
            else:
                moves.append(horz_moves + vert_moves + "A")
        else:
            moves.append(vert_moves + horz_moves + "A")
            moves.append(horz_moves + vert_moves + "A")
    return moves

# returns the sequence to get the numeric code

# cursor keypad
#      +---+---+
#      | ^ | A |
#  +---+---+---+
#  | < | v | > |
#  +---+---+---+

# if True, we need to mind the gap
def mind_cursor_gap(r0, c0, r1, c1):
    if c0 == 0 and r1 == 0:
        return True
    if r0 == 0 and c1 == 0:
        return True
    return False

def get_cursor_pos(val):
    if val == "^":
        return 0,1
    elif val == "A":
        return 0,2
    elif val == "<":
        return 1,0
    elif val == "v":
        return 1,1
    elif val == ">":
        return 1,2
    else:
        print("get_cursor_pos error: " + val)
        exit()

def calc_cursor_moves(r0, c0, r1, c1):
    #print("r,c = ("+str(r0)+","+str(c0)+")  -->  ("+str(r1)+","+str(c1)+")")
    moves = []
    dr = r1 - r0
    dc = c1 - c0
    vert_moves = get_vert_moves(dr)
    horz_moves = get_horz_moves(dc)
    if dr == 0:
        moves.append(horz_moves + "A")
    elif dc == 0:
        moves.append(vert_moves + "A")
    else:
        mind_gap = mind_cursor_gap(r0, c0, r1, c1)
        if mind_gap:
            if dr < 0:  # prevent gap
                moves.append(horz_moves + vert_moves + "A")
            else:
                moves.append(vert_moves + horz_moves + "A")
        else:
            moves.append(vert_moves + horz_moves + "A")
            moves.append(horz_moves + vert_moves + "A")
    return moves

def read_data(fname):
    global codes
    codes = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            codes.append(line)
    f.close()


def find_minimum(code, numeric, level):
    if level == 0:
        return len(code)

    key = code + "L" + str(level)
    if key in cache:
        return cache[key]

    if numeric: # first robot
        minimum = 0
        r0, c0 = get_numeric_pos("A")  # start position
        for num in code:
            r1, c1 = get_numeric_pos(num)
            moves = calc_numeric_moves(r0, c0, r1, c1)
            r0 = r1
            c0 = c1
            min_len = 0
            for move in moves:
                min_total = find_minimum(move, False, level-1)
                if min_len == 0:
                    min_len = min_total
                elif min_total < min_len:
                    min_len = min_total
            minimum = minimum + min_len
    else:
        minimum = 0
        r0, c0 = get_cursor_pos("A")  # start position
        for num in code:
            r1, c1 = get_cursor_pos(num)
            moves = calc_cursor_moves(r0, c0, r1, c1)
            r0 = r1
            c0 = c1
            min_len = 0
            for move in moves:
                min_total = find_minimum(move, False, level-1)
                if min_len == 0:
                    min_len = min_total
                elif min_total < min_len:
                    min_len = min_total
            minimum = minimum + min_len

    cache[key] = minimum
    return minimum

def day21(fname):
    read_data(fname)
    sum = 0
    for code in codes:
        min_len = find_minimum(code, True, 1+25)
        print(code + "  len = " + str(min_len))                
        val = int(code[:-1])*min_len
        sum = sum + val
    print("sum = " + str(sum))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day21(fname)
    else:
        print("Usage: python day21 input.txt")

