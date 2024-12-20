import sys

data = []
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


def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "_"  # outside

def read_data(fname):
    global rows, cols
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

def walk():
    global rc, cc, dr, data
    sum = 1
    while True:
        new_r, new_c = new_pos()
        x = ch(new_r, new_c)
        if x == '_':  # we're done
            break
        elif x == '#':  # obstruction, turn
            dr = (dr + 1)%4
        else:  # new pos
            rc = new_r
            cc = new_c
            if x == '.':
                sum = sum + 1
                row = data[rc]
                #print(row)
                new_row = row[:cc] + 'X' + row[cc+1:]
                data[rc] = new_row
                #print(new_row)
            else:
                pass
        #print("rc = " + str(rc) + ", cc = " + str(cc) + ", dr = " + str(dr) + ", sum = " + str(sum))
    print("sum = " + str(sum))

def day6(fname):
    read_data(fname)
    for row in data:
        print(row)
    find_guard()
    print("rc = " + str(rc) + ", cc = " + str(cc) + ", dr = " + str(dr))
    walk()
    for row in data:
        print(row)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])

