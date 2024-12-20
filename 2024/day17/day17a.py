import sys

A = 0
B = 0
C = 0
prog = []
IP = 0

opcode = 0
operand = 0

def read_data(fname):
    global A, B, C, prog
    prog = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        words = line.split()
        nr = len(words)
        if nr == 2:
            opcodes = words[1].split(",")
            for opc in opcodes:
                prog.append(int(opc))
        elif nr == 3:  # register
            if words[1] == "A:":
                A = int(words[2])
            elif words[1] == "B:":
                B = int(words[2])
            elif words[1] == "C:":
                C = int(words[2])
            else:
                print("Invalid input: " + line)
                exit()
    f.close()


def combo(oper):
    if ((oper >= 0) and (oper <= 3)):
        return oper
    elif oper == 4:
        return A
    elif oper == 5:
        return B
    elif oper == 6:
        return C
    elif oper == 7:
        print("combo_operand: " + str(oper))
        exit()

# opcode 0: division
def adv():
    global A
    num = A
    den = 2**combo(operand)
    result = num//den
    A = result

# opcode 1: bitwise XOR
def bxl():
    global B
    result = B ^ operand
    B = result

# opcode 2:
def bst():
    global B
    result = combo(operand) % 8
    B = result

# opcode 3:
def jnz():
    global IP
    if A != 0:
        IP = operand
   
# opcode 4:
def bxc():
    global B
    result = B ^ C
    B = result

first = True

# opcode 5:
def out():
    global first
    result = combo(operand) % 8
    if first:
        first = False
    else:
        print(",", end='')
    print(result, end='')

# opcode 6:
def bdv():
    global B
    num = A
    den = 2**combo(operand)
    result = num//den
    B = result
    
# opcode 7:
def cdv():
    global C
    num = A
    den = 2**combo(operand)
    result = num//den
    C = result

def load_instr():
    global IP, opcode, operand
    if IP < len(prog):
        opcode = prog[IP]
        IP = IP + 1
        operand = prog[IP]
        IP = IP + 1
        #print("Load: opcode = " + str(opcode) + ", operand = " + str(operand))

def exec_instr():
    if opcode == 0:
        adv()
    elif opcode == 1:
        bxl()
    elif opcode == 2:
        bst()
    elif opcode == 3:
        jnz()
    elif opcode == 4:
        bxc()
    elif opcode == 5:
        out()
    elif opcode == 6:
        bdv()
    elif opcode == 7:
        cdv()
    else:
        print("Illegal opcode: " + str(opcode))
        exit()

def process():
    while IP < len(prog):
        load_instr()
        exec_instr()
    print("")

def day17(fname):
    read_data(fname)
    print("A: " + str(A))
    print("B: " + str(B))
    print("C: " + str(C))
    print(prog)
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day17(fname)
    else:
        print("Usage: python day17 input.txt")

