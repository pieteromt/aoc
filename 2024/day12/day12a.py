import sys

data = []
datax = []
rows = 0
cols = 0

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

def init_datax():
    global datax
    datax = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            val = False    # not visited
            row.append(val)
        datax.append(row)
            
def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "_"  # outside

def chx(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return datax[row][col]
    else:
        return True # outside

# dir
# 0 = up
# 1 = right
# 2 = down
# 3 = left
def new_pos(r,c,dr):
    if dr == 0:
        new_r = r - 1
        new_c = c
    elif dr == 1:
        new_r = r
        new_c = c + 1
    elif dr == 2:
        new_r = r + 1
        new_c = c
    elif dr == 3:
        new_r = r
        new_c = c - 1
    return new_r, new_c

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def set_chx(r,c,val):
    global datax
    row = datax[r]
    new_row = row.copy()
    new_row[c] = val
    datax[r] = new_row

def visit(r,c):
    if chx(r,c):  # already visited
        return (0, 0)
    val = ch(r,c)
    set_chx(r,c,True)
    peri = 0
    cnt = 0
    nr = 0     # number of same neighbours
    for dr in range(0,4):
        r1,c1 = new_pos(r,c,dr)
        if ch(r1,c1) == val:
            nr = nr+1
            if not chx(r1,c1):
                cnt1, peri1 = visit(r1,c1)
                cnt = cnt + cnt1
                peri = peri + peri1
    cnt = cnt + 1
    peri = peri + (4 - nr)
    #print("r = " + str(r) + ", c = " + str(c) + ", cnt = " + str(cnt) + ", peri = " + str(peri))
    return (cnt, peri)

def process():
    sum = 0
    for r in range(0,rows):
        for c in range(0, cols):
            cnt, peri = visit(r,c)
            sum = sum + cnt*peri
    print("sum = " + str(sum))

def day12(fname):
    global data, data_x
    read_data(fname)
    init_datax()
    #for row in data:
    #    print(row)
    #for row in datax:
    #    print(row)
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])

