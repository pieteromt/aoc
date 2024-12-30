import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def triple_range():
    for i in range(ord('a'),ord('y')):
        yield chr(i)+chr(i+1)+chr(i+2)

def double_range():
    for c in range(ord('a'), ord('z')+1):
        yield chr(c) * 2

def rule1(pw):
    for tr in triple_range():
        if tr in pw:
            return True
    return False

def rule2(pw):
    illegal = "iol"
    for c in illegal:
        if c in pw:
            return False
    return True

def rule3(pw):
    doubles = 0
    for dd in double_range():
        if dd in pw:
            doubles += 1
    return doubles >= 2

def is_valid(pw):
    return rule1(pw) and rule2(pw) and rule3(pw)

def increment(pw):
    rest = pw[:-1]  # pw = rest + last
    last = pw[-1]
    if last == 'z':
        return increment(rest) + 'a'
    else:
        return rest + chr(ord(last)+1)

def calc_next_valid(pw):
    while True:
        pw = increment(pw)
        if is_valid(pw):
            return pw

def process(data):
    for pw in data:
        print("pw: " + pw, end='')
        pw = calc_next_valid(pw)
        print(", next: " + pw)

def day11(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day11 input.txt") 
    else:
    	day11(sys.argv[1])

