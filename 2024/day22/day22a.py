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
    for i in range(0,2000):
        code = calc(code)
    return code

def day22(fname):
    read_data(fname)
    sum = 0
    for code in codes:
        val = run(code)
        print("code: " + str(code) + " val: " + str(val))
        sum = sum + val
    print("sum = " + str(sum))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day22(fname)
    else:
        print("Usage: python day22 input.txt")

