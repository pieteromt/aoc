import sys

# m is a [3,3] matrix
def triples(data, m):
    for i in range(3):
        arr = []
        for j in range(3):
            arr.append(int(m[j][i]))   # transpose
        data.append(tuple(sorted(arr))) 

def read_data(fname):
    data = []
    f = open(fname,"r")
    m = []
    for line in f:
        line = line.strip()
        w = line.split()
        if len(m) == 3:
            triples(data, m)
            m = []
        m.append(w)
    f.close()
    triples(data, m)
    return data
    
# note: the values in the tuple are sorted
def is_triangle(t):
    return t[0] + t[1] > t[2]

def process(data):
    triangles = 0
    for t in data:
        if is_triangle(t):
            triangles += 1
    print("triangles = " + str(triangles))

def day3(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

