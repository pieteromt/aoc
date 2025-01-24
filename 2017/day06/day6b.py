import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        for i in w:
            data.append(int(i))
    f.close()
    return data
    
def range_all(ln, idx):
    for i in range(ln):
        idx = (idx+1)%ln
        yield idx

def process(data):
    cache = {}
    t = tuple(data)
    cache[t] = 1
    #print(t)
    seen = False
    cnt = 0
    t0 = (0,0)
    while True:
        idx_max = max(range(len(data)), key=data.__getitem__)
        val = data[idx_max]
        div = val//len(data)
        mod = val%len(data)
        # all can get 'div' blocks, 'mod' can get 'div+1' blocks
        data[idx_max] = 0
        for i in range_all(len(data), idx_max):
            if mod > 0:
                data[i] += div + 1
                mod -= 1
            else:
                data[i] += div
        t = tuple(data)
        #print(t)
        cnt += 1
        if t == t0:
            break
        if not seen:
            if t in cache:
                t0 = t
                seen = True
                cnt = 0
        cache[t] = 1
    print("cnt = " + str(cnt))

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])

