import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        c = int(w[0].replace(",",""))
        r = int(w[1])
        data.append((r,c))
    f.close()
    return data
    
def max_row_col(data):
    max_row = 0
    max_col = 0
    for t in data:
        r,c = t
        if r > max_row:
            max_row = r
        if c > max_col:
            max_col = c
    return max_row,max_col

def calc_total(r, c, data):
    dist = 0
    for t in data:
        ri, ci = t
        dist += abs(ri-r) + abs(ci-c)
    return dist

def fill_grid(nr, nc, grid, data):
    for r in range(nr):
        for c in range(nc):
            grid[r][c] = calc_total(r, c, data)

def count_grid(nr, nc, grid, limit):
    area = 0
    for r in range(nr):
        for c in range(nc):
            dist = grid[r][c]
            if dist < limit:
                area += 1
    return area

def process(data):
    max_row, max_col = max_row_col(data)
    nr = max_row+1
    nc = max_col+1
    grid = [[None]*nc for i in range(nr)]
    print("Max row = " + str(max_row) + ", max col = " + str(max_col))
    fill_grid(nr, nc, grid, data)
    #for row in grid:
    #    print(row)
    #print("")
    area = count_grid(nr,nc,grid,10000)   # real: 10000, test: 32
    print("Area = " + str(area))

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])
