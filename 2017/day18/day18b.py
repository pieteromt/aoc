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

# returns True if a value was received
def do_rcv(arg0, regs, queue):
    if len(queue) > 0:
        regs[arg0] = queue.pop(0)
        print("Received " + str(regs[arg0]))
        regs["ip"] += 1
        return True
    else:
        print("Receive failed!")
        return False

def do_set(arg0, arg1, regs):
    regs[arg0] = get_val(arg1, regs)
    regs["ip"] += 1

def do_snd(arg0, regs, queue):
    val = get_val(arg0, regs)
    print("Sending " + str(val))
    queue.append(val)
    regs["snd"] += 1
    regs["ip"] += 1

def show_regs(regs):
    a = regs["a"]
    b = regs["b"]
    f = regs["f"]
    i = regs["i"]
    p = regs["p"]
    ip = regs["ip"]
    print("ip: " + str(ip) + ", a: " + str(a) + ", b: " + str(b) + ", f: " + str(f) + ", i: " + str(i) + ", p: " + str(p))

# returns True if the instructed was executed succesfully
def execute(instr, regs, r_queue, s_queue):
    result = True
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
        result = do_rcv(instr[1], regs, r_queue)
    elif instr[0] == "set":
        do_set(instr[1], instr[2], regs)
    elif instr[0] == "snd":
        do_snd(instr[1], regs, s_queue)
    else:
        print("Error: " + str(instr))
        exit()
    return result

# returns the number of instructions executed
def run_program(data, pid, regs, s_queue, r_queue):
    nr = 0
    print("Running program " + str(pid))
    ip = regs["ip"]
    while ((ip >= 0) and (ip < len(data))):
        if execute(data[ip], regs, s_queue, r_queue):
            nr += 1
            ip = regs["ip"]
        else:
            # receive failed; switch programs
            break
    return nr

def create_program(pid):
    regs = {}
    regs["a"] = 0
    regs["b"] = 0
    regs["f"] = 0
    regs["i"] = 0
    regs["p"] = pid
    regs["ip"] = 0
    regs["snd"] = 0  # number of values sent
    return regs

def day18(fname):
    data = read_data(fname)
    regs0 = create_program(0)
    regs1 = create_program(1)
    queue0 = []  # send queue of program 0
    queue1 = []  # send queue of program 1
    nr0 = 0
    nr1 = 1
    while (nr0 > 0) or (nr1 > 0):
        nr0 = run_program(data, 0, regs0, queue0, queue1)
        nr1 = run_program(data, 1, regs1, queue1, queue0)
    # stop when both programs cannot execute anymore
    print("Program 0 has sent " + str(regs0["snd"]) + " values.")
    print("Program 1 has sent " + str(regs1["snd"]) + " values.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18 input.txt") 
    else:
    	day18(sys.argv[1])

