import sys

data = []
data_x = []
rows = 0
cols = 0

# current row
# current col
rc = 0
cc = 0
# dir
# 0 = up
# 1 = right
# 2 = down
# 3 = left
dr = 0


def read_data(fname):
    global rows, cols, data
    data = []
    rows = 0
    cols = 0
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            if cols == 0:
                cols = len(line)
            data.append(line)
            rows = rows + 1
        else:
            break
    f.close()

def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "_"  # outside

def chx(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data_x[row][col]
    else:
        return "_"  # outside

def is_up(c):
    return (c == '^')

def is_right(c):
    return (c == '>')

def is_down(c):
    return (c == 'v')

def is_left(c):
    return (c == '<')

def is_cursor(c):
    return is_up(c) or is_right(c) or is_down(c) or is_left(c)

def find_guard():
    global rc, cc, dr
    for r in range(0,rows):
        for c in range(0,cols):
            x = ch(r,c)
            if is_cursor(x):
                rc = r
                cc = c
                if is_up(x):
                    dr = 0
                elif is_right(x):
                    dr = 1
                elif is_down(x):
                    dr = 2
                elif is_left(x):
                    dr = 3
                break

def init(fname):
    read_data(fname)
    find_guard()
                
def new_pos():
    if dr == 0:
        new_r = rc - 1
        new_c = cc
    elif dr == 1:
        new_r = rc
        new_c = cc + 1
    elif dr == 2:
        new_r = rc + 1
        new_c = cc
    elif dr == 3:
        new_r = rc
        new_c = cc - 1
    return new_r, new_c

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def test_loop():
    global rc, cc, dr, data
    sum = 1
    cnt = 0
    while cnt < 30000:
        new_r, new_c = new_pos()
        x = ch(new_r, new_c)
        cnt = cnt + 1
        if x == '_':  # we're done
            break
        elif x == '#':  # obstruction, turn
            dr = (dr + 1)%4
        else:  # new pos
            rc = new_r
            cc = new_c
            if x == '.':
                sum = sum + 1
                set_ch(rc,cc,'X')
            else:
                pass
    #print("cnt = " + str(cnt))
    return cnt == 30000  # looping


def check(fname,r,c):
    init(fname)
    set_ch(r,c,'#')
    #print("check r = " + str(r) + ", c = " + str(c))
    #for row in data:
    #    print(row)
    return test_loop()


def day6(fname):
    global data, data_x
    init(fname)
    test_loop()
    data_x = data.copy()
    init(fname)
    #print("rows = " + str(rows) + ", cols = " + str(cols))
    #print("before")
    #for row in data:
    #    print(row)
    #print("after")
    #for row in data_x:
    #    print(row)
    #print("done")
    sum = 0
    for r in range(0,rows):
        for c in range(0, cols):
            if chx(r,c) == 'X':
                if check(fname,r,c):
                    print("loop for r = " + str(r) + ", c = " + str(c))
                    sum = sum + 1
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])

