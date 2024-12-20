import sys

#sys.setrecursionlimit(15000)

data1 = []   # pat
data2 = []   # des

# colors
# 0 w  white
# 1 u  blue
# 2 b  black
# 3 r  red
# 4 g  gree

bucket = []

endings = []

def make_buckets():
    global bucket,endings
    bucket = []
    max_len = 0
    for pat in data1:
        pat_len = len(pat)
        if pat_len > max_len:
            max_len = pat_len
    #print("max_len = " + str(max_len))      # 8
    for i in range(0,max_len):
        bucket.append([])
    for pat in data1:
        pat_len = len(pat)
        bucket[pat_len-1].append(pat)
    #print(str(bucket))     
    #print("")
    #print(str(bucket[0]))     
    #print("")
    endings = []
    for p1 in bucket[0]:
        endings.append(p1)
    for i in range(1,max_len):
        b2s = [] # starts with 'g'
        b2e = [] # ends with 'g'
        b2r = [] # no g
        for pi in bucket[i]:
            if pi[0] == 'g':
                b2s.append(pi)
            if pi[-1] == 'g':
                b2e.append(pi)
                endings.append(pi)
            if not 'g' in pi:
                b2r.append(pi)
        #print("")
        #print(str(b2s) + "   " + str(b2e) + "   " + str(b2r))
        #print("")
    #print(str(endings)) 

def read_data(fname):
    global data1, data2
    f = open(fname,"r")
    state = 0
    data1 = []
    data2 = []
    for line in f:
        line = line.strip()
        if line:
            if state == 0:
                words = line.split(',')
                for w in words:
                    w = w.strip()
                    data1.append(w)
            else:
                data2.append(line)
        else:
            state = state + 1
    f.close()


# returns True if match
def check(des):
    match = False
    if not 'g' in des:
        return True
    else:
        if des[-1] != 'g':  # doesn't end with 'g'
            return True
        for ee in endings:
            if des.endswith(ee):
                n = len(des) - len(ee)
                match = check(des[:n])
                if match:
                    break
    return match

def process():
    sum = 0
    other = 0
    for des in data2:
        #print("START: " + des)
        if check(des):
            #print("YES " + des)
            sum = sum + 1
        else:
            #print("NO  " + des)
            other = other + 1
        #print("END: " + des)
        #print("")
    print("sum = " + str(sum) + ", other = " + str(other))

def day19(fname):
    read_data(fname)
    #print("Patterns:")
    #for pat in data1:
    #    print(pat)
    #print("Designs:")
    #for des in data2:
    #    print(des)
    make_buckets()
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day19(fname)
    else:
        print("Usage: python day19 input.txt")

