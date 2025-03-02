import sys

def read_data(fname):
    program = []
    f = open(fname,"r")
    state = 0
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 2:
            instr = ("ip", int(w[1]))
        else:
            instr = (w.pop(0),) + tuple(map(int,w))
        program.append(instr)
    f.close()
    return program
    

def get_func(name):
    funcs = [ (addr, "addr"), (addi, "addi"), (mulr, "mulr"), (muli, "muli"), \
              (banr, "banr"), (bani, "bani"), (borr, "borr"), (bori, "bori"), \
              (setr, "setr"), (seti, "seti"), (gtir, "gtir"), (gtri, "gtri"), \
              (gtrr, "gtrr"), (eqir, "eqir"), (eqri, "eqri"), (eqrr, "eqrr") ]
    for t in funcs:
        if t[1] == name:
            return t[0]
    print("get_func error: name = " + name)
    exit()

def show_regs(regs):
    print(" [",end='')
    for i in range(len(regs)):
        if i>0:
            print(",",end='')
        print(" "+str(regs[i]),end='')
    print("] ",end='')

def addr(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] + regs[B]

def addi(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] + B

def mulr(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] * regs[B]

def muli(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] * B

def banr(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] & regs[B]

def bani(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] & B

def borr(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] | regs[B]

def bori(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A] | B

def setr(instr, regs):
    op, A, B, C = instr
    regs[C] = regs[A]

def seti(instr, regs):
    op, A, B, C = instr
    regs[C] = A

def gtir(instr, regs):
    op, A, B, C = instr
    if A > regs[B]:
        regs[C] = 1
    else:
        regs[C] = 0

def gtri(instr, regs):
    op, A, B, C = instr
    if regs[A] > B:
        regs[C] = 1
    else:
        regs[C] = 0

def gtrr(instr, regs):
    op, A, B, C = instr
    if regs[A] > regs[B]:
        regs[C] = 1
    else:
        regs[C] = 0

def eqir(instr, regs):
    op, A, B, C = instr
    if A == regs[B]:
        regs[C] = 1
    else:
        regs[C] = 0

def eqri(instr, regs):
    op, A, B, C = instr
    if regs[A] == B:
        regs[C] = 1
    else:
        regs[C] = 0

def eqrr(instr, regs):
    op, A, B, C = instr
    if regs[A] == regs[B]:
        regs[C] = 1
    else:
        regs[C] = 0

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice if it's perfect square
                divisors.append(n // i)
    return sorted(divisors)

def execute(program):
    regs = {}
    regs[0] = 1
    regs[1] = 0
    regs[2] = 0
    regs[3] = 0
    regs[4] = 0
    regs[5] = 0
    op, ip_reg = program.pop(0)  # get ip_reg
    ip = 0
    cnt = 0
    while (ip >= 0) and (ip < len(program)):
        show = False
        instr = program[ip]
        op, A, B, C = instr  # get opcode
        func = get_func(op)
        regs[ip_reg] = ip
        if show:
            print("ip="+str(ip),end='')
            show_regs(regs)
            print(instr,end='')
        func(instr, regs)
        if show:
            show_regs(regs)
            print("")
        ip = regs[ip_reg]
        ip += 1
        cnt += 1
        if regs[0] == 0:
            break
    # Reverse engineering of the program:
    print("Calculate sum of divisors of value in r[1] (" + str(regs[1]) + "), result = ", end='')
    divs = find_divisors(regs[1])
    print(sum(divs))

def day19(fname):
    program = read_data(fname)
    execute(program)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])
