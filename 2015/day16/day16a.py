import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip() + ","  # trailing comma...
        w = line.split()
        items = {}
        if len(w) == 8:
            nr = int(w[1][:-1])
            for i in range(1,4):
                item = w[2*i][:-1]
                count = int(w[2*i+1][:-1])
                items[item] = count
            data.append(items)
        else:
            print("error: " + str(len(w)))
            exit()
    f.close()
    return data

def read_gifts(fname):
    gifts = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 2:
            item = w[0][:-1]
            count = int(w[1])
            gifts[item] = count
        else:
            print("error: " + str(len(w)))
            exit()
    f.close()
    return gifts

def is_match(d, gifts):
    for item in d:
        if d[item] != gifts[item]:
            return False
    return True

def process(data,gifts):
    nr = len(data)
    for i in range(0,nr):
        if is_match(data[i],gifts):
            print("Match! Sue " + str(i+1))

def day16(fname1,fname2):
    data = read_data(fname1)
    gifts = read_gifts(fname2)
    process(data,gifts)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: day16 input.txt gifts.txt") 
    else:
    	day16(sys.argv[1], sys.argv[2])

