import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line.startswith("/dev/grid"):
            w = line.split()
            dev = w[0].split('-')
            x = int(dev[1][1:])
            y = int(dev[2][1:])
            size = int(w[1][:-1])
            used = int(w[2][:-1])
            avail = int(w[3][:-1])
            use = int(w[4][:-1])
            data.append((x,y,size,used,avail,use))
    f.close()
    return data
    
def is_same(di, dj):
    return (di[0] == dj[0]) and (di[1] == dj[1])

def is_viable(di, dj):
    if is_same(di,dj):
        return False
    xi, yi, sizei, usedi, availi, usei = di
    xj, yj, sizej, usedj, availj, usej = dj
    return (usedi != 0) and (usedi <= availj)

def is_connected(di, dj):
    xi, yi, sizei, usedi, availi, usei = di
    xj, yj, sizej, usedj, availj, usej = dj
    return abs(xi - xj) + abs(yi - yj) == 1

def is_viable_connected(di,dj):
    return is_viable(di,dj) and is_connected(di,dj)
    
def viable(data):
    ln = len(data)
    vi = 0
    vic = 0
    for i in range(ln):
        xi, yi, sizei, usedi, availi, usei = data[i]
        for j in range(ln):
            xj, yj, sizej, usedj, availj, usej = data[j]
            ti = (xi,yi)
            tj = (xj,yj)
            if is_viable(data[i], data[j]):
                vi += 1
                #print(str(ti) + " " + str(tj) + ", sizei = " + str(sizei) + \
                #       ", usedi = " + str(usedi) + ", availj = " + str(availj))
            if is_viable_connected(data[i], data[j]):
                print("viable connected: " + str(ti) + " " + str(tj))
                vic += 1
    print("viable: " + str(vi) + ", viable connected = " + str(vic) + ", total = " + str(ln))

def process(data):
    #for d in data:
    #    print(d)
    viable(data)

def day22(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day22 input.txt") 
    else:
    	day22(sys.argv[1])

