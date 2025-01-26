import sys

def read_data(fname):
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data = line.split(',')
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

def process(data, len_list):
    lst = []
    for i in range(len_list):
        lst.append(i)
    cur = 0
    skip = 0
    for sln in data:
        ln = int(sln)
        reverse(lst, cur, ln)
        cur = (cur + ln + skip)%len_list
        skip += 1
    lst0 = lst[0]
    lst1 = lst[1]
    mult = lst0*lst1
    print(str(lst0) + " * " + str(lst1) + " = " + str(mult))

def day10(fname):
    data = read_data(fname)
    #process(data,5)    # test input
    process(data,256)   # real input

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])

