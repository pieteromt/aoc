import sys

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

vals = {}

def add(r,c,val):
    global vals
    #print("row = " + str(r) + ", col = " + str(c) + ", val = " + str(val))
    if val not in vals:
        vals[val] = []
    vals[val].append((r,c))

def valid(a):
    return (a[0] >= 0) and (a[0] < rows) and (a[1] >= 0) and (a[1] < cols)

pairs = {}

def add_pair(a):
    global pairs
    if a not in pairs:
        pairs[a] = 1
        set_ch(a[0], a[1], '#')


def do_pair(a1,a2):
    dr = a2[0] - a1[0]
    dc = a2[1] - a1[1]
    v1 = True
    n = 1
    while v1:
        a3 = (a1[0] - n*dr, a1[1] - n*dc)
        n = n + 1
        v1 = valid(a3)
        if valid(a3):
            add_pair(a3)
    v2 = True
    n = 1
    while v2:
        a4 = (a2[0] + n*dr, a2[1] + n*dc)
        n = n + 1
        v2 = valid(a4)
        if valid(a4):
            add_pair(a4)
    #print("a1 = " + str(a1) + ", a2 = " + str(a2) + ", a3 = " + str(a3) + ", a4 = " + str(a4))

def do_arr(arr):
    #print(arr)
    nr = len(arr)
    for i in range(0,nr):
        for j in range(i+1,nr):
            do_pair(arr[i], arr[j])

def process():
    for r in range(0,rows):
        for c in range(0, cols):
            val = ch(r,c)
            if val != ".":
                add(r,c,val)
                add_pair((r,c))  # antenna counts too

    #print(vals)
    for val in vals.keys():
        arr = vals[val]
        do_arr(arr)
    sum = len(pairs)
    print("sum = " + str(sum))
    #for row in data:
    #    print(row)

def day8(fname):
    read_data(fname)
    #for row in data:
    #    print(row)
    #print("rows = " + str(rows) + ", cols = " + str(cols))
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day8 input.txt") 
    else:
    	day8(sys.argv[1])

