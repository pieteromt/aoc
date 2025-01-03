import sys

def read_data(fname):
    f = open(fname,"r")
    data = []
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def calc_qe(data,mask):
    qe = 1
    pwr = 1
    for i in range(len(data)):
        if mask & pwr != 0:
            qe *= data[i]
        pwr <<= 1
    return qe

def calc_sum(data,mask):
    sum = 0
    pwr = 1
    for i in range(len(data)):
        if mask & pwr != 0:
            sum += data[i]
        pwr <<= 1
    return sum

def print_list(data,mask):
    pwr = 1<<(len(data)-1)
    for i in range(len(data)-1,-1,-1):
        if mask & pwr != 0:
            print(str(data[i]) + " ", end='')
        pwr >>= 1
    print("")

def find_minimum_bits(data,goal):
    sum = 0
    nr = 0
    for i in range(len(data)-1,-1,-1):
        nr += 1
        sum += data[i]
        if sum >= goal:
            break
    return nr

def mask_with_n_bits(max_bits, n_bits):
    for mask in range(2**max_bits):
        if mask.bit_count() == n_bits:
            yield mask

def find_goals(data,goal):
    min_bits = find_minimum_bits(data,goal)
    max_bits = len(data)
    min_qe = -1
    for n_bits in range(min_bits,len(data)+1):
        print("Trying " + str(n_bits) + " bits...")
        for mask in mask_with_n_bits(max_bits,n_bits):
            sum = calc_sum(data,mask)
            if sum == goal:
                qe = calc_qe(data,mask)
                if min_qe == -1 or qe < min_qe:
                    min_qe = qe
                print(str(n_bits) + " (QE=" + str(qe) + ") ",end='')
                print_list(data,mask)
        if min_qe != -1:
            break
    print("min bits = " + str(n_bits) + ", min QE = " + str(min_qe))

def process(data):
    mask = 2**len(data) - 1
    sum = calc_sum(data,mask)
    goal = sum//4
    print("sum = " + str(sum))
    print("goal = " + str(goal))  # 512
    find_goals(data,goal)

def day24(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day24 input.txt") 
    else:
    	day24(sys.argv[1])

