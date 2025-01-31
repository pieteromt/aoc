import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data[w[0]] = w[2]
    f.close()
    return data
    
def init_grid():
    grid = []
    grid.append(".#.")
    grid.append("..#")
    grid.append("###")
    return grid

def show_grid(grid):
    for row in grid:
        print(row)
    print("")

# rotate a 2x2 or 3x3 grid
def rotate_grid(grid):
    n = len(grid)
    gr = []
    for r in range(n):
        row = ""
        for c in range(n):
            row += grid[(n-1)-c][r]
        gr.append(row)
    return gr
    
def flip_horz_grid(grid):
    n = len(grid)
    gr = []
    for r in range(n):
        row = ""
        for c in range(n):
            row += grid[(n-1)-r][c]
        gr.append(row)
    return gr

def flip_vert_grid(grid):
    n = len(grid)
    gr = []
    for r in range(n):
        row = ""
        for c in range(n):
            row += grid[r][(n-1)-c]
        gr.append(row)
    return gr

def grid_to_pattern(grid):
    n = len(grid)
    pat = ""
    for r in range(n):
        if r>0:
            pat += "/"
        pat += grid[r]
    return pat

def pattern_to_grid(pat):
    grid = pat.split('/')
    return grid

def get_rot_pats(grid, pats):
    pat = grid_to_pattern(grid)
    if pat not in pats:
        pats.append(pat)
    for i in range(4):
        grid = rotate_grid(grid)
        pat = grid_to_pattern(grid)
        if pat not in pats:
            pats.append(pat)

def get_patterns(grid):
    pats = []
    get_rot_pats(grid, pats)
    grid = flip_horz_grid(grid)
    get_rot_pats(grid, pats)
    grid = flip_horz_grid(grid)
    grid = flip_vert_grid(grid)
    get_rot_pats(grid, pats)
    grid = flip_vert_grid(grid)
    return pats

def lookup_rule(data, pats):
    for pat in pats:
        if pat in data:
            return data[pat]
    print("error: no rule found")
    exit()

def iterate(data, grid):
    n = len(grid)
    # calculate the number of tiles (nr)
    if n%2 == 0:
        nr = n//2
        n = 2
    else:
        nr = n//3
        n = 3
    grgr = []
    for rr in range(nr):
        for cc in range(nr):
            gr = []
            for r in range(n):
                row = ""
                for c in range(n):
                    row += grid[rr*n+r][cc*n+c]
                gr.append(row)
            pats = get_patterns(gr)
            rule = lookup_rule(data, pats)
            gr = pattern_to_grid(rule)
            for r in range(n+1):
                row_nr = rr*(n+1)+r
                if len(grgr) > row_nr:
                    row = grgr[row_nr]
                else:
                    row = ""
                for c in range(n+1):
                    row += gr[r][c]
                if len(grgr) > row_nr:
                    grgr[row_nr] = row
                else:
                    grgr.append(row)
    return grgr

def count_pixels(grid):
    cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                cnt += 1
    print("Pixels: " + str(cnt))

def process(data,nr):
    grid = init_grid()
    #show_grid(grid)
    for i in range(nr):
        grid = iterate(data, grid)
        #show_grid(grid)
    count_pixels(grid)

def day21(fname):
    data = read_data(fname)
    process(data,5)
    process(data,18)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day21 input.txt") 
    else:
    	day21(sys.argv[1])

