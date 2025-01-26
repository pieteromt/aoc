import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
# good news: 0 always remains in front of the list.
# so we don't need to keep track of the whole list.
# we only need to keep track of insertions right after the zero.
def insert(lst, cur, steps, val):
    idx = (cur + steps)%val
    if idx == 0:
        lst.insert(idx+1,val)
    return idx+1

def do_inserts(steps):
    lst = [0]
    cur = 0
    for i in range(50000000):
        cur = insert(lst, cur, steps, i+1)
        if cur == 1:
            idx = lst.index(0)
            print(str(i) + "   " + str(lst[idx+1]))
    return lst

def process(data):
    lst = do_inserts(data[0])
    idx = lst.index(0)
    print(lst[idx+1])

def day17(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])

