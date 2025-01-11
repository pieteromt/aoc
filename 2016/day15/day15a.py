import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        nr_pos = int(w[3])
        pos = int(w[11].replace(".",""))
        data.append((nr_pos,pos))
    f.close()
    return data
    
# returns True if all line up
def check(data, t):
    for d in range(1,len(data)+1):
        nr_pos, pos = data[d-1]
        td = t + d
        if (nr_pos + pos + td)%nr_pos != 0:
            return False
    return True

def process(data):
    t = 0
    while not check(data, t):
        t += 1
    print("t = " + str(t))

def day15(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])

