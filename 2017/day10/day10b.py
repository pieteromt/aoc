import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        for c in line:
            data.append(ord(c))
    f.close()
    return data
    
def reverse(lst, cur, ln):
    len_lst = len(lst)
    sub = []
    idx = cur
    for i in range(ln):
        sub.append(lst[idx])
        idx = (idx+1)%len_lst
    sub.reverse()
    idx = cur
    for i in range(ln):
        lst[idx] = sub[i]
        idx = (idx+1)%len_lst

def calc_sparse(data):
    lst = []
    for i in range(256):
        lst.append(i)
    cur = 0
    skip = 0
    for i in range(64):
        for ln in data:
            reverse(lst, cur, ln)
            cur = (cur + ln + skip)%256
            skip += 1
    return lst

def calc_dense(lst):
    dense = []
    for i in range(16):
        val = lst[16*i]
        for j in range(1,16):
            val ^= lst[16*i + j]
        dense.append(val)
    return dense

def process(data):
    lst = calc_sparse(data)
    lst = calc_dense(lst)
    hx = ""
    for val in lst:
        hx += "{:02x}".format(val)
    print(hx)

def day10(fname):
    data = read_data(fname)
    data.append(17)
    data.append(31)
    data.append(73)
    data.append(47)
    data.append(23)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])

