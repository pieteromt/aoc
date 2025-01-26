import sys

def read_data(fname):
    data = {}
    mx = 0
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        layer = int(w[0].replace(':',''))
        data[layer] = int(w[1])
        if layer > mx:
            mx = layer
    f.close()
    return data, mx
    
def process(data, mx):
    t = 0
    while True:
        t += 1
        caught = False
        for i in range(mx+1):
            if i in data:
                cycle = 2*(data[i]-1)
                if (t+i)%cycle == 0:
                    caught = True
                    break
        if not caught:
            print("t = " + str(t) + " picoseconds")
            break

def day13(fname):
    data, mx = read_data(fname)
    process(data, mx)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])

