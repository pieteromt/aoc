import sys

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

def process(data, mol):
    s = set()
    for d in data:
        start = 0
        ln = len(d[0])
        while True:
            idx = mol.find(d[0],start)
            if idx == -1:
                break
            new_mol = mol[:idx] + d[1] + mol[idx+ln:]
            #print(new_mol)
            s.add(new_mol)
            start = idx+ln
    print("Distinct: " + str(len(s)))

def day19(fname):
    data, mol = read_data(fname)
    process(data, mol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])

