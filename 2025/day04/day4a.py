import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def get_data(data,r,c):
    row = data[r]
    val = row[c]
    return val

def set_data(data,r,c,val):
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def get_count(data,r,c):
    nr = len(data)
    nc = len(data[0])
    cnt = 0
    for dy in range(3):
        for dx in range(3):
            dr = dy-1
            dc = dx-1
            rr = r + dr
            cc = c + dc
            if (rr >= 0) and (rr < nr):
                if (cc >= 0) and (cc < nc):
                    if (dr == 0) and (dc == 0):
                        continue
                    val = get_data(data,rr,cc)
                    if val == '@':
                        cnt += 1
    return cnt

def process(data):
    nr = len(data)
    nc = len(data[0])
    sum = 0
    for r in range(nr):
        for c in range(nc):
            if get_data(data,r,c) == '@':
                val = get_count(data,r,c)
                if val < 4:
                    sum += 1
    print(sum)

def day4(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])
