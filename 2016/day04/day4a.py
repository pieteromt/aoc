import sys

# input looks like: aaaaa-bbb-z-y-x-123[abxyz]
def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.replace('[',' ').replace(']','').split()  # get rid of []
        ww = w[0].split('-')
        id = int(ww[-1])
        name = "".join(ww[:-1])
        checksum = w[1]
        data.append((name,id,checksum))
    f.close()
    return data
    
def make_hist(name):
    hist = {}
    for c in name:
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
    return hist

def reverse_hist(h):
    hist = {}
    for c in h:
        n = h[c]
        if n in hist:
            hist[n] += [c]
        else:
            hist[n] = [c]
    return hist

def calc_checksum(hist):
    checksum = ""
    for key in reversed(sorted(hist.keys())):
        for c in sorted(hist[key]):
            checksum += c
    return checksum[:5]

def is_real_room(t):
    name, id, checksum = t
    hist = make_hist(name)
    hist = reverse_hist(hist)
    return calc_checksum(hist) == checksum

def process(data):
    ids = 0
    for t in data:
        if is_real_room(t):
            ids += t[1]
    print("Sum of IDs = " + str(ids))

def day4(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])

