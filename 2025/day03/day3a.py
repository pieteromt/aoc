import sys

nr_bat = 2

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

# start searching at index idx
def calcn(s,idx,nr):
    n = len(s)
    ln = nr_bat - nr
    max = 0
    maxi = 0
    for i in range(n):
        if i <= idx:
            continue
        if i >= n - ln + 1:
            continue
        val = int(s[i])
        if val > max:
            max = val
            maxi = i
    return max,maxi

def calc(s):
    val = 0
    idx = -1
    for i in range(nr_bat):
        max, idx = calcn(s,idx,i)
        val = 10*val + max
    return val

def process(data):
    sum = 0
    for d in data:
        sum += calc(d)
    print(sum)

def day3(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])
