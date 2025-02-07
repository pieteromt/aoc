import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
def remove_unit(s,c):
    s1 = ""
    for i in range(len(s)):
        c1 = s[i]
        if c1.lower() != c:
            s1 += c1
    return s1

def react(s,c):
    s = remove_unit(s,c)
    i = 0
    n = len(s)
    while i < n-1:
        c1 = s[i]
        c2 = s[i+1]
        if (c1.lower() == c2.lower()) and (c1 != c2):
            #print("remove " + c1 + " and " + c2)
            s = s[:i] + s[i+2:]
            n -= 2
            i = 0  # restart
        else:
            i += 1
    return len(s)

def process(s):
    min_len = 99999
    for c in "abcdefghijklmnopqrstuvwxyz":
        ln = react(s,c)
        if ln < min_len:
            min_len = ln
            min_c = c
    print("Minimum length is " + str(min_len) + " for unit '" + min_c + "'")

def day5(fname):
    data = read_data(fname)
    process(data[0])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])
