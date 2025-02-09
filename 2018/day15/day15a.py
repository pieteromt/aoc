import sys

def read_data(fname):
    maze = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        maze.append(line)
    f.close()
    return maze
    
class Unit:
    def __init__(self,ch,r,c,hp,pwr):
        self.ch  = ch  # 'G' or 'E'
        self.r   = r
        self.c   = c
        self.hp  = hp
        self.pwr = pwr
        self.idx = -1

    def __str__(self):
        return self.ch + "(" + str(self.hp) + ")"

    def coor(self):
        return "("+str(self.r)+","+str(self.c)+")"

    def info(self):
        return self.ch + "("+str(self.r)+","+str(self.c)+")"

# 'find_minimum' copied from AoC 2016 day24
def next_pos(cur):
    r,c = cur
    yield (r-1,c)
    yield (r,c-1)
    yield (r,c+1)
    yield (r+1,c)

def visit_maze(cache, maze, cur, goal, steps):
    if cur in cache:              # been here before?
        if cache[cur] <= steps:   # no faster route search needed
            return
    cache[cur] = steps            # fastest route found sofar
    for pos in next_pos(cur):     # visit neighbours
        r,c = pos
        if maze[r][c] == ".":
            visit_maze(cache, maze, pos, goal, steps+1)

# returns the minimum distance between start and goal
def find_minimum(maze, start, goal):
    cache = {}        # visited locations (minimum number of steps needed)
    visit_maze(cache, maze, start, goal, 0)
    if goal in cache:
        return cache[goal]
    else:
        return -1  # goal not reachable

def reading_order(unit):
    return (1000*unit.r) + unit.c

def ro_pos(pos):
    r,c = pos
    return (1000*r) + c

def show(maze, units):
    for r in range(len(maze)):
        row = maze[r]
        print(row + "   ",end='')
        first = True
        for unit in units:
            if unit.hp <= 0:  # skip dead
                continue
            if unit.r == r:
                if not first:
                    print(", ", end='')
                print(unit, end='')
                first = False
        print("")

def init_units(maze):  # reading all units (in reading order)
    units = []
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            ch = maze[r][c]
            if (ch == 'G') or (ch == 'E'):
                units.append(Unit(ch,r,c,200,3))
    return units

def index_units(units):
    for i in range(len(units)):
        units[i].idx = i
        
def enemy(ch):
    if (ch == 'E'):
        return 'G'
    else:
        return 'E'

def get_targets(units,ch):
    targets = []
    for unit in units:
        if unit.hp <= 0: # skip dead
            continue
        if unit.ch == ch:
            targets.append(unit)
    return targets

def in_range(u1,u2): # returns True if adjacent
    return abs(u1.r - u2.r) + abs(u1.c - u2.c) == 1

def get_targets_in_range(targets, unit):
    tgts = []
    for tgt in targets:
        if in_range(tgt, unit):
            tgts.append(tgt)
    return tgts

# select the target with the fewest hitpoints
def select_target(tgts):
    min_hp  = 99999
    for i in range(len(tgts)):
        tgt = tgts[i]
        if tgt.hp < min_hp:
            min_hp  = tgt.hp
            min_tgt = i
    return tgts[min_tgt]

def set_rc(maze,r,c,val):
    row = maze[r]
    maze[r] = row[:c] + val + row[c+1:]

def get_open_squares(maze, targets):
    squares = []
    for tgt in targets:
        for pos in next_pos((tgt.r,tgt.c)):
            r,c = pos
            if maze[r][c] == ".":
                if not pos in squares:
                    squares.append(pos)
    squares.sort(key=ro_pos)
    return squares

def find_next_move(maze, start, goal):
    cache = {}
    visit_maze(cache, maze, goal, start, 0)
    min_dist = 99999
    move_pos = None
    for pos in next_pos(start):
        if pos in cache: 
            dist = cache[pos]
            if dist < min_dist:
                min_dist = dist
                move_pos = pos
    return move_pos

# returns True if an attack was done
def attack(maze, units, targets, unit):
    tgts = get_targets_in_range(targets, unit)
    if len(tgts) > 0:
        tgt = select_target(tgts)
        #print("attack: " + unit.info() + " attacks " + tgt.info())
        # now attack the target
        tgt.hp -= unit.pwr
        if tgt.hp <= 0:
            print("Target '" + tgt.ch + "' at " + tgt.coor() + " died! idx: " + str(tgt.idx))
            set_rc(maze,tgt.r,tgt.c,".")
            #del units[tgt.idx]
        return True
    return False

# returns True when combat is over
def do_unit(maze, units, unit):
    index_units(units)
    #print("do_unit '" + unit.ch + "' " + unit.coor() + " at idx: " + str(unit.idx))

    # identify all possible targets
    targets = get_targets(units,enemy(unit.ch))
    if len(targets) == 0:  # combat ends
        print("No more targets, combat ends")
        return True

    # determine if any targets are in range to attack:
    if attack(maze, units, targets, unit):
        return False

    # no targets in range, move
    squares = get_open_squares(maze, targets)
    min_dist = 99999
    min_goal = None
    start = (unit.r,unit.c)
    for goal in squares:
        dist = find_minimum(maze, start, goal)
        if dist != -1:  # reachable
            if dist < min_dist:
                min_dist = dist
                min_goal = goal
    if min_goal != None:
        #print("Move goal is: " + str(min_goal))
        mov_pos = find_next_move(maze, start, min_goal)
        #print("Moving to " + str(mov_pos))
        set_rc(maze,unit.r,unit.c,".")
        unit.r, unit.c = mov_pos
        set_rc(maze,unit.r,unit.c,unit.ch)
        attack(maze, units, targets, unit)
    #else:
    #    print("Cannot reach any of the open squares")
    return False

def do_round(maze, units):
    units.sort(key=reading_order)
    for unit in units:
        if unit.hp <= 0: # skip dead
            continue
        done = do_unit(maze, units, unit)
        if done:
            break
    return done

def remaining_sum(units):
    sum = 0
    for unit in units:
        if unit.hp <= 0:  # skip dead
            continue
        sum += unit.hp
    return sum

def process(maze):
    units = init_units(maze)
    print("Initially:")
    show(maze, units)
    done = False
    n = 0
    while not done:
        done = do_round(maze, units)
        if done:
            break
        n += 1
        print("")
        print("After " + str(n) + " rounds:")
        show(maze, units)
    sum = remaining_sum(units)
    outcome = n*sum
    print("Finished after " + str(n) + " rounds, sum = " + str(sum) + ", outcome = " + str(outcome))

def day15(fname):
    maze = read_data(fname)
    process(maze)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])
