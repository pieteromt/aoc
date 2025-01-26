import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(int(w[4]))
    f.close()
    return data
    
def process(data):
    val_a = data[0]
    val_b = data[1]
    match = 0
    for i in range(40000000):
        val_a = (16807 * val_a) % 2147483647
        val_b = (48271 * val_b) % 2147483647
        #print(str(val_a) + "     " + str(val_b))
        #print("{0:032b}".format(val_a))
        #print("{0:032b}".format(val_b))
        #print("")
        if (val_a & 0xffff) == (val_b & 0xffff):
            match += 1
    print("match = " + str(match))

def day15(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])

