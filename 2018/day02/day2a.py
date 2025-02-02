import sys
import string

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def count_nr(s, nr):
    cnt = 0
    for c in string.ascii_lowercase:
        if s.count(c) == nr:
            cnt += 1
    return cnt

def process(data):
    nr2 = 0
    nr3 = 0
    for d in data:
        if count_nr(d,2) > 0:
            nr2 += 1
        if count_nr(d,3) > 0:
            nr3 += 1
    checksum = nr2*nr3
    print("Checksum: " + str(checksum))

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])

