import sys

#sys.setrecursionlimit(1500)

arr = []
arr0 = []
arr1 = []

def read_data(fname):
    global arr
    arr = []
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            words = line.split()
            for word in words:
                arr.append(word)
        else:
            break
    f.close()

def rules(s):
    global arr0, arr1
    si = int(s)
    ln = len(s)
    if si == 0:
       si = 1
       arr1.append(str(si))
    elif ln%2 == 0:
        div = ln//2;
        s0 = s[:div]
        s1 = s[div:]
        si0 = int(s0)
        si1 = int(s1)
        arr1.append(str(si0))
        arr1.append(str(si1))
    else:
        si = si*2024
        arr1.append(str(si))

def process(val, count):
    #print("val = " + val)
    global arr0, arr1
    arr0 = [ val ]
    for i in range(0,count):
        #print("val = " + val + ", i = " + str(i))
        arr1 = []
        for s in arr0:
            rules(s)
        arr0 = arr1
    return len(arr0)

total = 0

def loop():
    ln = len(arr)
    sum = 0
    for i in range(0,ln):
        sum = sum + process(arr[i], 25)
        #print(arr0)
    print("sum = " + str(sum))
        
def day11(fname):
    read_data(fname)
    #print(arr)
    loop()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day11 input.txt") 
    else:
    	day11(sys.argv[1])

