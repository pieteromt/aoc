import sys

# 0 = +++++
# 1 = *++++
# 2 = +*+++
# 3 = **+++
# etc

# returns 0, 1 or 2
# bit = 0, 1, 2
def calc_mask(val, bit):
    m = 0
    mul = 3**bit
    div = val//mul
    mod = div%3
    #print("val = " + str(val) + ", div = "+ str(div) + ", mod = " + str(mod) + ",  bit = " + str(bit) + ", m = " + str(m))
    return mod

def calc(nums, val):
    #print(nums)
    #print("val = " + str(val))
    result = nums[0]
    nr = len(nums)
    for i in range(0,nr-1):
        m = calc_mask(val, i)
        if m == 0:
            #print("*")
            result = result * nums[i+1]
        elif m == 1:
            #print("+")
            result = result + nums[i+1]
        else:
            #print("||")
            result = int(str(result) + str(nums[i+1]))
    return result

def match(first, nums):
    #print("first = " + str(first))
    #print(nums)
    match = False
    max = 3**(len(nums)-1)
    #print("max = "+str(max))
    for val in range(0,max):
        res = calc(nums,val)
        if res == first:
            match = True
            break
    #print("match = " + str(match))
    return match

def read_data(fname):
    sum = 0
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            words = line.split()
            first = int(words.pop(0).split(':')[0])
            nums = []
            for w in words:
               nums.append(int(w))
            if match(first, nums):
                sum = sum + first
        else:
            break
    f.close()
    print("sum = " + str(sum))

def day7(fname):
    read_data(fname)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])

