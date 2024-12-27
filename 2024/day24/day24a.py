import sys

#sys.setrecursionlimit(15000)

inputs = {}
rules = []

def read_data(fname):
    global inputs, rules
    state = 0
    inputs = {}
    rules = []
    state = 0
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            if state == 0:
                words = line.split()
                inp = words[0].split(':')[0]
                val = int(words[1])
                inputs[inp] = val
            else:
                words = line.split()
                oper1 = words[0]
                op = words[1]
                oper2 = words[2]
                out = words[4]
                rules.append([oper1,op,oper2,out])
        else:
            state = state + 1
    f.close()

def evaluate(r):
    val1 = inputs[r[0]] 
    val2 = inputs[r[2]] 
    op = r[1]
    if op == "AND":
        val3 = val1 and val2
    elif op == "XOR":
        val3 = val1 ^ val2
    elif op == "OR":
        val3 = val1 or val2
    else:
        print("error: " + op)
        exit()
    inputs[r[3]] = val3

def process():
    skip = 0
    done = 0
    for r in rules:
        if (r[0] in inputs) and (r[2] in inputs):  # can evaluate
            if not r[3] in inputs:
                evaluate(r)
            else:
                done = done + 1
        else:
            skip = skip + 1
    return skip

def process_all():
    skip = process()
    while skip != 0:
        #print("skip: " + str(skip))
        skip = process()

def calc_result():
    z = ""
    for inp in sorted(inputs.keys()):
        if inp[0] == 'z':
            z = str(inputs[inp]) + z
    print("z = " + z)
    zi = int("0b"+z,2)
    print("zi = " + str(zi))
    

def day24(fname):
    read_data(fname)
    #for inp in inputs.keys():
    #    print(inp + " " + str(inputs[inp]))
    #for r in rules:
    #    print(str(r))
    process_all()
    for inp in sorted(inputs.keys()):
        print(inp + " " + str(inputs[inp]))
    calc_result()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day24(fname)
    else:
        print("Usage: python day24 input.txt")

