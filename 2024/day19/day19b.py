import sys

#sys.setrecursionlimit(15000)

max_pat = 0  # maximum pattern size
data1 = []   # pat (patterns)
data2 = []   # des (designs)

# colors
# 0 w  white
# 1 u  blue
# 2 b  black
# 3 r  red
# 4 g  gree

def read_data(fname):
    global data1, data2, max_pat
    f = open(fname,"r")
    state = 0
    max_pat = 0
    data1 = []
    data2 = []
    for line in f:
        line = line.strip()
        if line:
            if state == 0:
                words = line.split(',')
                for w in words:
                    w = w.strip()
                    ln = len(w)
                    if ln > max_pat:
                        max_pat = ln
                    data1.append(w)
            else:
                data2.append(line)
        else:
            state = state + 1
    f.close()

# https://en.wikipedia.org/wiki/Memoization
def calc_perm(des):
    ln = len(des)
    perm = [0] * (ln + 1)
    perm[0] = 1
    for i in range(1, ln + 1):
        start = i - 1
        end   = max(i - max_pat - 1, -1)
        for j in range(start, end, -1):
            if des[j:i] in data1:
                perm[i] += perm[j]
    return perm[ln]    

def process():
    sum = 0
    for des in data2:
        sum = sum + calc_perm(des)
    print("sum = " + str(sum))

def day19(fname):
    read_data(fname)
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day19(fname)
    else:
        print("Usage: python day19 input.txt")

