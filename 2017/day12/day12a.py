import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        conn = []
        for i in range(2,len(w)):
            conn.append(w[i].replace(",",""))
        data[w[0]] = conn
    f.close()
    return data
    
def collect(data, nr, visited):
    visited.add(nr)
    v = set(data[nr])
    for i in data[nr]:
        if not i in visited:
            v = v.union(collect(data,i,visited))
    return v
    
def process(data):
    v = collect(data,"0",set())
    print(len(v))

def day12(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])

