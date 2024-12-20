import sys

data = []

def mult(fa):
    value = 1
    for f in fa:
        value = value * f
    return value

def read_data(fname):
    global data
    data = []
    f = open(fname,"r")
    p = []
    for line in f:
        line = line.strip()
        if line:
            if line[:8] == "Button A":
                line = line[9:]
                line = line.strip()
                words = line.split(",")
                for w in words:
                    w = w.strip()
                    ww = w.split('+')
                    #print(ww[1])
                    p.append(int(ww[1]))
            elif line[:8] == "Button B":
                line = line[9:]
                line = line.strip()
                words = line.split(",")
                for w in words:
                    w = w.strip()
                    ww = w.split('+')
                    #print(ww[1])
                    p.append(int(ww[1]))
            elif line[:5] == "Prize":
                line = line[6:]
                line = line.strip()
                #print(line)
                words = line.split(",")
                for w in words:
                    w = w.strip()
                    ww = w.split('=')
                    #print(ww[1])
                    p.append(int(ww[1]) + 10000000000000)
                    #p.append(int(ww[1]))
                data.append(p)
                #print(p)
                p = []
            else:
                pass
    f.close()

def check(p,a,b):
    sum_1 = a*p[0] + b*p[2]
    sum_2 = a*p[1] + b*p[3]
    if (sum_1 == p[4]) and (sum_2 == p[5]):
        #print("match: a = " + str(a) + ", b = " + str(b))
        return True
    else:
        return False

def do_puzzle(p):
    sum = 0
    max_a1 = p[4]//p[0]
    max_a2 = p[5]//p[1]
    max_a = max_a1
    if max_a2 < max_a:
        max_a = max_a2
    max_b1 = p[4]//p[2]
    max_b2 = p[5]//p[3]
    max_b = max_b1
    if max_b2 < max_b:
        max_b = max_b2
    #print("max_a = " + str(max_a) + ", max_b = " + str(max_b))

    dv1 = (p[1]*p[4] - p[0]*p[5])
    rm1 = (p[1]*p[2] - p[0]*p[3])
    b = dv1//rm1
    #print("div = " + str(dv1) + ", rem = " + str(rm1) + ", b = " + str(b))
    dv2 = (p[4] - b*p[2])
    rm2 = p[0]
    a = dv2//rm2
    #print("div = " + str(dv2) + ", rem = " + str(rm2) + ", a = " + str(a))
    if check(p,a,b):
        sum = 3*a + b
    return sum

def process():
    sum = 0
    i = 0
    for p in data:
        #print(p)
        sum_i = do_puzzle(p)
        #print(str(i) + " : " + str(sum_i))
        sum = sum + sum_i
        i = i + 1
    print("sum = " + str(sum))

def day13(fname):
    read_data(fname)
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])

