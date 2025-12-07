import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def process(data):
    pos = 50
    nr = 0
    for d in data:
        dir = d[0]
        val = int(d[1:])
        if dir == 'L':
            val = -val
        pos = pos + val
        pos = (pos + 10000)%100
        #print(dir + " " + str(val) + " " + str(pos))
        if pos == 0:
            nr += 1
    print(nr)

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])
