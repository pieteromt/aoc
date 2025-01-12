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

def move_position(s, x, y):
    s1 = s[:x]
    ch = s[x]
    s2 = s[x+1:]
    s3 = s1 + s2 #  ch removed
    return s3[:y] + ch + s3[y:]

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

# "ecabd" d == 4
def rotate_position(s, x):
    idx = s.find(x)
    rot_right = 1 + idx
    if idx >= 4:
        rot_right += 1
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

def process(data):
    s = "abcdefgh"
    for d in data:
        s = execute(s,d)
    print("s: " + s)

def day21(fname):
    data = read_data(fname)
    process(data)
    #test()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day21 input.txt") 
    else:
    	day21(sys.argv[1])

