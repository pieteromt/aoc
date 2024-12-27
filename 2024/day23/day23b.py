import sys

#sys.setrecursionlimit(15000)

conn = []
comp = {}

def read_data(fname):
    global conn
    conn = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            words = line.split('-')
            conn.append((words[0],words[1]))
    f.close()

def make_comp():
    global comp
    for c in conn:
        c1, c2 = c
        if not c1 in comp:
            comp[c1] = [c2]
        else:
            comp[c1].append(c2)
        if not c2 in comp:
            comp[c2] = [c1]
        else:
            comp[c2].append(c1)
    for c in comp.keys():
        comp[c].sort()

# get the rotten apples
def get_apples(arr, rows, cols):
    ln = len(arr)
    ra = []
    ca = []
    for i in range(0,ln):
        if rows[i] > 0:
            ra.append(arr[i])
        if cols[i] > 0:
            ca.append(arr[i])
    return ra, ca    

# find the minimum set of 'rotten apples'
def calc_minimal(arr):
    ln = len(arr)
    rows = [0] * ln
    cols = [0] * ln
    for i in range(0,ln):
        for j in range(i+1,ln):
            ci = arr[i]
            cj = arr[j]
            if not ci in comp[cj]: # rotten apple?
                rows[i] += 1
                cols[j] += 1
    ra, ca = get_apples(arr, rows, cols)      
    if len(ra) < len(ca):
        return ra
    else:
        return ca

# arr is array with rotten apples
def remove_rotten_apples(c, arr):
    filt_arr = comp[c]
    for apple in arr:
        filt_arr.remove(apple)
    filt_arr.append(c)  # don't forget to add 'c' itself :-)
    filt_arr.sort()
    return ",".join(filt_arr)

def process():
    minimum = 9999
    min_com = None
    min_arr = None
    for c in comp:
        arr = calc_minimal(comp[c])
        ln = len(arr)
        if ln < minimum:
            minimum = ln
            min_com = c
            min_arr = arr
    print(remove_rotten_apples(min_com, min_arr))

def day23(fname):
    read_data(fname)
    make_comp()
    process()

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day23(fname)
    else:
        print("Usage: python day23 input.txt")
