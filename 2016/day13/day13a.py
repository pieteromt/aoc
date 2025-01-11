import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def calc(x,y,num):
    z = x*x + 3*x + 2*x*y + y + y*y
    z += num
    if z.bit_count()%2 == 0:
        return "."
    else:
        return "#"

def create_maze(num,w,h):
    maze = []
    for y in range(h):            # y is row
        row = ""
        for x in range(w):        # x is col
            row += calc(x,y,num)
        maze.append(row)
    return maze

def show_maze(maze):
    for row in maze:
        print(row)
    print("")

def next_pos(cur,w,h):
    x,y = cur
    if x > 0:
        yield (x-1,y)
    if x < w-1:
        yield (x+1,y)
    if y > 0:
        yield (x,y-1)
    if y < h-1:
        yield (x,y+1)

def visit_maze(cache, maze, w,h, cur, goal, steps):
    if cur in cache:              # been here before?
        if cache[cur] <= steps:   # no faster route search needed
            return

    cache[cur] = steps            # fastest route found sofar

    for pos in next_pos(cur,w,h): # visit neighbours
        x,y = pos
        if maze[y][x] == ".":
            visit_maze(cache, maze, w,h, pos, goal, steps+1)

def count(cache):
    sum = 0
    for t in cache:
        if cache[t] <= 50:
            sum += 1
    print("count: " + str(sum))
            
def process(data):
    cache = {}        # visited locations (minimum number of steps needed)
    start = (1,1)     # starting position
    #goal = (7,4)     # end position (test input)
    goal = (31,39)    # end position (real input)
    w,h = 60,60
    maze = create_maze(data[0],w,h)
    #show_maze(maze)
    visit_maze(cache,maze,w,h,start,goal,0)
    print("minimum: " + str(cache[goal]))
    count(cache)

def day13(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])

