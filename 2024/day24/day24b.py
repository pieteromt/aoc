import sys

# we need:
# z00  ['x00', 'XOR', 'y00']
# ...
# z41 =  ['(', 'y40', 'AND', 'x40', ')', 'XOR', '(', 'y41', 'XOR', 'x41', ')']
# ...
# z45  ['x44', 'AND', 'y44', 'z45']

#sys.setrecursionlimit(15000)

inputs0 = {}
inputs = {}
rules0 = []
rules = []

rev = {}

xand = {}
xxor = {}
yand = {}
yxor = {}

zzz = {}

# to create a picture, use:
# dot -Tpng -o day24.png day24.dot
def save_dot(fname):
    f = open(fname,"w") 
    f.write("graph {\n")
    ior = 0
    iand = 0
    ixor = 0
    for r in rules:
        n0 = r[0]
        n1 = r[1]  # oper
        if n1 == "AND":
            n1 = n1 + str(iand)
            iand = iand + 1
        elif n1 == "OR":
            n1 = n1 + str(ior)
            ior = ior + 1
        elif n1 == "XOR":
            n1 = n1 + str(ixor)
            ixor = ixor + 1
        n2 = r[2]
        n3 = r[3]  # out

        f.write('"'+str(n0)+'" -- "'+str(n1)+'"' + '\n')
        f.write('"'+str(n2)+'" -- "'+str(n1)+'"' + '\n')
        f.write('"'+str(n1)+'" -- "'+str(n3)+'"' + '\n')
    f.write("}\n") 
    f.close()

def read_data(fname):
    global inputs0, rules0
    state = 0
    inputs0 = {}
    rules0 = []
    state = 0
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            if state == 0:
                words = line.split()
                inp = words[0].split(':')[0]
                val = int(words[1])
                inputs0[inp] = val
            else:
                words = line.split()
                oper1 = words[0]
                op = words[1]
                oper2 = words[2]
                out = words[4]
                rules0.append([oper1,op,oper2,out])
        else:
            state = state + 1
    f.close()

def init_inputs():
    global inputs, rules
    inputs = {}
    for inp in inputs0.keys():
        inputs[inp] = inputs0[inp]
    rules = []
    for r in rules0:
        rules.append(r.copy())
        
def reverse():
    global rev
    rev = {}
    for r in rules:
        rev[r[3]] = r

def calc_result(name):
    z = ""
    for inp in sorted(inputs.keys()):
        if inp[0] == name:
            z = str(inputs[inp]) + z
    zi = int("0b"+z,2)
    return zi
    
def swap(i,j):
    ri = rules[i].copy()
    rj = rules[j].copy()

    zi = ri[3]
    zj = rj[3]
    #print("swap: " + zi + " " + zj)

    ri[3] = zj
    rj[3] = zi

    rules[i] = ri
    rules[j] = rj

def find_out(out,show):  # find 'out' param
    ln = len(rules)
    for i in range(0,ln):
        if rules[i][3] == out:
            if show:
                print(out + " " + str(i) + " " + str(rules[i]))
            return i
    print("error: " + out)
    exit()

def swap_names(out1, out2):
    print("swap("+out1+","+out2+")")
    i1 = find_out(out1,False)
    i2 = find_out(out2,False)
    swap(i1,i2)

def zoek():
    global xand, xxor, yand, yxor, zzz
    for i in range(0,46):
        x = "x" + str(i).zfill(2)
        for r in rules:
            if (r[0] == x) or (r[2] == x):
                if r[1] == "AND":
                    xand[x] = find_out(r[3],False)
                elif r[1] == "XOR":
                    xxor[x] = find_out(r[3],False)
                #print(x + " " + str(i) + " " + str(r))

    for i in range(0,46):
        y = "y" + str(i).zfill(2)
        for r in rules:
            if (r[0] == y) or (r[2] == y):
                if r[1] == "AND":
                    yand[y] = find_out(r[3],False)
                elif r[1] == "XOR":
                    yxor[y] = find_out(r[3],False)
                #print(y + " " + str(i) + " " + str(r))

    for i in range(0,46):
        z = "z" + str(i).zfill(2)
        for r in rules:
            if r[3] == z:
                zzz[z] = find_out(z, False)

def set_x(xval):
    xb = "{0:045b}".format(xval)
    for i in range(0,45):
        x = "x" + str(i).zfill(2)
        inputs[x] = int(xb[44-i])
    
def set_y(xval):
    yb = "{0:045b}".format(xval)
    for i in range(0,45):
        y = "y" + str(i).zfill(2)
        inputs[y] = int(yb[44-i])

def evaluate(r):
    val1 = inputs[r[0]] 
    val2 = inputs[r[2]] 
    op = r[1]
    if op == "AND":
        val3 = val1 & val2
    elif op == "XOR":
        val3 = val1 ^ val2
    elif op == "OR":
        val3 = val1 | val2
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
    cnt = 0
    while (skip != 0) and (cnt < 100):
        skip = process()
        cnt = cnt + 1

def doit():
    process_all()
    x = calc_result("x")
    y = calc_result("y")
    z = calc_result("z")

    xplusy = x + y

    xor = z ^ xplusy

    sx = "x     = " + str(x).zfill(14) + " ({0:48b}".format(x) + ") (" + str(z.bit_count()) + ")\n"
    sy = "y     = " + str(y).zfill(14) + " ({0:48b}".format(y) + ") (" + str(z.bit_count()) + ")\n"
    sz = "z     = " + str(z).zfill(14) + " ({0:48b}".format(z) + ") (" + str(z.bit_count()) + ")\n"

    sxplusy = "x + y = " + str(xplusy).zfill(14) + " ({0:48b}".format(xplusy) + ") (" + str(xplusy.bit_count())+ ")\n"
    sxor    = "z ^ s = " + str(xor).zfill(14)    + " ({0:48b}".format(xor) + ") (" + str(xor.bit_count())+ ")\n"

    print(sx + sy + sxplusy + sz  + sxor)
    print("")
    return xor.bit_count()

def day24(fname):
    read_data(fname)
    init_inputs()
    zoek()
    reverse()
    swap_names("tqq","z20")
    swap_names("ksv","z06")
    swap_names("kbs","nbd")
    swap_names("z39","ckb")
    save_dot("day24.dot")
    doit()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day24(fname)
    else:
        print("Usage: python day24 input.txt")

