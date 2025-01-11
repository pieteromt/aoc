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

def do_cpy(arg0, arg1, regs):
    regs[arg1] = get_val(arg0, regs)
    regs["ip"] += 1
    
def do_inc(arg0, regs):
    regs[arg0] += 1
    regs["ip"] += 1
    
def do_dec(arg0, regs):
    regs[arg0] -= 1
    regs["ip"] += 1
    
def do_jnz(arg0, arg1, regs):
    if get_val(arg0, regs) != 0:
        regs["ip"] += get_val(arg1, regs)
    else:
        regs["ip"] += 1

def execute(instr, regs):
    if instr[0] == "cpy":
        do_cpy(instr[1], instr[2], regs)
    elif instr[0] == "inc":
        do_inc(instr[1], regs)
    elif instr[0] == "dec":
        do_dec(instr[1], regs)
    elif instr[0] == "jnz":
        do_jnz(instr[1], instr[2], regs)
    else:
        print("Error: " + str(instr))
        exit()

def process(data,regs):
    ip = regs["ip"]
    while ((ip >= 0) and (ip < len(data))):
        execute(data[ip], regs)
        ip = regs["ip"]
    print("a = " + str(regs["a"]))

def day12(fname):
    data = read_data(fname)
    regs = {}
    regs["a"] = 0
    regs["b"] = 0
    regs["c"] = 0
    regs["d"] = 0
    regs["ip"] = 0
    process(data,regs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])

