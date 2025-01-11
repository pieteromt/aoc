import sys

import hashlib
import itertools

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
# returns the MD5 hash (as a hexadecimal string)
def calc_hash(salt,val):
    inp = salt + str(val)
    result = hashlib.md5(inp.encode())
    return result.hexdigest()

# returns first char that is repeated 3 times (or None)
def find_triple(s):
    for i in range(len(s)-2):
        if (s[i] == s[i+1]) and (s[i] == s[i+2]):
            return s[i]
    return None

# returns the index of the hash with 5 times 'c'
def find_five(salt,i,c):
    five = c * 5
    for j in range(1000):
        idx = i+j+1
        s = calc_hash(salt,idx)
        if five in s:
            return idx
    return -1

def find_hash(salt):
    i   = 0
    cnt = 0
    idx = 0
    while True:
        s = calc_hash(salt,i)
        c = find_triple(s)
        if c != None:
            idx = find_five(salt,i,c)
            if idx != -1:
                cnt += 1
                if cnt == 64:
                    break
        i += 1
    return i

def process(data):
    for d in data:
        print("idx: " + str(find_hash(d)))

def day14(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day14 input.txt") 
    else:
    	day14(sys.argv[1])

