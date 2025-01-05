import sys

import hashlib

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)      # secret key
    f.close()
    return data

# returns the MD5 hash (as a hexadecimal string)
def calc_hash(key,val):
    inp = key + str(val)
    result = hashlib.md5(inp.encode())
    return result.hexdigest()

def find_index(key,start):
    val = start
    while True:
        if calc_hash(key,val).startswith("00000"):
            break
        val += 1
    return val

def get_char(key,val):
    hash = calc_hash(key,val)
    return hash[5]

def calc_code(key):
    start = 0
    code = ""
    for i in range(8):
        val = find_index(key,start)
        code += get_char(key,val)
        start = val+1
    print("key = " + key + ", code = " + code)
        
def test():
    key = "abc"
    calc_code(key)

def process(data):
    for key in data:
        calc_code(key)

def day5(fname):
    data = read_data(fname)
    #test()
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])

