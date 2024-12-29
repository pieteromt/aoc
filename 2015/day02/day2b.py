import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        dim = line.split("x")
        data.append(tuple(map(int,dim)))
    f.close()
    return data

def process(data):
    total = 0
    for dim in data:
        l,w,h = dim
        m1, m2 = tuple(sorted(dim)[:-1])  # two minimum values
        ribbon = 2*(m1 + m2) + l*w*h
        print(str(dim) + " : " + str(ribbon))
        total += ribbon
    print("total: " + str(total))

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])

