import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def get_next(presents, elf):
    next_elf = elf
    ln = len(presents)
    while True:
        next_elf = (next_elf + 1)%ln
        if presents[next_elf] != 0:
            return next_elf

def elves(nr):
    presents = [1] * nr
    elf = 0
    while True:
        if presents[elf] != 0:
            next_elf = get_next(presents, elf)
            presents[elf] += presents[next_elf]
            presents[next_elf] = 0
            if presents[elf] == nr:
                break
        elf = (elf + 1)%nr
    return elf

def process(data):
    for d in data:
        elf = elves(d)
        print("Elf: " + str(elf+1))

def day19(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19 input.txt") 
    else:
    	day19(sys.argv[1])

