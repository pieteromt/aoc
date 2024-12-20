import sys

def make_hist(arr):
    mx = max(arr)
    hist = [0] * (mx+1)
    for nr in arr:
        hist[nr] = hist[nr] + 1
    return hist

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
    hist = make_hist(right_s)
    #print(hist)
    mx = len(hist) - 1
    for nr in left_s:
        if (nr >= 0) and (nr <= mx):
            sum = sum + nr * hist[nr]
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

