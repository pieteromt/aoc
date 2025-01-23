import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        arr = []
        for i in range(len(w)):
            arr.append(int(w[i]))
        data.append(arr)
    f.close()
    return data
    
def process(data):
    sum = 0
    for d in data:
        m0 = min(d)
        m1 = max(d)
        sum += (m1 - m0)
    print("sum = " + str(sum))

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])

