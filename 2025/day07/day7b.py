import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
h = dict()
nr = 0
nc = 0

def get_data(data,r,c):
    if (c < 0) or (c >= nc):
        return '.'
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

def do_row(data,r,c):
    global h, nr, nc
    if r == nr:  # done
        return
    if (c < 0) or (c >= nc):
        return
    ch = get_data(data,r,c)
    if ch == '^':
        do_row(data,r,c-1)
        do_row(data,r,c+1)
    elif ch == '.':
        set_data(data,r,c,'|')
        do_row(data,r+1,c)
    elif ch == '|':
        pass
    else:
        pass

def print_hash(data,h):
    global nr, nc
    for r in range(nr):
        for c in range(nc):
            if (r,c) in h:
                txt = f"{h[(r,c)]:3d}"
                print(txt, end="")
            else:
                if get_data(data,r,c) == '^':
                    print("  ^", end="")
                else:
                    print("  0", end="")
            print(" ", end="")
        print("")

def get_h(r,c):
    global h
    if (r,c) in h:
        return h[(r,c)]
    else:
        return 0

def calc(data):
    global nr, nc, h
    for r in range(nr):
        for c in range(nc):
            ch = get_data(data,r,c)
            if (ch == '|'):
                val = get_h(r-1,c)
                ch0 = get_data(data,r,c-1)
                if ch0 == '^':
                    val += get_h(r-1,c-1)
                ch1 = get_data(data,r,c+1)
                if ch1 == '^':
                    val += get_h(r-1,c+1)
                h[(r,c)] = val
    #print_hash(data,h)            
    sum = 0
    for c in range(nc):
        sum += get_h(nr-1,c)
    print(sum)

def process(data):
    global h, nr, nc
    nr = len(data)
    nc = len(data[0])
    c = find_start(data)
    h[(0,c)] = 1
    do_row(data,1,c)
    calc(data)

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])
