import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def rule1(s):
    for i in range(0,len(s)-1):
        if s.count(s[i:i+2]) >= 2:
            return True
    return False

def rule2(s):
    for i in range(0,len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False
    
def is_nice(s):
    return rule1(s) and rule2(s)

def process(data):
    sum = 0
    for s in data:
        print(s + " " + str(is_nice(s)))
        if is_nice(s):
            sum += 1
    print("sum = " + str(sum))

def day5(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])

