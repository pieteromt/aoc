import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
def set_pix(grid, r, c, val):
    row = grid[r]
    grid[r] = row[:c] + val + row[c+1:]

def extend_grid(data,fact):
    rows = len(data)
    cols = len(data[0])
    grid = []
    for r in range(fact*rows):
        grid.append("." * (fact*cols))
    r0 = ((fact-1)*rows+1)//2
    c0 = ((fact-1)*cols+1)//2
    for r in range(rows):
        for c in range(cols):
            set_pix(grid, r0+r, c0+c, data[r][c])
    return grid

def show_grid(grid):
    for row in grid:
        print(row)
    print("")

def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    return (rows//2,cols//2)
    
# t = (r,c,d,n)
# direction
# 0 = up
# 1 = right
# 2 = down
# 3 = left
def do_burst(grid, t):
    r,c,d,n = t
    infected = (grid[r][c] != '.')
    if infected:
        d = (d+1)%4  # turn right
        set_pix(grid, r, c, '.')
    else:
        d = (d+3)%4  # turn left
        set_pix(grid, r, c, '#')
        n += 1
    if d == 0:
        r -= 1
    elif d == 1:
        c += 1
    elif d == 2:
        r += 1
    else:
        c -= 1
    return (r,c,d,n)
    
def process(data,nr):
    #show_grid(data)
    grid = extend_grid(data,1000)
    r,c = get_start(grid)
    #set_pix(grid, r, c, 'X')
    #show_grid(grid)
    t = (r,c,0,0)
    for i in range(nr):
        t = do_burst(grid,t)
        #show_grid(grid)
    r,c,d,n = t
    #show_grid(grid)
    print("Bursts = " + str(nr) + ", infections = " + str(n))

def day22(fname):
    data = read_data(fname)
    process(data,10000)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day22 input.txt") 
    else:
    	day22(sys.argv[1])

