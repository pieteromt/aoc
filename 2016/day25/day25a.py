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

output = ""

def do_out(arg0, regs):
    global output
    output += str(regs[arg0]) + " "
    #print(str(regs[arg0]) + " ", end='')
    regs["ip"] += 1
    regs["nr"] += 1
    if regs["nr"]%50 == 0:
        #print("")
        regs["ip"] = -1  # break

def do_jnz(arg0, arg1, regs):
    if get_val(arg0, regs) != 0:
        regs["ip"] += get_val(arg1, regs)
    else:
        regs["ip"] += 1

def do_tgl(data, arg0, regs):
    new_ip = regs["ip"] + regs[arg0]
    if (new_ip >= 0) and (new_ip < len(data)):
        instr = data[new_ip]
        if instr[0] == "inc":
            instr= ("dec", instr[1])
        elif (instr[0] == "dec") or (instr[0] == "tgl"):
            instr= ("inc", instr[1])
        elif (instr[0] == "jnz"):
            instr= ("cpy", instr[1], instr[2])
        elif (instr[0] == "cpy"):
            instr= ("jnz", instr[1], instr[2])
        else:
            print("Error: " + str(instr))
            exit()
        data[new_ip] = instr
    regs["ip"] += 1

def execute(data, instr, regs):
    if instr[0] == "cpy":
        do_cpy(instr[1], instr[2], regs)
    elif instr[0] == "inc":
        do_inc(instr[1], regs)
    elif instr[0] == "dec":
        do_dec(instr[1], regs)
    elif instr[0] == "jnz":
        do_jnz(instr[1], instr[2], regs)
    elif instr[0] == "tgl":
        do_tgl(data, instr[1], regs)
    elif instr[0] == "out":
        do_out(instr[1], regs)
    else:
        print("Error: " + str(instr))
        exit()

def process(data,regs):
    ip = regs["ip"]
    while ((ip >= 0) and (ip < len(data))):
        execute(data, data[ip], regs)
        ip = regs["ip"]
    #print("a = " + str(regs["a"]))

def try_value(data, val):
    global output
    output = ""
    regs = {}
    regs["a"] = val
    regs["b"] = 0
    regs["c"] = 0
    regs["d"] = 0
    regs["ip"] = 0
    regs["nr"] = 0   # number of out done
    process(data,regs)

def find_a(data):
    a = 0
    while True:
        try_value(data, a)
        if a%10 == 0:
            print(str(a) + " " + output)
        if output.startswith("0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1"):
            break
        a += 1
    print("a = " + str(a))

def day25(fname):
    data = read_data(fname)
    find_a(data)
    #try_value(data, 180)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day25 input.txt") 
    else:
    	day25(sys.argv[1])

