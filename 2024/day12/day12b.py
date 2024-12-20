import sys

data = []
datax = []
datay = []
rows = 0
cols = 0

def read_data(fname):
    global data, rows, cols
    data = []
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            if cols == 0:
                cols = len(line)
            data.append(line)
        else:
            break
    rows = len(data)

def init_datax():
    global datax
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append(False)
        datax.append(row)

def ch(r,c):
    if ((r >= 0) and (r < rows) and (c >= 0) and (c < cols)):
        return data[r][c]
    else:
        return "_"

def chx(r,c):
    if ((r >= 0) and (r < rows) and (c >= 0) and (c < cols)):
        return datax[r][c]
    else:
        return True

def set_chx(r,c,val):
    global datax
    row = datax[r]
    new_row = row[:c]
    new_row.append(val)
    for i in range(c+1,cols):
        new_row.append(row[i])
    datax[r] = new_row

def set_chy(r,c,val):
    global datay
    row = datay[r]
    new_row = row[:c]
    new_row.append(val)
    for i in range(c+1,cols):
        new_row.append(row[i])
    datay[r] = new_row

def chy(r,c):
    if ((r >= 0) and (r < rows) and (c >= 0) and (c < cols)):
        return datay[r][c]
    else:
        return [0,0,0,0]

def new_pos(r,c,dr):
    if dr == 0:
        r1 = r - 1
        c1 = c
    elif dr == 1:
        r1 = r
        c1 = c + 1
    elif dr == 2:
        r1 = r + 1
        c1 = c
    else:
        r1 = r
        c1 = c - 1
    return r1,c1

def calc_fence(r,c):
    val = ch(r,c)
    fence = [0,0,0,0]
    for dr in range(0,4):
        r1,c1 = new_pos(r,c,dr)
        if ch(r1,c1) != val:
            fence[dr] = 1
    return fence

def init_datay():
    global datay
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append(calc_fence(r,c))
        datay.append(row)

def calc_same(r,c,r1,c1):
    d0 = chy(r,c)
    d1 = chy(r1,c1)
    same = 0
    for i in range(0,4):
        if (d0[i] == 1) and (d1[i] == 1):
            same = same + 1
    return same

def calc_same_pos(r,c):
    val = ch(r,c)
    same = 0
    for dr in range(0,4):
        r1,c1 = new_pos(r,c,dr)
        if ch(r1,c1) == val:
            same = same + calc_same(r,c,r1,c1)
    return same

def visit(r,c):
    if chx(r,c): # already visited
        return 0,0,0

    val = ch(r,c)
    set_chx(r,c,True)
    cnt = 0
    peri = 0
    nr = 0
    same = 0

    for dr in range(0,4):
        r1,c1 = new_pos(r,c,dr)
        if ch(r1,c1) == val:
            if not chx(r1,c1):  # not yet visited
                cnt1, peri1, same1 = visit(r1,c1)
                cnt = cnt + cnt1
                peri = peri + peri1
                same = same + same1
        else:
            nr = nr+1 # fence
    
    same = same + calc_same_pos(r,c)
    cnt = cnt + 1
    peri = peri + nr
    return cnt, peri, same

def process():
    sum = 0
    for r in range(0,rows):
        for c in range(0,cols):
            cnt, peri, same = visit(r,c)
            new_peri = peri - (same//2)
            sum = sum + cnt*new_peri
    print("sum = " + str(sum))

def day12(fname):
    read_data(fname)
    init_datax()
    init_datay()
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day12 input.txt")
    else:
        day12(sys.argv[1])

