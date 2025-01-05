import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
# returns the (r,c) coordinates of a key
def get_pos(key):
    if key in "123":
        r = 0
    elif key in "456":
        r = 1
    else:
        r = 2
    if key in "147":
        c = 0
    elif key in "258":
        c = 1
    else:
        c = 2
    return (r,c)

# coor is an (r,c) coordinates tuple
def get_key(coor):
    keypad = [["1","2","3"],["4","5","6"],["7","8","9"]]
    r,c = coor
    return keypad[r][c]

def new_pos(pos,move):
    r,c = pos
    if move == "U":
        r -= 1
    elif move == "L":
        c -= 1
    elif move == "D":
        r += 1
    else:
        c += 1
    return (r,c)

def is_valid_pos(pos):
    r,c = pos
    return ((r >= 0) and (r < 3) and (c >= 0) and (c < 3))

# returns the new pos after making the move (optional)
def make_move(key, move):
    pos = get_pos(key)
    pos2 = new_pos(pos,move)
    if is_valid_pos(pos2):  # ignore invalid moves
        pos = pos2
    return get_key(pos)

def calc_key(key, moves):
    for move in moves:
        key = make_move(key,move)
    return key

def process(data):
    key = "5"
    print("Bathroom code is ", end='')
    for moves in data:
        key = calc_key(key, moves)
        print(key,end='')
    print("")

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])

