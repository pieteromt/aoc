import sys

def read_data(fname):
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data = line.split(',')
    f.close()
    return data
    
# s1:  "abcde" --> "eabcd"
def spin(progs, move):
    cnt = int(move[1:])
    back = progs[-cnt:]
    front = progs[:-cnt]
    return back + front

def swap(progs,sw):
    sw.sort()
    s0 = sw[0]
    s1 = sw[1]
    tmp0 = progs[s0]
    tmp1 = progs[s1]
    return progs[:s0] + tmp1 + progs[s0+1:s1] + tmp0 + progs[s1+1:]

def exchange(progs, move):
    return swap(progs,list(map(int,move[1:].split('/'))))

def partner(progs, move):
    mv = move[1:].split('/')
    i0 = progs.find(mv[0])
    i1 = progs.find(mv[1])
    return swap(progs,[i0,i1])

def dance(progs, move):
    if move.startswith('s'):
        progs = spin(progs, move)
    elif move.startswith('x'):
        progs = exchange(progs, move)
    else: # partner
        progs = partner(progs, move)
    return progs

def process(data):
    progs = "abcdefghijklmnop"  # real input
    #progs = "abcde"            # test input
    for move in data:
        progs = dance(progs, move)
    print(progs)

def day16(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day16 input.txt") 
    else:
    	day16(sys.argv[1])

