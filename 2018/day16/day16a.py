import sys

def get_four(line):
    line = line.replace("[","").replace("]","").replace(",","")
    w = line.split()
    w.pop(0)
    return list(map(int,w))

def read_data(fname):
    samples = []
    program = []
    f = open(fname,"r")
    state = 0
    for line in f:
        line = line.strip()
        if len(line) > 0:
            empty = 0
            w = line.split()
            if state == 0:
                if w[0] == "Before:":
                    b = get_four(line)
                elif w[0] == "After:":
                    a = get_four(line)
                    samples.append((b,instr,a))
                else:
                    instr = tuple(map(int,w))
            else:
                program.append(tuple(map(int,w)))
        else:
            empty += 1
            if empty >= 3:
                state = 1  # part 2
    f.close()
    return samples, program
    
def show_regs(regs):
    r0 = regs[0]
    r1 = regs[1]
    r2 = regs[2]
    r3 = regs[3]
    print("r0: " + str(r0) + ", r1: " + str(r1) + \
          ", r2: " + str(r2) + ", r3: " + str(r3))

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

# returns True if match
def execute(sample, func):
    before, instr, after = sample
    regs = {}
    regs = before.copy()
    #show_regs(regs)
    func(instr,regs)
    #show_regs(regs)
    return regs == after

def count_match(sample):
    funcs = [ addr, addi, mulr, muli, banr, bani, borr, bori,
              setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    n = 0
    for func in funcs:
        if execute(sample, func):
            n += 1
    return n

def process(samples):
    cnt = 0
    for sample in samples:
        if count_match(sample) >= 3:
            cnt += 1
    print(cnt)

def day16(fname):
    samples, program = read_data(fname)
    process(samples)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day16 input.txt") 
    else:
    	day16(sys.argv[1])
