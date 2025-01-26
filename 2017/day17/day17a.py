import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def insert(lst, cur, steps, val):
    idx = (cur + steps)%len(lst)
    lst.insert(idx+1,val)
    return idx+1

def do_inserts(steps):
    lst = [0]
    cur = 0
    for i in range(2017):
        cur = insert(lst, cur, steps, i+1)
    return lst

def process(data):
    lst = do_inserts(data[0])
    idx = lst.index(2017)
    print(lst[idx+1])

def day17(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])

