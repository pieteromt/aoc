import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        items = []
        line = line.rstrip()
        for c in line:
            items.append(c)
        data.append(items)
    f.close()
    return data
    
def pad(data):
    max = 0
    for d in data:
        if len(d) > max:
            max = len(d)
    dd = []
    for d in data:
        while len(d) < max:
            d.append(' ')
        dd.append(d)
    return dd

def process(data):
    nr = len(data)
    nc = len(data[0])
    done = False
    c = 0
    sum = 0
    while not done:
        op = data[nr-1][c]
        if op == '+':
            oper = op
            s = 0
        elif op == '*':
            oper = op
            s = 1
        else:
            pass
        st = ""
        for r in range(nr-1):
            st = st + data[r][c]
        st = st.strip()
        if len(st) == 0:
            val = 0
        else:
            val = int(st)
        if val != 0:
            if oper == '+':
                s = s + val
            else:
                s = s * val
        else:
            sum += s
        c += 1
        if c == nc:
            sum += s
            break
    print(sum)

def day6(fname):
    data = read_data(fname)
    data = pad(data)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])
