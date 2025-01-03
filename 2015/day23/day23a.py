import sys

def read_data(fname):
    f = open(fname,"r")
    data = []
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 2:
            if w[0] == 'jmp':
                w[1] = int(w[1])
            data.append((w[0],w[1]))
        elif len(w) == 3:
            w[1] = w[1][:-1] # remove comma
            w[2] = int(w[2])
            data.append((w[0],w[1],w[2]))
        else:
            print("Error: " + str(len(w)))
            exit()
    f.close()
    return data
    
def hlf(regs,reg):
    regs[reg] //= 2
    regs["ip"] += 1

def tpl(regs,reg):
    regs[reg] *= 3
    regs["ip"] += 1

def inc(regs,reg):
    regs[reg] += 1
    regs["ip"] += 1

def jmp(regs,off):
    regs["ip"] += off

def jie(regs,reg,off):
    if regs[reg]%2 == 0:  # even?
        regs["ip"] += off
    else:
        regs["ip"] += 1

def jio(regs,reg,off):
    if regs[reg] == 1:
        regs["ip"] += off
    else:
        regs["ip"] += 1

def execute_instr(instr, regs):
    opcode = instr[0]
    reg = instr[1]
    if opcode == "hlf":
        hlf(regs, reg)
    elif opcode == "tpl":
        tpl(regs,reg)
    elif opcode == "inc":
        inc(regs,reg)
    elif opcode == "jmp":
        off = instr[1]
        jmp(regs,off)
    elif opcode == "jie":
        off = instr[2]
        jie(regs,reg,off)
    elif opcode == "jio":
        off = instr[2]
        jio(regs,reg,off)
    else:
        print("Error: " + opcode)
        exit()

def execute_prog(prog,regs):
    ip = regs["ip"]
    while (ip >= 0) and (ip < len(prog)):
        execute_instr(prog[ip],regs)
        ip = regs["ip"]

def process(prog):
    regs = {}
    regs["ip"] = 0
    regs["a"] = 0
    regs["b"] = 0
    execute_prog(prog, regs)
    print("a = " + str(regs["a"]))
    print("b = " + str(regs["b"]))

def day23(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day23 input.txt") 
    else:
    	day23(sys.argv[1])

