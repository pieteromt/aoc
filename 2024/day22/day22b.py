import sys

#sys.setrecursionlimit(15000)

codes = []

def read_data(fname):
    global codes
    codes = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            codes.append(int(line))
    f.close()

def calc(val):
    val1 = val<<6
    val  = val1 ^ val
    val  = val % 16777216
    val4 = val>>5
    val  = val4 ^ val
    val  = val % 16777216
    val7 = val<<11
    val  = val7 ^ val
    val  = val % 16777216
    return val

def test():
    val = 123
    for i in range(0,10):
        val = calc(val)
        print(str(val))

def run(code):
    one = []
    delta = []
    one.append(code%10)
    for i in range(0,2000):
        code = calc(code)
        one.append(code%10)
        delta.append(one[-1] - one[-2])
    return one, delta

def calc_seq(one, delta):
    seqs = {}
    for i in range(0,2000 - 3):
        seq = (delta[i],delta[i+1],delta[i+2],delta[i+3])
        val = one[i+4]
        if not seq in seqs:  # first occurrence
            seqs[seq] = val
    return seqs

def process():
    all_seqs = []
    for code in codes:
        one, delta = run(code)
        seqs = calc_seq(one, delta)
        all_seqs.append(seqs)
    join = {}
    for seqs in all_seqs:
        for seq in seqs.keys():
            val = seqs[seq]
            if not seq in join:
                join[seq] = val
            else:
                join[seq] += val
    max_val = 0
    max_seq = None
    for seq in join.keys():
        val = join[seq]
        if val > max_val:
            max_val = val
            max_seq = seq
    print("val = " + str(max_val) + ", seq = " + str(max_seq))

def day22(fname):
    read_data(fname)
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day22(fname)
    else:
        print("Usage: python day22 input.txt")
