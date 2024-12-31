import sys

def read_data(fname):
    rows = 0
    cols = 0
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if cols == 0:
            cols = len(line)
        data.append(line)
    f.close()
    rows = len(data)
    return rows,cols,data

def ch(rows,cols,data,r,c):
    if (r >= 0) and (r < rows) and (c >= 0) and (c < cols):
        return data[r][c]
    else:
        return "."

def calc_light(rows,cols,data,r,c):
    nr = 0
    for dr in range(-1,2):
        for dc in range(-1,2):
            if (dr == 0) and (dc == 0):
                continue
            if ch(rows,cols,data,r+dr,c+dc) == '#':
                nr += 1
    if ch(rows,cols,data,r,c) == '#':
        if nr == 2 or nr == 3:
            return '#'
        else:
            return '.' 
    else:
        if nr == 3:
            return '#'
        else:
            return '.' 

def do_step(rows,cols,data):
    new_data = []
    for r in range(rows):
        row = ""
        for c in range(cols):
            row += calc_light(rows,cols,data,r,c)
        new_data.append(row)
    return new_data

def show(rows,cols,data):
    for i in range(rows):
        print(data[i])
    print("")

def count(rows,cols,data):
    nr = 0
    for r in range(rows):
        for c in range(cols):
            if ch(rows,cols,data,r,c) == '#':
                nr += 1
    return nr

def process(rows,cols,data,nr):
    #show(rows,cols,data)
    for i in range(nr):
        data = do_step(rows,cols,data)
        #show(rows,cols,data)
    print("Lights on: " + str(count(rows,cols,data)))

def day18(fname):
    rows,cols,data = read_data(fname)
    process(rows,cols,data,100)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18 input.txt") 
    else:
    	day18(sys.argv[1])

