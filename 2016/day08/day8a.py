import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 2:
            wh = list(map(int,w[1].split('x')))
            data.append(["rect"] + wh)
        elif len(w) == 5:
            xy = w[2].split('=')
            data.append(["rotate",xy[0],int(xy[1]),int(w[4])])
        else:
            print("Error: " + str(len(w)))
            exit()
    f.close()
    return data
    
def init_grid(w,h):
    return ["." * w] * h

# x = col, y = row
def set_ch(grid,x,y,val):
    row = grid[y]
    grid[y] = row[:x] + val + row[x+1:]

def show_grid(grid):
    for row in grid:
        print(row)
    print("")

def do_rect(grid,w,h):
    for y in range(h):            # row
        for x in range(w):        # column
            set_ch(grid,x,y,'#')

def do_rotate_x(grid, h, x, cnt):
    for i in range(cnt):          # grid[y+1][x] = grid[y][x]
        ch0 = grid[h-1][x]
        for y in range(h-1,0,-1):
            ch = grid[y-1][x]
            set_ch(grid,x,y,ch)
        set_ch(grid,x,0,ch0)

def do_rotate_y(grid, w, y, cnt):
    for i in range(cnt):          # grid[y][x+1] = grid[y][x]
        ch0 = grid[y][w-1]
        for x in range(w-1,0,-1):
            ch = grid[y][x-1]
            set_ch(grid,x,y,ch)
        set_ch(grid,0,y,ch0)

def execute(grid,w,h,instr):
    if instr[0] == "rect":
        do_rect(grid,instr[1],instr[2])
    else:
        if instr[1] == "x":
            do_rotate_x(grid, h, instr[2], instr[3])
        else:
            do_rotate_y(grid, w, instr[2], instr[3])

def count(grid,w,h):
    sum = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                sum += 1
    print("Pixels lit = " + str(sum))

def process(w,h,data):
    grid = init_grid(w,h)
    show_grid(grid)
    for instr in data:
        execute(grid,w,h,instr)
        show_grid(grid)
    count(grid,w,h)

def day8(fname):
    data = read_data(fname)
    #process(7,3,data)   # test data
    process(50,6,data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day8 input.txt") 
    else:
    	day8(sys.argv[1])

