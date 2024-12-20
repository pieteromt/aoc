import sys

def day1(fname):
    sum = 0
    left = []
    right = []
    f = open(fname,"r")
    for line in f:
        numbers = line.strip().split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    f.close()
    left_s = sorted(left)
    right_s = sorted(right)
    #print(left_s)
    #print(right_s)
    nr = len(left_s)
    for i in range(0,nr):
        diff = abs(left_s[i] - right_s[i])
        sum = sum + diff
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

