import sys

#sys.setrecursionlimit(1500)

data = []
rows = 0
cols = 0

# current row
# current col
rc = 0
cc = 0

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "_"  # outside

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

# dir
# 0 = up
# 1 = right
# 2 = down
# 3 = left
def new_pos(r,c,d):
    r1 = r
    c1 = c
    if d == 0:
        r1 = r1 - 1
    elif d == 1:
        c1 = c1 + 1
    elif d == 2:
        r1 = r1 + 1
    else:
        c1 = c1 - 1
    return (r1,c1)

map = []

def make_map():
    global map
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            s = [False] * 4
            for d in range(0,4):
                r1,c1 = new_pos(r,c,d)
                ch0 = ch(r,c)
                ch1 = ch(r1,c1)
                s[d] = ((ord(ch1) - ord(ch0)) == 1)
            row.append(s)
        map.append(row)

sum = 0

def count_map(r,c):
    nr = 0
    for d in range(0,4):
        if map[r][c][d]:
            nr = nr + 1
    return nr

seen = {}

# ch0 = current char at r,c.
# ch1 = next char to be found ("1" .. "9")
def zoek(r,c,ch0):
    #nr = count_map(r,c)
    #print("zoek: r = "+str(r) + ", c = " + str(c) + ", ch = " + ch0 + ", nr = " + str(nr))
    global sum, seen
    tup = (r,c)
    #if (ch0 == "9") and not tup in seen:  # part1
    if (ch0 == "9"):                       # part2
        sum = sum + 1
        seen[tup] = True
        return
    if map[r][c] == (False, False, False, False): # no valid next
        return
    ch1 = chr(ord(ch0)+1)  # next
    for d in range(0,4):
        if map[r][c][d]:
            r1,c1 = new_pos(r,c,d)
            zoek(r1,c1,ch1)

# find all start of the series ("0")
def zoek_all():
    global seen
    for r in range(0,rows):
        for c in range(0,cols):
            ch0 = ch(r,c)
            seen = {}
            if ch0 == "0":
                #print("sum = " + str(sum))
                #print("found zero at r = " + str(r) + ", col = " + str(c))
                zoek(r,c,ch0)

    
def day10(fname):
    read_data(fname)
    #for row in data:
    #    print(row)
    make_map()
    #print(map)
    zoek_all()
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])

