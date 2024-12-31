import sys

cache = {}

def read_data(fname):
    data = []
    f = open(fname,"r")
    state = 0
    for line in f:
        line = line.strip()
        if line:
            if state == 0:
                w = line.split()
                data.append([w[0],w[2]])
            else:
                mol = line
        else:
            state += 1
    f.close()
    return data, mol

# returns non-zero for minimal steps, or -1 if cannot reduce
# works, but slow for real input :-(
def reduce(data, mol, steps):
    if mol == "e":
        print("Found e! " + str(steps))
        return steps

    if mol in cache:
        return cache[mol]

    st_min = -1
    for d in data:
        idx = mol.find(d[1])
        if idx != -1:
            f = mol[:idx]
            r = mol[idx+len(d[1]):]
            m = f + d[0] + r
            st = reduce(data,m,steps+1)
            if st != -1:
                if st_min == -1 or st < st_min:
                    st_min = st

    cache[mol] = st_min
    return st_min

def process(data, mol):
    print("Minimum steps: " + str(reduce(data, mol, 0)))

def day19(fname):
    data, mol = read_data(fname)
    process(data, mol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])

