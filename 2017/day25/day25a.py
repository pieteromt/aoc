import sys

class State:
    def __init__(self, name):
        self.name = name
        self.wmc = [[None,None,None],[None,None,None]]

    def __str__(self):
        s = self.name + " : "
        s += str(self.wmc[0])
        s += "  "
        s += str(self.wmc[1])
        return s

def read_data(fname):
    begin = ""
    steps = 0
    name = ""
    cur = None
    cv = 0
    states = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line.startswith("Begin"):
            w = line.split()
            begin = w[3].replace(".","")
        elif line.startswith("Perform"):
            w = line.split()
            steps = int(w[5])
        elif len(line) == 0:
            if cur != None:
                states[name] = cur
                cur = None
        elif line.startswith("In state"):
            w = line.split()
            name = w[2].replace(":","")
            cur = State(name)
        elif line.startswith("If the current value"):
            w = line.split()
            cv = int(w[5].replace(":",""))
        elif line.startswith("- Write"):
            w = line.split()
            val = int(w[4].replace(".",""))
            cur.wmc[cv][0] = val
        elif line.startswith("- Move"):
            w = line.split()
            move = w[6].replace(".","")
            cur.wmc[cv][1] = move
        elif line.startswith("- Continue"):
            w = line.split()
            cont = w[4].replace(".","")
            cur.wmc[cv][2] = cont
        else:
            print("error: " + line)
            exit()
    f.close()
    if cur != None:
        states[name] = cur
    return begin, steps, states
    
def show_turing(turing, width):
    start = len(turing)//2
    for i in range(start-width,start+width+1):
        print(str(turing[i]) + " ", end='')
    print("")

def calc_checksum(turing):
    cnt = 0
    for i in range(len(turing)):
        if turing[i] == 1:
            cnt += 1
    print("Checksum: " + str(cnt))

def process(begin, steps, states):
    turing = [0] * (2*steps + 1)
    pos = steps
    cur = begin
    #show_turing(turing,6)
    for i in range(steps):
        state = states[cur]
        val = turing[pos]
        wmc = state.wmc[val]
        #print("cur: " + cur + ", pos: " + str(pos) + ", val: " + str(val) + ", wmc = " + str(wmc))
        turing[pos] = wmc[0]
        if wmc[1] == "left":
            pos -= 1
        else:
            pos += 1
        cur = wmc[2]
        #show_turing(turing,6)
    calc_checksum(turing)

def day25(fname):
    begin, steps, states = read_data(fname)
    #print("Begin: " + begin)
    #print("Steps: " + str(steps))
    #for state in states:
    #    print(states[state])
    process(begin, steps, states)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day25 input.txt") 
    else:
    	day25(sys.argv[1])
