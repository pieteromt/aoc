import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 2:
            instr = w[0]
            arg0 = w[1]
            data.append((instr,arg0))
        else:
            instr = w[0]
            arg0 = w[1]
            arg1 = w[2]
            data.append((instr,arg0,arg1))
    f.close()
    return data

def check_int(arg):
    try:
        value = int(arg)
        return True
    except ValueError:
        return False

def get_val(arg0, regs):
    if check_int(arg0):
        return int(arg0)
    else:
        return regs[arg0]

def do_jnz(arg0, arg1, regs):
    if get_val(arg0, regs) != 0:
        regs["ip"] += get_val(arg1, regs)
    else:
        regs["ip"] += 1

nr_mul = 0   # yeah, kinda lame, using a global var...

def do_mul(arg0, arg1, regs):
    global nr_mul
    nr_mul += 1
    regs[arg0] = get_val(arg0, regs) * get_val(arg1, regs)
    regs["ip"] += 1

def do_set(arg0, arg1, regs):
    regs[arg0] = get_val(arg1, regs)
    regs["ip"] += 1

def do_sub(arg0, arg1, regs):
    regs[arg0] = get_val(arg0, regs) - get_val(arg1, regs)
    regs["ip"] += 1

def show_regs(regs):
    a = regs["a"]
    b = regs["b"]
    c = regs["c"]
    d = regs["d"]
    e = regs["e"]
    f = regs["f"]
    g = regs["g"]
    h = regs["h"]
    ip = regs["ip"]
    print("ip: " + str(ip) + ", a: " + str(a) + ", b: " + str(b) + \
          ", c: " + str(c) + ", d: " + str(d) + \
          ", e: " + str(e) + ", f: " + str(f) + \
          ", g: " + str(g) + ", h: " + str(h))

def execute(instr, regs):
    #show_regs(regs)
    if instr[0] == "jnz":
        do_jnz(instr[1], instr[2], regs)
    elif instr[0] == "mul":
        do_mul(instr[1], instr[2], regs)
    elif instr[0] == "set":
        do_set(instr[1], instr[2], regs)
    elif instr[0] == "sub":
        do_sub(instr[1], instr[2], regs)
    else:
        print("Error: " + str(instr))
        exit()

def process(data,regs):
    ip = regs["ip"]
    while ((ip >= 0) and (ip < len(data))):
        execute(data[ip], regs)
        ip = regs["ip"]
    print("mul = " + str(nr_mul))

def day23(fname):
    data = read_data(fname)
    regs = {}
    regs["a"] = 0
    regs["b"] = 0
    regs["c"] = 0
    regs["d"] = 0
    regs["e"] = 0
    regs["f"] = 0
    regs["g"] = 0
    regs["h"] = 0
    regs["ip"] = 0
    process(data,regs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day23 input.txt") 
    else:
    	day23(sys.argv[1])

