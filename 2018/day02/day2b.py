import sys
import string

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data
    
def calc_diff(s1,s2):
    if len(s1) != len(s2):
        print("error: different length")
        exit()
    n = len(s1)
    eq = 0
    df = -1
    for i in range(n):
        if s1[i] == s2[i]:
            eq += 1
        else:
            df = i
    if eq == n-1:
        answer = s1[:df] + s1[df+1:]
        print("found: " + s1 + " " + s2 + " diff at: " + str(df) + " --> " + answer)

def process(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1,n):
            calc_diff(data[i], data[j])

def day2(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])
