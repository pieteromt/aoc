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

def search(arr,goal):
    cnt = 0
    for mask in range(0,2**len(arr)):
        sum = calc_sum(arr,mask)
        if sum == goal:
            cnt += 1
    print("Combinations: " + str(cnt))
    
def process(data):
    search(data,150)

def day17(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17 input.txt") 
    else:
    	day17(sys.argv[1])

