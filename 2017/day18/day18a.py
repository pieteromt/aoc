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

last_freq = 0

def get_val(arg0, regs):
    if check_int(arg0):
        return int(arg0)
    else:
        return regs[arg0]

def do_add(arg0, arg1, regs):
    regs[arg0] = get_val(arg0, regs) + get_val(arg1, regs)
    regs["ip"] += 1

def do_jgz(arg0, arg1, regs):
    if get_val(arg0, regs) > 0:
        regs["ip"] += get_val(arg1, regs)
    else:
        regs["ip"] += 1

def do_mod(arg0, arg1, regs):
    regs[arg0] = get_val(arg0, regs) % get_val(arg1, regs)
    regs["ip"] += 1

def do_mul(arg0, arg1, regs):
    regs[arg0] = get_val(arg0, regs) * get_val(arg1, regs)
    regs["ip"] += 1

def do_rcv(arg0, regs):
    if get_val(arg0, regs) != 0:
        print("Recover " + str(last_freq))
        exit()
    regs["ip"] += 1

def do_set(arg0, arg1, regs):
    regs[arg0] = get_val(arg1, regs)
    regs["ip"] += 1

def do_snd(arg0, regs):
    global last_freq
    freq = get_val(arg0, regs)
    print("play sound: " + str(freq))
    last_freq = freq
    regs["ip"] += 1

def show_regs(regs):
    a = regs["a"]
    b = regs["b"]
    f = regs["f"]
    i = regs["i"]
    p = regs["p"]
    ip = regs["ip"]
    print("ip: " + str(ip) + ", a: " + str(a) + ", b: " + str(b) + ", f: " + str(f) + ", i: " + str(i) + ", p: " + str(p))

def execute(instr, regs):
    #show_regs(regs)
    if instr[0] == "add":
        do_add(instr[1], instr[2], regs)
    elif instr[0] == "jgz":
        do_jgz(instr[1], instr[2], regs)
    elif instr[0] == "mod":
        do_mod(instr[1], instr[2], regs)
    elif instr[0] == "mul":
        do_mul(instr[1], instr[2], regs)
    elif instr[0] == "rcv":
        do_rcv(instr[1], regs)
    elif instr[0] == "set":
        do_set(instr[1], instr[2], regs)
    elif instr[0] == "snd":
        do_snd(instr[1], regs)
    else:
        print("Error: " + str(instr))
        exit()

def process(data,regs):
    ip = regs["ip"]
    while ((ip >= 0) and (ip < len(data))):
        execute(data[ip], regs)
        ip = regs["ip"]

def day18(fname):
    data = read_data(fname)
    regs = {}
    #for ch in "abcdefghijklmnopqrstuvwxyz":
    #    regs[ch] = 0
    regs["a"] = 0
    regs["b"] = 0
    regs["f"] = 0
    regs["i"] = 0
    regs["p"] = 0
    regs["ip"] = 0
    process(data,regs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18 input.txt") 
    else:
    	day18(sys.argv[1])

