import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append((w[0],w[2],int(w[4])))
    f.close()
    return data

def get_locs(data):
    locs = set()
    for d in data:
        locs.add(d[0])
        locs.add(d[1])
    return locs

def get_dist(data,l1,l2):
    for d in data:
        if ((d[0] == l1) and (d[1] == l2)) or ((d[0] == l2) and (d[1] == l1)):
            return d[2]
    print("error: " + l1 + " " + l2)
    exit()

def calc_dist(data,t):
    dist = 0
    for i in range(len(t)-1):
        dist += get_dist(data,t[i],t[i+1])
    return dist

# tuple generator
def all_tuples(locs):
    if len(locs) == 1:
        yield (locs.pop(),)
    else:
        for loc in locs:              # loc is the startlocation
            lc = locs.copy()
            lc.remove(loc) 
            for t in all_tuples(lc):  # lc is the rest of the locations
                yield (loc,) + t

# version 1: use a brute-force to iterate over all tuples
def process(data):
    locs = get_locs(data)
    d_max = -1
    t_max = None
    for t in all_tuples(locs):
        dist = calc_dist(data,t)
        if dist > d_max:
            d_max = dist
            t_max = t
        #print(str(dist) + " " + str(t))
    print("Maximum: " + str(d_max) + " " + str(t_max))
    
def day9(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])

