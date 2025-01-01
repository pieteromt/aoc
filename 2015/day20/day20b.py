import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data

hist = {} # must be mulitplied by 11 for total presents

def get_val(t):
    sum = 0
    for i in range(len(t)):
        sum += t[i]
    return sum

def do_elves(d):
    i = 1
    m_max = 0
    while True:
        for j in range(i,50*i+1,i):
            if j in hist:
                hist[j] += (i,)
            else:
                hist[j] = (i,)
        m = 11*get_val(hist[i])
        if m > m_max:
            #print("new max: " + str(m) + " : " + str(i) + " : " + str(hist[i]))
            print("new max: " + str(m) + " : " + str(i))
            m_max = m
        if m >= d:
            print("Found: " + str(i))
            break
        i += 1

def process(data):
    for d in data:
        do_elves(d)

def day20(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])

