import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def get_next(presents, idx):
    ln = len(presents)
    next_idx = (idx + (ln//2))%ln
    #print("elf: " + str(presents[idx][0]) + ", next_elf: " + str(presents[next_idx][0]))
    return next_idx

def elves(nr):
    presents = []
    for i in range(nr):
        presents.append((i+1,1))  # tuple (elf, #presents)
    idx = 0
    #print(presents)
    while True:
        #print("idx = " + str(idx))
        t = presents[idx]
        next_idx = get_next(presents, idx)
        next_pres = presents[next_idx][1]
        tot_pres = t[1] + next_pres
        #print("Elf " + str(t[0]) + " takes " + str(next_pres) + " presents from elf " + str(presents[next_idx][0]))
        presents[idx] = (t[0], tot_pres)
        if tot_pres == nr:
            break
        #print("Elf " + str(presents[next_idx][0]) + " leaves.")
        presents.pop(next_idx)
        #print(presents)
        ln = len(presents)
        if ln%10000 == 0:
            print("Length = " + str(ln))
        if next_idx > idx:
            idx += 1
        if idx >= ln:
            idx = 0
    return presents[idx][0]  # elf

def process(data):
    for d in data:
        elf = elves(d)
        print("Elf: " + str(elf))

def day19(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])

