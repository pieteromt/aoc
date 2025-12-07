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

def find_start(data):
    nc = len(data[0])
    for c in range(nc):
        if get_data(data,0,c) == 'S':
            return c
    print('S not found?')
    exit(1)

def print_data(data):
    for d in data:
        print(d)

split = 0

def do_row(data,r,c):
    global split
    nr = len(data)
    nc = len(data[0])
    if r == nr:  # done
        return
    if (c < 0) or (c >= nc):
        return
    ch = get_data(data,r,c)
    if ch == '^':
        split += 1
        do_row(data,r,c-1)
        do_row(data,r,c+1)
    elif ch == '.':
        set_data(data,r,c,'|')
        do_row(data,r+1,c)
    elif ch == '|':
        pass
    else:
        pass

def process(data):
    c = find_start(data)
    do_row(data,1,c)
    print(split)

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])
