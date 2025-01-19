import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line.startswith("/dev/grid"):
            w = line.split()
            dev = w[0].split('-')
            x = int(dev[1][1:])
            y = int(dev[2][1:])
            size = int(w[1][:-1])
            used = int(w[2][:-1])
            avail = int(w[3][:-1])
            use = int(w[4][:-1])
            data.append((x,y,size,used,avail,use))
    f.close()
    return data
    
def get_max_xy(data):
    max_x = -1
    max_y = -1
    for d in data:
        x, y, size, used, avail, use = d
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return (max_x, max_y)

def range_conn(w,h,x,y):
    if x > 0:
        yield y,x-1
    if x < w-1:
        yield y,x+1
    if y > 0:
        yield y-1,x
    if y < h-1:
        yield y+1,x

def is_viable(grid, y0, x0, y1, x1):
    size0, used0, avail0 = grid[y0][x0]
    size1, used1, avail1 = grid[y1][x1]
    return (used0 != 0) and (used0 <= avail1)

def get_viable_conns(grid):
    w = len(grid[0])
    h = len(grid)
    vcs = []
    for y in range(h):
        for x in range(w):
            for y1,x1 in range_conn(w,h,x,y):
                if is_viable(grid, y, x, y1, x1):
                    t0 = (x,y)
                    t1 = (x1,y1)
                    #print(str(t0) + " -> " + str(t1))
                    vcs.append((t0,t1))
    return vcs

# note: grid[y][x]  y are rows, x are columns
def make_grid(data):
    max_x, max_y = get_max_xy(data)
    #print("max_x = " + str(max_x) + ", max_y = " + str(max_y))
    # (size,used,avail)
    grid = [[(0,0,0)] * (max_x+1) for i in range(max_y+1)]
    for d in data:
        x, y, size, used, avail, use = d
        grid[y][x] = (size, used, avail)
    return grid

# use a wide monitor :-)
def show_grid(grid):
    w = len(grid[0])
    h = len(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            size, used, avail = grid[y][x]
            print("{:3d}".format(used) + "/" + "{:3d}".format(size) + " ", end="")
        print("")
    print("")

def process(data):
    grid = make_grid(data)
    vcs = get_viable_conns(grid)
    for vc in vcs:
        t0, t1 = vc
        x0,y0 = t0
        x1,y1 = t1
        size0, used0, avail0 = grid[y0][x0]
        size1, used1, avail1 = grid[y1][x1]
        print("t0 = " + str(t0) + " used = " + str(used0) + " size = " + str(size0) + " t1 = " + str(t1) + " used = " + str(used1) + " size = " + str(size1))
    show_grid(grid)
    #
    # if you print out the grid, you'll see a big "wall" on the third row (y = 2)
    # we need to walk around that wall first
    #
    # move 6 to the left
    # move 6 up
    # move 22 to the right ; the hole is now at the top right corner
    # we need 5 moves to move the payload *one* position to the left
    # we need to do this 35 times
    # so we need 35*5 = 175 moves
    # so in total we need 6 + 6 + 22 + 175 = 209 moves

def day22(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day22 input.txt") 
    else:
    	day22(sys.argv[1])

