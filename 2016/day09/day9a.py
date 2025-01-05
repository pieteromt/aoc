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
    
def decompress(s):
    d_s = ""
    while len(s) > 0:
        b0 = s.find('(')
        if b0 != -1:
            b1 = s.find(')')
            d_s += s[:b0]
            x = s[b0+1:b1].split('x')
            n_char = int(x[0])
            repeat = int(x[1])
            chars = s[b1+1:b1+1+n_char]
            d_s += chars * repeat
            s = s[b1+1+n_char:]
        else:
            d_s += s
            s = ""
    return d_s

def process(data):
    sum = 0
    for d in data:
        d_s = decompress(d)
        sum += len(d_s)
        #print(d + " -> " + d_s)
    print("Sum = " + str(sum))

def day9(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])

