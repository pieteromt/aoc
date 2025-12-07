import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        ranges=line.split(',')
        for range in ranges:
            w=range.split('-')
            data.append((int(w[0]),int(w[1])))
    f.close()
    return data
    
def match(s,x):
    idx = len(s)//x
    if x*idx != len(s):
        return False
    s0 = s[:idx]
    for i in range(x-1):
        si = s[(i+1)*idx:(i+2)*idx]
        if si != s0:
            return False
    return True    
    
def process(data):
    sum = 0
    for d in data:
        for n in range(d[0],d[1]+1):
            s = str(n)
            for x in range(len(s)-1):
                if match(s,x+2):
                    sum += n
                    break
    print(sum)

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])
