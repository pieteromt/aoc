import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def process(data):
    ip = 0
    steps = 0
    while (ip >= 0) and (ip < len(data)):
        jmp = data[ip]
        if jmp >= 3:
            data[ip] -= 1
        else:
            data[ip] += 1
        ip += jmp
        steps += 1
    print("steps: " + str(steps))

def day5(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])

