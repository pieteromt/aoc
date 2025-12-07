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
    
def process(data):
    sum = 0
    for d in data:
        for n in range(d[0],d[1]+1):
            s = str(n)
            idx = len(s)//2
            s0 = s[:idx]
            s1 = s[idx:]
            if s0 == s1:
                sum += n
    print(sum)

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])
