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
def calc_hash(inp):
    result = hashlib.md5(inp.encode())
    return result.hexdigest()

def calc_stretched_hash(salt,val):
    s = calc_hash(salt + str(val))
    for i in range(2016):
        s = calc_hash(s)
    return s

def calc_stretched_hash0(salt,val):
    result = hashlib.pbkdf2_hmac("md5", val, salt, 2017)
    #return result.hexdigest()
    return result

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
        s = calc_stretched_hash(salt,idx)
        if five in s:
            return idx
    return -1

def find_hash(salt):
    i   = 0
    cnt = 0
    idx = 0
    while True:
        s = calc_stretched_hash(salt,i)
        c = find_triple(s)
        if c != None:
            idx = find_five(salt,i,c)
            if idx != -1:
                cnt += 1
                print("cnt = " + str(cnt))
                if cnt == 64:
                    break
        i += 1
    return i

# warning: expect some execution time for this... :-(
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

