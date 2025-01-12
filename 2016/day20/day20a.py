import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split('-')
        start = int(w[0])
        end = int(w[1])
        size = end - start + 1
        data[start] = (start,size,end)
    f.close()
    return data
    
def process(data):
    blocked = -1  # blocked+1 is the first free IP
    for d in sorted(data.keys()):
        start, size, end = data[d]
        if start <= blocked+1:
            if end > blocked:
                blocked = end
        else:
            break
    print("Found: " + str(blocked+1))

def day20(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])

