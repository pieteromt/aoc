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
    nr = 0
    pos = 50
    for d in data:
        dir=d[0]
        val=int(d[1:])
        if dir == 'L':
            val = -val
        oldpos=pos
        pos += val
        if pos >= 100:
            while pos >= 100:
                pos -= 100
                nr += 1
            if pos == 0:
                nr -= 1
        if pos < 0:
            if oldpos == 0:
                nr -= 1
            while pos < 0:
                pos += 100
                nr += 1
        if pos == 0:
            nr += 1
        #print(dir + " " + str(val) + "        " + str(oldpos) + " " + str(pos)  + " " + str(nr))
    print(nr)

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])
