import sys

# input format: 
# #1 @ 1,3: 4x4
def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        coor = w[2].replace(":","").split(",")
        size = w[3].split("x")
        c = int(coor[0])
        r = int(coor[1])
        w = int(size[0])
        h = int(size[1])
        data.append((r,c,h,w))
    f.close()
    return data
    
def max_coor(data):
    max_r = 0
    max_c = 0
    for t in data:
        r,c,h,w = t
        r += h
        c += w
        if r > max_r:
            max_r = r
        if c > max_c:
            max_c = c
    return (max_r,max_c)

def add_claim(grid, t):
    r,c,h,w = t
    for i in range(h):
        for j in range(w):
            grid[r+i][c+j] += 1

def count_multiple(grid):
    cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 1:
                cnt += 1
    return cnt

def show_grid(grid):
    for row in grid:
        print(row)
    print("")

def process(data):
    #for d in data:
    #    print(d)
    #print("Max coor: " + str(max_coor(data)))
    size = 1000
    grid = [[0]*size for i in range(size)]
    #show_grid(grid)
    for t in data:
        add_claim(grid, t)
        #show_grid(grid)
    cnt = count_multiple(grid)
    print("Multiple: " + str(cnt))

def day3(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3 input.txt") 
    else:
    	day3(sys.argv[1])

