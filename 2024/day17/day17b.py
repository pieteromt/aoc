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
cnt = 0

# opcode 5:
def out():
    global first, cnt
    result = combo(operand) % 8
    if first:
        first = False
    else:
        print(",", end='')
    print(result, end='')
    cnt = cnt + 1

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

def show_div(i):
    n = i
    s = ""
    while n != 0:
        div = n//8
        rem = n%8
        s = str(rem) + " " + s
        n = div
    print(s,end='')

def process(i):
    global IP, A, B, C, first, cnt
    first = True
    IP = 0
    A = i
    B = 0
    C = 0
    cnt = 0
    print(str(i) + " : ", end='')
    bin = "{:0b}".format(i)
    #bin3 = bin[len(bin)-6:len(bin)-3]
    print(str(i) + " " + bin + " : ", end='')
    while IP < len(prog):
        load_instr()
        exec_instr()
    print("  cnt = " + str(cnt), end='')
    print("   ",end='')
    #show_div(i)
    print("")
    return cnt > 16

def show_prog():
    f = True
    print("prog : ",end='')
    for opc in prog:
        if f:
            f = False
        else:
            print(",", end='')
        print(opc,end='')
    print(" ")

def day17(fname):
    read_data(fname)
    #print("A: " + str(A))
    #print("B: " + str(B))
    #print("C: " + str(C))
    show_prog()

    # lowest, highest
    i = 8**15
    #process(i)
    #process(8*i-1)

# 2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0

    size = 1024*64
    start = 0
    end = start + size
    #base = 0b110100111110101110000010101000101010
    #base = 0b11010000010101000101010
    #base = 0b10101000101010
    #base = 0b10101000101000
    #base = 0b1110101100000010101000101010
    base = 0b110100111110101100000010101000101010
    bits = 36
    mask = (2**bits - 1) 
    lower = i & mask
    i = i - lower
    #process(i)

    for j in range(start,end):
        for k in range(0,8):
            if process(i+ (j<<bits) + base + k):
                exit()

# grep in the output for  ": 2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0"

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day17(fname)
    else:
        print("Usage: python day17 input.txt")

