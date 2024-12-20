import sys

data = []

def read_data(fname):
    global data
    data = []
    f = open(fname,"r")
    puzzle = []
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
                    puzzle.append(int(ww[1]))
            elif line[:8] == "Button B":
                line = line[9:]
                line = line.strip()
                words = line.split(",")
                for w in words:
                    w = w.strip()
                    ww = w.split('+')
                    #print(ww[1])
                    puzzle.append(int(ww[1]))
            elif line[:5] == "Prize":
                line = line[6:]
                line = line.strip()
                #print(line)
                words = line.split(",")
                for w in words:
                    w = w.strip()
                    ww = w.split('=')
                    #print(ww[1])
                    puzzle.append(int(ww[1]))
                data.append(puzzle)
                #print(puzzle)
                puzzle = []
            else:
                pass
    f.close()

def do_puzzle(p):
    min_cost = -1
    min_a = -1
    min_b = -1
    for a in range(0,100):
        if a*p[0] > p[4]:
            break
        for b in range(0,100):
            sum_1 = a*p[0] + b*p[2]
            sum_2 = a*p[1] + b*p[3]
            if (sum_1 > p[4]) or (sum_2 > p[5]):
                break
            if (sum_1 == p[4]) and (sum_2 == p[5]):
                cost = 3*a + b
                if min_cost == -1:
                    min_cost = cost
                    min_a = a
                    min_b = b
                elif cost < min_cost:
                    min_cost = cost
                    min_a = a
                    min_b = b
                #print("a = " + str(a) + ", b = " + str(b) + ", cost = " + str(cost))
    #print("MIN a = " + str(min_a) + ", b = " + str(min_b) + ", cost = " + str(min_cost))
    if min_cost == -1:
        return 0
    else:
        return min_cost
     
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

