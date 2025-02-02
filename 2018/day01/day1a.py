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
    #for d in data:
    #    print(d)
    print("sum = " + str(sum(data)))

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

