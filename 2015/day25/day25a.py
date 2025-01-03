import sys

def read_data(fname):
    f = open(fname,"r")
    r,c = 0,0
    for line in f:
        line = line.strip()
        w = line.split()
        for i in range(len(w)):
            if w[i] == "row":
                r = int(w[i+1][:-1])  # remove comma
            elif w[i] == "column":
                c = int(w[i+1][:-1])  # remove dot
    f.close()
    return r,c
    
def get_idx(r,c):
    c += (r-1)
    return ((c*(c+1))//2)-(r-1)

def next_code(code):
    return (code * 252533)%33554393

def get_code(idx):
    i = 1
    code = 20151125
    while i < idx:
        code = next_code(code)
        i += 1
    return code

def print_table():
    for r in range(1,7):
        for c in range(1,7):
            idx = get_idx(r,c)
            code = get_code(idx)
            print("{:10d}".format(code) + " ", end='')
        print("")

def process(data):
    print_table()
    r,c = data
    idx = get_idx(r,c)
    code = get_code(idx)
    print("code at (" + str(r) + "," + str(c) + ") = " + str(code))

def day25(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day25 input.txt") 
    else:
    	day25(sys.argv[1])

