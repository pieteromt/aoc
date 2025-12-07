import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        words = line.split()
        items = []
        for w in words:
            if (w != '*') and (w != '+'):
                items.append(int(w))
            else:
                items.append(w)
        data.append(items)
    f.close()
    return data
    
def process(data):
    sum = 0
    nr = len(data)
    nc = len(data[0])
    for c in range(nc):
        oper = data[nr-1][c]
        if oper == '+':
            s = 0
        else:
            s = 1
        for r in range(nr-1):
            val = data[r][c]
            if oper == '+':
                s = s + val
            else:
                s = s * val
        sum += s
    print(sum)

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])
