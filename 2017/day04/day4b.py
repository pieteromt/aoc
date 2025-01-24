import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(w)
    f.close()
    return data
    
# returns the characters of the word, alphabetically sorted
def rearrange(w):
    l = list(w)
    l.sort()
    return "".join(l)

# return True if no anagram words
def is_valid(arr):
    words = {}
    for w in arr:
        w1 = rearrange(w)
        if w1 in words:
            return False
        words[w1] = 1
    return True

def process(data):
    sum = 0
    for d in data:
        if is_valid(d):
            sum += 1
    print("Valid passphrases: " + str(sum))

def day4(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])

