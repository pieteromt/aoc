import sys

from collections import Counter

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def char_range2(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c) * 2

def rule1(s):
    counter = Counter(s)
    vowels = 0
    for c in "aeiou":
        vowels += counter[c]
    return vowels >= 3

def rule2(s):
    doubles = 0
    for cc in char_range2('a','z'):
        doubles += s.count(cc)
    return doubles >= 1

def rule3(s):
    count = 0
    for cc in "ab","cd","pq","xy":
        count += s.count(cc)
    return count == 0

def is_nice(s):
    return rule1(s) and rule2(s) and rule3(s)

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

