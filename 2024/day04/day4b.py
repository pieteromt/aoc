import sys

data = []
rows = 0
cols = 0

def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "."

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

def match_dir(r,c,dr,dc):
    sum = 0
    one = ch(r+dr,c+dc)
    two = ch(r-dr,c-dc)
    if ((one == "M") and (two == "S")) or ((one == "S") and (two == "M")):
        sum = 1
    return sum

def count_xmas(r,c):
    #print("r = " + str(r) + ", c = " + str(c))
    sum = 0
    if (match_dir(r,c,-1,-1)==1) and (match_dir(r,c,-1,1)==1):
        sum = 1
    return sum

def count():
    sum = 0
    for r in range(0,rows):
        for c in range(0,rows):
            if ch(r,c) == "A":
                cnt = count_xmas(r,c)
                sum = sum + cnt
    print("sum = " + str(sum))

def day4(fname):
    read_data(fname)
    print(data)
    count()
    #print("rows = " + str(rows))
    #print("cols = " + str(cols))
    #print("a[0][0] = " + ch(0,0))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])

