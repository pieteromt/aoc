import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        nr = len(w)
        if nr == 3:
            inp = w[0]
            out = w[2]
            if inp.isnumeric():
                inp = int(inp)
            op = "ASSIGN"
            data.append((op,inp,out))
        elif nr == 4:
            op = w[0]
            inp = w[1]
            if inp.isnumeric():
                inp = int(inp)
            out = w[3]
            data.append((op,inp,out))
        elif nr == 5:
            inp1 = w[0]
            if inp1.isnumeric():
                inp1 = int(inp1)
            op = w[1]
            inp2 = w[2]
            if inp2.isnumeric():
                inp2 = int(inp2)
            out = w[4]
            data.append((op,inp1,inp2,out))
        else:
            print("error: nr = " + str(nr))
            exit()
    f.close()
    return data

# returns None if unknown
def get_val(r,regs):
    if type(r) == int:
        return r
    if r in regs:
        return regs[r]
    return None

def set_out(r,val,regs):
    if not r in regs:
        regs[r] = val

def do_assign(instr,regs):
    op,inp,out = instr
    inp = get_val(inp,regs)
    if inp != None:
        set_out(out, inp, regs)
        return True
    else:
        return False  # don't know input value yet

def not_val(val):
    return ~val + 2**16  # make unsigned 16-bit value

def do_not(instr,regs):
    op,inp,out = instr
    inp = get_val(inp,regs)
    if inp != None:
        set_out(out, not_val(inp), regs)
        return True
    else:
        return False  # don't know input value yet

def do_and(instr,regs):
    op,inp1,inp2,out = instr
    inp1 = get_val(inp1,regs)
    inp2 = get_val(inp2,regs)
    if inp1 != None and inp2 != None:
        set_out(out, inp1 & inp2, regs)
        return True
    else:
        return False  # don't know (one of) input values yet

def do_or(instr,regs):
    op,inp1,inp2,out = instr
    inp1 = get_val(inp1,regs)
    inp2 = get_val(inp2,regs)
    if inp1 != None and inp2 != None:
        set_out(out, inp1 | inp2, regs)
        return True
    else:
        return False  # don't know (one of) input values yet

def do_lshift(instr,regs):
    op,inp1,inp2,out = instr
    inp1 = get_val(inp1,regs)
    inp2 = get_val(inp2,regs)
    if inp1 != None and inp2 != None:
        set_out(out, inp1 << inp2, regs)
        return True
    else:
        return False  # don't know (one of) input values yet

def do_rshift(instr,regs):
    op,inp1,inp2,out = instr
    inp1 = get_val(inp1,regs)
    inp2 = get_val(inp2,regs)
    if inp1 != None and inp2 != None:
        set_out(out, inp1 >> inp2, regs)
        return True
    else:
        return False  # don't know (one of) input values yet

# returns True if successful execution
# for successful execution, all inputs need to be available
def execute(instr,regs):
    if instr[0] == "ASSIGN":
        return do_assign(instr,regs)
    elif instr[0] == "NOT":
        return do_not(instr,regs)
    elif instr[0] == "AND":
        return do_and(instr,regs)
    elif instr[0] == "OR":
        return do_or(instr,regs)
    elif instr[0] == "LSHIFT":
        return do_lshift(instr,regs)
    elif instr[0] == "RSHIFT":
        return do_rshift(instr,regs)
    else:
        print("error: nr = " + str(nr))
        exit()

# reassign a new value to a register in the assignment instructions
def reassign(r,val,data):
    for i in range(len(data)):
        instr = data[i]
        if instr[0] == "ASSIGN":
            op,inp,out = instr
            if out == r:
                data[i] = (op,val,out)

def do_run(data):
    regs = {}
    done = False
    while not done:
        done = True
        for instr in data:
            if not execute(instr,regs):
                done = False
    return regs

def process(data):
    regs = do_run(data)
    reassign("b", regs["a"], data)
    regs = do_run(data)
    r = "a"
    print(r + ": " + str(regs[r]))

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])

