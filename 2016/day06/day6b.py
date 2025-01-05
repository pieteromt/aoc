import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
def reverse_hist(h):
    hist = {}
    for c in h:
        n = h[c]
        if n in hist:
            hist[n] += [c]
        else:
            hist[n] = [c]
    return hist

def most_common(data,i):
    hist = {}
    for d in data:
        c = d[i]
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
    hist = reverse_hist(hist)
    return hist[min(hist.keys())][0]

def process(data):
    code = ""
    for i in range(len(data[0])):
        code += most_common(data,i)
    print("code = " + code)

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])
