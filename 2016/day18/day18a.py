import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
def get_trap(left, center, right):
    if (left == "^") and (center == "^") and (right == "."):
        return "^"
    if (left == ".") and (center == "^") and (right == "^"):
        return "^"
    if (left == "^") and (center == ".") and (right == "."):
        return "^"
    if (left == ".") and (center == ".") and (right == "^"):
        return "^"
    return "."

def generate_row(d):
    d2 = ""
    ln = len(d)
    for i in range(ln):
        if i>0:
            left = d[i-1]
        else:
            left = "."
        if i<ln-1:
            right = d[i+1]
        else:
            right = "."
        center = d[i]
        ch = get_trap(left, center, right)
        d2 += ch
    return d2

def make_map(d, nrows):
    map = []
    map.append(d)
    for i in range(nrows-1):
        d = generate_row(d)
        map.append(d)
    return map

def show_map(map):
    for row in map:
        print(row)
    print("")

def count(map):
    sum = 0
    for row in map:
        for ch in row:
            if ch == ".":
                sum += 1
    print("Safe tiles: " + str(sum))

def process(data):
    for d in data:
        map = make_map(d, 40)
        #show_map(map)
        count(map)
        map = make_map(d, 400000)
        #show_map(map)
        count(map)

def day18(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18 input.txt") 
    else:
    	day18(sys.argv[1])

