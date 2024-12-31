import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data

def calc_sum(arr,mask):
    sum = 0
    pwr = 1
    for val in arr:
        if mask & pwr != 0:
            sum += val
        pwr <<= 1
    return sum

def find_minimum(arr,goal):
    b_min = -1
    for mask in range(0,2**len(arr)):
        sum = calc_sum(arr,mask)
        if sum == goal:
            bc = mask.bit_count()
            if b_min == -1 or bc < b_min:
                b_min = bc
    return b_min

def search(arr,goal,b_min):
    cnt = 0
    for mask in range(0,2**len(arr)):
        sum = calc_sum(arr,mask)
        if sum == goal and mask.bit_count() == b_min:
            cnt += 1
    print("Combinations: " + str(cnt))
    
def process(data,goal):
    b_min = find_minimum(data,goal)
    search(data,goal,b_min)

def day17(fname):
    data = read_data(fname)
    process(data,150)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])

