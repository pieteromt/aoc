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
    
def get_section_length(s):
    b0 = s.find('(')
    if b0 != -1:
        b1 = s.find(')')
        x = s[b0+1:b1].split('x')
        n_char = int(x[0])
        repeat = int(x[1])
        return repeat * get_length(s[b1+1:])

def get_length(s):
    r = 0
    b0 = s.find('(')
    if b0 != -1:
        b1 = s.find(')')
        x = s[b0+1:b1].split('x')
        n_char = int(x[0])
        repeat = int(x[1])
        if b0 != 0:
            r += len(s[:b0])
        r += get_section_length(s[b0:b1+1+n_char])
        return r + get_length(s[b1+1+n_char:])
    else: # no decompression needed
        return len(s)

def process(data):
    for d in data:
        print("Decompressed length = " + str(get_length(d)))

def day9(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])

