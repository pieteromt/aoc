import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    

def check_number(d):
    n = len(d)
    print(d + " ", end='')
    d += d[0]
    sum = 0
    for i in range(n):
        if d[i] == d[i+1]:
            sum += ord(d[i]) - ord("0")
    print(str(sum))    

def process(data):
    for d in data:
        check_number(d)

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

