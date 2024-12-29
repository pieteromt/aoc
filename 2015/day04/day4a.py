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

def process(data):
    for key in data:
        val = 0
        while True:
            if calc_hash(key,val).startswith("00000"):
                break
            val += 1
        print(key + " : " + str(val))    
        
def test():
    print(calc_hash("abcdef", 609043))
    print(calc_hash("pqrstuv", 1048970))

def day4(fname):
    data = read_data(fname)
    #test()
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])

