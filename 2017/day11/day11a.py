import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split(',')
        data.append(w)
    f.close()
    return data
    
def new_pos(cur, move):
    r, c = cur
    if move == "n":
        return (r-2,c)
    elif move == "s":
        return (r+2,c)
    elif move == "nw":
        return (r-1,c-1)
    elif move == "ne":
        return (r-1,c+1)
    elif move == "sw":
        return (r+1,c-1)
    else: # "se"
        return (r+1,c+1)

def calc_steps(cur):
    r, c = cur
    r = abs(r)
    c = abs(c)
    steps = c
    rest = r - c
    if rest > 0:
        steps += rest//2
    return steps

def make_moves(moves):
    max_steps = 0
    cur = (0,0)
    for move in moves:
        cur = new_pos(cur, move)
        steps = calc_steps(cur)
        if steps > max_steps:
            max_steps = steps
    steps = calc_steps(cur)
    print("steps = " + str(steps))
    print("max_steps = " + str(max_steps))

def process(data):
    for moves in data:
        #print(moves)
        make_moves(moves)

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

