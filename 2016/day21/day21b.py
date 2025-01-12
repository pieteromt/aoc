import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 4:     # rotate
            data.append((w[0],w[1],w[2]))
        elif len(w) == 5:   # reverse 
            data.append((w[0],w[1],w[2],w[4]))
        elif len(w) == 6:   # swap, move
            data.append((w[0],w[1],w[2],w[5]))
        elif len(w) == 7:   # rotate based on position
            data.append((w[0],w[3],w[6]))
        else:
            print("error: len = " + str(len(w)) + " " + line)
            exit()
    f.close()
    return data
    
# 'move',    'position',
# 'reverse', 'positions',
# 'rotate',  'left',
# 'rotate',  'position',
# 'rotate',  'right',
# 'swap',    'letter',
# 'swap',    'position',

# move position 6 to position 3
# "abcdefgh"  --> "abcgdefh"
def move_position(s, x, y):
    s1 = s[:x]
    ch = s[x]
    s2 = s[x+1:]
    s3 = s1 + s2 #  ch removed
    return s3[:y] + ch + s3[y:]

# reverse positions 1 through 6
def reverse_position(s, p1, p2):
    s1 = ""
    for i in range(p1,p2+1):
        s1 = s[i] + s1
    return s[:p1] + s1 + s[p2+1:]

# "abcde" --> "bcdea"
def rotate_left(s, n):
    n = n%len(s)
    return s[n:] + s[:n]

# "abcde" --> "eabcd"
def rotate_right(s, n):
    n = n%len(s)
    return s[-n:] + s[:-n]

# rotate based on position of letter e
# 0 --> 1
# 1 --> 3
# 2 --> 5
# 3 --> 7
# 4 --> 2
# 5 --> 4
# 6 --> 6
# 7 --> 0
def rotate_position(s, x):
    idx = s.find(x)
    rot_right = 1 + idx
    if idx >= 4:
        rot_right += 1
    #print("idx = " + str(idx) + ", rot_right = " + str(rot_right))
    return rotate_right(s, rot_right)

# rotate based on position of letter e
# 0 --> 7   7
# 1 --> 0   7
# 2 --> 4   2
# 3 --> 1   6
# 4 --> 5   1
# 5 --> 2   5
# 6 --> 6   0
# 7 --> 3   4
def reverse_rotate_position(s, x):
    lut = [7,7,2,6,1,5,0,4]
    idx = s.find(x)
    rot_right = lut[idx]
    #print("idx = " + str(idx) + ", rot_right = " + str(rot_right))
    return rotate_right(s, rot_right)

def swap_letter(s, x, y):
    s1 = ""
    for i in range(len(s)):
        if s[i] == x:
            s1 += y
        elif s[i] == y:
            s1 += x
        else:
            s1 += s[i]
    return s1

def swap_position(s, x, y):
    p1 = min(x,y)
    p2 = max(x,y)
    t1 = s[p1]
    t2 = s[p2]
    return s[:p1] + t2 + s[p1+1:p2] + t1 + s[p2+1:]

def test():
    s = "abcde"
    s = swap_position(s,4,0)
    s = swap_letter(s,"b","d")
    s = reverse_position(s,0,4)
    s = rotate_left(s,1)
    s = move_position(s,1,4)
    s = move_position(s,3,0)
    s = rotate_position(s,"b")
    s = rotate_position(s,"d")
    print(s)

def execute(s,d):
    if d[0] == "move":
        s = move_position(s,int(d[2]),int(d[3]))
    elif d[0] == "reverse":
        s = reverse_position(s,int(d[2]),int(d[3]))
    elif d[0] == "rotate":
        if d[1] == "left":
            s = rotate_left(s,int(d[2]))
        elif d[1] == "right":
            s = rotate_right(s,int(d[2]))
        else:
            s = rotate_position(s,d[2])
    else: # "swap"
        if d[1] == "letter":
            s = swap_letter(s,d[2],d[3])
        else: # "position"
            s = swap_position(s,int(d[2]),int(d[3]))
    return s

def reverse_execute(s,d):
    if d[0] == "move":
        s = move_position(s,int(d[3]),int(d[2]))
    elif d[0] == "reverse":
        s = reverse_position(s,int(d[2]),int(d[3]))
    elif d[0] == "rotate":
        if d[1] == "left":
            s = rotate_right(s,int(d[2]))
        elif d[1] == "right":
            s = rotate_left(s,int(d[2]))
        else:
            s = reverse_rotate_position(s,d[2])
    else: # "swap"
        if d[1] == "letter":
            s = swap_letter(s,d[2],d[3])
        else: # "position"
            s = swap_position(s,int(d[2]),int(d[3]))
    return s

def test2():
    for i in range(8):
        s = "abcdefgh"
        c = s[i]
        print(s + " " + c)
        s = rotate_position(s,c)
        print(s)
        s = reverse_rotate_position(s,c)
        print(s)
        print("")

def process(data):
    s = "fbgdceah"
    for i in range(len(data)-1,-1,-1):  # reverse order
        s = reverse_execute(s,data[i])
    print("s: " + s)

def day21(fname):
    data = read_data(fname)
    process(data)
    #test()
    #test2()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day21 input.txt") 
    else:
    	day21(sys.argv[1])

