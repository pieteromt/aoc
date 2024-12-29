import sys

# actions:
# 0: turn off
# 1: turn on
# 2: toggle

size = 1000

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if line.startswith("turn off"):
            a = 0
            off = 2
        elif line.startswith("turn on"):
            a = 1
            off = 2
        elif line.startswith("toggle"):
            a = 2
            off = 1
        else:
            print("error: " + line)
            exit()
        t1 = tuple(map(int,w[off].split(",")))
        t2 = tuple(map(int,w[off+2].split(",")))
        data.append((a,t1,t2))
    f.close()
    return data

def init_grid():
    return [ [0]*size for i in range(size)]  # all lights start 'off' (0)

def count_grid(grid):
    count = 0
    for r in range(size):
        for c in range(size):
            count += grid[r][c]
    return count

def do_instr(grid, instr):
    a, t1, t2 = instr
    for r in range(t1[0],t2[0]+1):
        for c in range(t1[1],t2[1]+1):
            if a == 0:
                grid[r][c] = 0
            elif a == 1:
                grid[r][c] = 1
            else:  # toggle
                grid[r][c] = 1 - grid[r][c]

def process(data):
    grid = init_grid()
    for instr in data:
        do_instr(grid, instr)
    print("count = " + str(count_grid(grid)))

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])

