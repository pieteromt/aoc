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

def calc_nearest(r, c, data):
    dist = []
    for t in data:
        ri, ci = t
        di = abs(ri-r) + abs(ci-c)
        dist.append(di)
    min_dist = min(dist)
    cnt_min = dist.count(min_dist)
    if cnt_min == 1:
        return data[dist.index(min_dist)]
    else:
        return None

def fill_grid(nr, nc, grid, data):
    for r in range(nr):
        for c in range(nc):
            grid[r][c] = calc_nearest(r, c, data)

def count_grid(nr, nc, grid):
    area = {}
    for r in range(nr):
        for c in range(nc):
            t = grid[r][c]
            if t in area:
                area[t] += 1
            else:
                area[t] = 1
    return area

def find_infinity(nr, nc, data):
    infinity = []
    delta = 10
    r0 = -delta
    r1 = nr + delta
    c0 = -delta
    c1 = nc + delta
    # ----
    for r in range(r0,r1):
        t = calc_nearest(r, c0, data)
        if not t in infinity:
            infinity.append(t)
    # ----
    for r in range(r0,r1):
        t = calc_nearest(r, c1, data)
        if not t in infinity:
            infinity.append(t)
    # ----
    for c in range(c0,c1):
        t = calc_nearest(r0, c, data)
        if not t in infinity:
            infinity.append(t)
    # ----
    for c in range(c0,c1):
        t = calc_nearest(r1, c, data)
        if not t in infinity:
            infinity.append(t)
    # ----
    return infinity

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
    print("Infinity: ", end='')
    inf = find_infinity(nr, nc, data)
    print(inf)
    area = count_grid(nr,nc,grid)
    #for t in area:
    #    print(str(t) + " " + str(area[t]))
    #print("")
    max_area = 0
    for t in area:
        if not t in inf:
            a = area[t] 
            print(str(t) + " " + str(a))
            if a > max_area:
                max_area = a
    print("Max area = " + str(max_area))

def day6(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day6 input.txt") 
    else:
    	day6(sys.argv[1])
