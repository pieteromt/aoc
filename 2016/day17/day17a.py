import sys

import hashlib

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        #w = line.split()
        data.append(line)
    f.close()
    return data
    
# returns the MD5 hash (as a hexadecimal string)
def calc_hash(inp):
    result = hashlib.md5(inp.encode())
    return result.hexdigest()

# returns the position in the grid
def get_pos(path):
    r,c = 0,0
    for ch in path:
        if ch == 'U':
            r -= 1
        elif ch == 'D':
            r += 1
        elif ch == 'L':
            c -= 1
        else: # if c == 'R':
            c += 1
    return (r,c)

# returns True if vault reached
def vault(path):
    return get_pos(path) == (3,3)

dirs = "UDLR"
drs = [-1,1,0,0]
dcs = [0,0,-1,1]

def valid(r,c):
    return (r >= 0) and (r < 4) and (c >= 0) and (c < 4)

def find_path(code, path):
    if vault(path):
        #print("Vault reached! path = " + path)
        return len(path), path

    h = calc_hash(code+path)[:4]

    r,c = get_pos(path)

    min_len = 9999
    min_path = ""
    for i in range(4):
        if h[i] in "bcdef":
            dp = dirs[i]
            dr = drs[i]
            dc = dcs[i]
            r1 = r + dr
            c1 = c + dc
            if valid(r1,c1):
                length, new_path = find_path(code, path + dp)
                if length < min_len:
                    min_len = length
                    min_path = new_path
    return min_len, min_path
   
def process(data):
    for d in data:
        min_len, min_path = find_path(d, "")
        print("min_path = " + min_path)
        print("min_len = " + str(min_len))

def day17(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])

