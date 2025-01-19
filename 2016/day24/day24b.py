import sys

sys.setrecursionlimit(1500)

def read_data(fname):
    maze = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        maze.append(line)
    f.close()
    return maze
    
def next_pos(cur):
    r,c = cur
    yield (r-1,c)
    yield (r+1,c)
    yield (r,c-1)
    yield (r,c+1)

def visit_maze(cache, maze, cur, goal, steps):
    if cur in cache:              # been here before?
        if cache[cur] <= steps:   # no faster route search needed
            return
    cache[cur] = steps            # fastest route found sofar
    for pos in next_pos(cur):     # visit neighbours
        r,c = pos
        if maze[r][c] != "#":
            visit_maze(cache, maze, pos, goal, steps+1)

# returns the minimum distance between start and goal
def find_minimum(maze, start, goal):
    cache = {}        # visited locations (minimum number of steps needed)
    visit_maze(cache, maze, start, goal, 0)
    return cache[goal]

def get_dists(maze,locs,nr):
    dists = {}
    for i in range(nr):
        for j in range(i+1,nr):
            steps = find_minimum(maze, locs[i], locs[j])
            t = (i,j)
            dists[t] = steps
    return dists

def find_loc(maze, si):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == si:
                return (r,c)
    print("Error: find_loc: " + si)
    exit()

def find_locs(maze, nr):
    locs = []
    for i in range(nr):
        loc = find_loc(maze, str(i))
        locs.append(loc)
    return locs

# returns the distance in steps between location i and j
def get_dist(dists, i, j):
    return dists[(min(i,j),max(i,j))]

def calc_best_route(maze, locs, dists, path, s, steps):
    if len(s) == 0:
        delta = get_dist(dists, path[-1], 0)  # return to 0
        return steps + delta
    min_steps = 99999
    for i in s:
        s2 = s.copy()
        s2.remove(i)
        delta = get_dist(dists, path[-1], i)
        path.append(i)
        steps2 = calc_best_route(maze, locs, dists, path, s2, steps + delta)
        path.pop()
        if steps2 < min_steps:
            min_steps = steps2
    return min_steps

# we reuse code from day 13
# we need to visit locations 0 to 7
# first determine the coordinates of all locations to visit
def process(maze):
    nr = 8
    locs = find_locs(maze, nr)
    #for loc in locs:
    #    print(loc)
    dists = get_dists(maze,locs,nr)
    path = [0]
    s = set()
    for i in range(1,nr):
        s.add(i)
    #print("calculating best route...")
    steps = calc_best_route(maze, locs, dists, path, s, 0)
    print("steps = " + str(steps))

def day24(fname):
    maze = read_data(fname)
    process(maze)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day24 input.txt") 
    else:
    	day24(sys.argv[1])

