import sys

sys.setrecursionlimit(6000)

def add_clay(data, line):
    w = line.split()
    w[0] = w[0].replace(",","")
    c1 = w[0].split("=")
    xy = c1[0]  # "x" or "y"
    v1 = int(c1[1])
    c2 = w[1].split("=")
    r = c2[1].split("..")
    r0 = int(r[0])
    r1 = int(r[1])
    if xy == "x":
        for y in range(r0,r1+1):
            data.append((v1,y))
    else:
        for x in range(r0,r1+1):
            data.append((x,v1))

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        add_clay(data, line)
    f.close()
    return data
    
def max_xy(data):
    min_x = 99999
    max_x = -99999
    min_y = 99999
    max_y = -99999
    for t in data:
        x, y = t
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    return min_x, max_x, min_y, max_y

def show_grid(grid):
    for y in range(len(grid)):
        row = grid[y]
        print("{:5d}".format(y) + "  " + row)
    print("")

def show_dim(dim):
    min_x, max_x, min_y, max_y = dim
    print("min_x: " + str(min_x) + ", max_x: " + str(max_x) + \
          ", min_y: " + str(min_y) + ", max_y: " + str(max_y))

def init_grid(dim):
    min_x, max_x, min_y, max_y = dim
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = ["." * width for i in range(height)]
    return grid

def set_xy(grid, dim, x, y, val):
    min_x, max_x, min_y, max_y = dim
    x -= min_x
    row = grid[y]
    grid[y] = row[:x] + val + row[x+1:]

def get_xy(grid, dim, x, y):
    min_x, max_x, min_y, max_y = dim
    x -= min_x
    return grid[y][x]

# returns True if a wall is reached
def flood_left_right(grid, dim, x, y, sym, left):
    wall = False
    min_x, max_x, min_y, max_y = dim
    if left:
        x -= 1
    else:
        x += 1
    val = get_xy(grid, dim, x, y)
    val2 = get_xy(grid, dim, x, y+1)
    if (val2 == "#") or (val2 == "~"):  # we can still flood to the right
        if (val == ".") or (val == "|"):
            set_xy(grid, dim, x, y, sym)
            wall = flood_left_right(grid, dim, x, y, sym, left)
        elif val == "#":
            wall = True
    elif (val2 == ".") or (val2 == "|"):
        set_xy(grid, dim, x, y, sym)
        flood_down(grid, dim, x, y)
    return wall

# returns True if both left and right have walls; in that case, '~' is used
def flood_horz(grid, dim, x, y):
    set_xy(grid, dim, x, y, "|")
    fill_l = flood_left_right(grid, dim, x, y, "|", True)
    fill_r = flood_left_right(grid, dim, x, y, "|", False)
    if fill_l and fill_r:  # fill bucket
        flood_left_right(grid, dim, x, y, "~", True)
        flood_left_right(grid, dim, x, y, "~", False)
        return True
    return False

def flood_down(grid, dim, x, y):
    min_x, max_x, min_y, max_y = dim
    if y < max_y:
        y1 = y + 1
        val = get_xy(grid, dim, x, y1)
        if val == ".":
            set_xy(grid, dim, x, y1, "|")
            flood_down(grid, dim, x, y1)
        elif (val == "#") or (val == "~"):
            while flood_horz(grid, dim, x, y):  # fill bucket
                set_xy(grid, dim, x, y, "~")
                y -= 1
    else:
        pass # bottom of grid reached, we're done
    
def count(grid, min_y):
    cnt1 = 0
    cnt2 = 0
    for y in range(len(grid)):
        if y < min_y:   # skip top lines in count!
            continue
        row = grid[y]
        for ch in row:
            if ch == "~":
                cnt1 += 1
            if ch == "|":
                cnt2 += 1
    print("Water tiles = " + str(cnt1+cnt2))
    print("After drain = " + str(cnt1))

def process(data):
    min_x, max_x, min_y, max_y = max_xy(data)
    keep_min_y = min_y 
    if min_y > 0:
        min_y = 0
    min_x -= 1
    max_x += 1
    dim = (min_x, max_x, min_y, max_y)
    grid = init_grid(dim)
    for t in data:
        x,y = t
        set_xy(grid, dim, x, y, "#")
    set_xy(grid, dim, 500, 0, "+")   # source
    show_grid(grid)
    flood_down(grid, dim, 500, 0)
    show_grid(grid)
    count(grid, keep_min_y)

def day17(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])
