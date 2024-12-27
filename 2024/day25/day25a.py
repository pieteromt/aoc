import sys

#sys.setrecursionlimit(15000)

locks = []
keys = []


def do_box(is_lock, box):
    global locks, keys
    cols = len(box[0])
    rows = len(box)
    code = []

    if is_lock:
        start = 1
        end = rows
        step = 1
    else:
        start = rows-2
        end = 0
        step = -1

    for c in range(0,cols):
        cnt = 0
        for r in range(start,end,step):
            if box[r][c] == '#':
                cnt = cnt + 1
            else:
                break
        code.append(cnt)

    if is_lock:
        locks.append(code)
    else:
        keys.append(code)

def read_data(fname):
    global locks, keys
    locks = []
    keys = []
    f = open(fname,"r")
    first = True  # start of lock or key
    is_lock = False
    box = []
    for line in f:
        line = line.strip()
        if line:
            if first:
                first = False
                box = []
                is_lock = (line[0] == '#')  # lock
            box.append(line)
        else:
            do_box(is_lock, box)
            first = True  # next lock or key
            box = []
    f.close()
    do_box(is_lock, box)

def process():
    sum = 0
    for lock in locks:
        for key in keys:
            ln = len(key)
            sums = []
            for i in range(0,ln):
                sums.append(lock[i] + key[i])
            match = True
            for i in range(0,ln):
                if sums[i] > 5:
                    match = False
            #print(str(lock) + " " + str(key) + " " + str(sums) + " " + str(match))
            if match:
                sum = sum + 1
    print("sum = " + str(sum))

def day25(fname):
    read_data(fname)
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day25(fname)
    else:
        print("Usage: python day25 input.txt")
