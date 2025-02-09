import sys

# position=< 9,  1> velocity=< 0,  2>
def process_line(data, line):
    w = line.split()
    line = "".join(w)
    line = line.replace("<"," ").replace(">"," ")
    w = line.split()
    pos = w[1].split(",")  # "9,1"
    vel = w[3].split(",")  # "0,2"
    data.append((tuple(map(int,pos)),tuple(map(int,vel))))

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        process_line(data, line)
    f.close()
    return data
    
def set_xy(grid, x, y, val):
    row = grid[y]
    grid[y] = row[:x] + val + row[x+1:]

def calc_grid(data, t, min_x, max_x, min_y, max_y):
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = ["." * width for i in range(height)]
    for tt in data:
        pos, vel = tt
        x, y = pos
        vx, vy = vel
        xt = x + vx*t - min_x
        yt = y + vy*t - min_y
        set_xy(grid, xt, yt, "#")
    return grid        

def calc_area(data,t):
    min_x = 100000
    max_x = -100000
    min_y = 100000
    max_y = -100000
    for tt in data:
        pos, vel = tt
        x, y = pos
        vx, vy = vel
        xt = x + vx*t
        yt = y + vy*t
        if xt < min_x:
            min_x = xt
        if xt > max_x:
            max_x = xt
        if yt < min_y:
            min_y = yt
        if yt > max_y:
            max_y = yt
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    return width, height, min_x, max_x, min_y, max_y

def show_grid(grid):
    for row in grid:
        print(row)

def process(data):
    min_width = 100000
    min_height = 100000
    t_width = 0
    t_height = 0
    for t in range(20000):
        width, height, min_x, max_x, min_y, max_y = calc_area(data,t)
        if width < min_width:
            min_width = width
            t_width = t
        if height < min_height:
            min_height = height
            t_height = t
    #print("min_width: " + str(min_width) + " for t: " + str(t_width))
    #print("min_height: " + str(min_height) + " for t: " + str(t_height))
    t = t_width
    print("t = " + str(t))
    width, height, min_x, max_x, min_y, max_y = calc_area(data,t)
    grid = calc_grid(data, t, min_x, max_x, min_y, max_y)
    show_grid(grid)

def day10(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])
