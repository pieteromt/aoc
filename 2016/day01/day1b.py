import sys

# Walking directions:
# 0 = North
# 1 = East
# 2 = South
# 3 = West

# input looks like: R3, L5, R2, L2, R1, ...
def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        for d in line.split():
            turn = d[0]
            dist = int(d[1:].replace(",",""))  # strip comma
            data.append((turn,dist))
    f.close()
    return data
    
# returns the new walking direction after taking a turn
def take_turn(dir, turn):
    if turn == "R":
        return (dir + 1)%4 # turn right
    else:
        return (dir - 1 + 4)%4 # turn left

def show_result(pos):
    r,c = pos
    blocks = abs(r) + abs(c)
    print("Position: " + str(pos) + " is " + str(blocks) + " blocks away.")
    exit()

# do a single step, and mark the visited location
def step(visited, pos, dir):
    r,c = pos
    if dir == 0:   # going North
        r -= 1
    elif dir == 1: # going East
        c += 1
    elif dir == 2: # going South
        r += 1
    else:          # going West
        c -= 1
    pos = (r,c)
    if pos in visited:
        print("Already visited: " + str(pos))
        show_result(pos)
    else:
        visited[pos] = 1
    return pos

# returns the new position after walking a number of steps
def walk(visited, pos, dir, dist):
    for i in range(dist):
        pos = step(visited, pos, dir)
    return pos

def process(data):
    visited = {}
    pos = (0,0)
    dir = 0
    visited[pos] = 1
    for d in data:
        turn, dist = d
        dir = take_turn(dir, turn)
        pos = walk(visited, pos, dir, dist)

def day1(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

