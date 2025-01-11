import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def reverse(b):
    s = ""
    ln = len(b)
    for i in range(ln):
        s += b[ln-1 - i]
    return s

def invert(b):
    s = ""
    for i in range(len(b)):
        if b[i] == "0":
            s += "1"
        else:
            s += "0"
    return s

def make_data(a):
    b = a
    b = reverse(b)
    b = invert(b)
    return a + "0" + b

def test(a):
    d = make_data(a)
    print(a + " -> " + d)

def tests():
    test("1")
    test("0")
    test("11111")
    test("111100001010")

def make_enough_data(a, size):
    while True:
        if len(a) >= size:
            break
        a = make_data(a)
    return a

def checksum(a):
    sum = ""
    for i in range(len(a)//2):
        if a[2*i] == a[2*i+1]:
            sum += "1"
        else:
            sum += "0"
    return sum    

def make_checksum(a):
    while True:
        a = checksum(a)
        if len(a)%2 != 0:
            break
    return a

def calc(a,size):
    aa = make_enough_data(a,size)
    aaa = aa[:size]
    sum = make_checksum(aaa)
    print("Checksum: " + sum)

def test2():
    a = "10000"
    size = 20
    calc(a,size)

def process(data):
    size = 35651584
    for a in data:
        calc(a,size)

def day16(fname):
    data = read_data(fname)
    process(data)
    #test2()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day16 input.txt") 
    else:
    	day16(sys.argv[1])

