import sys

def read_chars(fname):
    chars = []
    f = open(fname,"r")
    while True:
        c = f.read(1)
        if not c:
            break
        chars.append(c)
    f.close()
    return chars

# states
# 0 : search for "mul("
# 1 : search for first digit of first number "1"
# 2 : search for rest of digits "23"
# 3 : search for first digit of second number "1"
# 4 : search for rest of digits of second number "23"
# 5 : match!
def process(ch):
    nr = len(ch)
    print("nr = " + str(nr))
    state = 0
    match = False
    sum = 0
    for i in range(0,nr):
        if state == 0:
            match = (ch[i] == "m") and (ch[i+1] == "u") and (ch[i+2] == "l") and (ch[i+3] == "(")
            if match:
                state = 1
                #print("found match at index " + str(i))

        elif state == 1:
            match = ch[i].isdigit()
            if match:
                nr0 = int(ch[i])
                state = 2

        elif state == 2:
            if ch[i].isdigit():
                nr0 = 10*nr0 + int(ch[i])
            elif ch[i] == ",":
                state = 3
            else:
                state = 0 # illegal statement
             
        elif state == 3:
            match = ch[i].isdigit()
            if match:
                nr1 = int(ch[i])
                state = 4

        elif state == 4:
            if ch[i].isdigit():
                nr1 = 10*nr1 + int(ch[i])
            elif ch[i] == ")":
                print("found: mul("+str(nr0)+","+str(nr1)+")")
                sum = sum + nr0*nr1
                state = 0
            else:
                state = 0 # illegal statement
        else:
            pass
    print("sum = " + str(sum))


def day3(fname):
    chars = read_chars(fname)
    #print(chars)
    process(chars)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

