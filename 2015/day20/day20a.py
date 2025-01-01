import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data

def factors(i):
    print(str(i) + " : ",end='')
    for j in range(1,i+1):
        if i%j == 0:
            print(str(j) + " ",end='')
    print("")

def calc_presents(i):
    sum = 0
    for j in range(1,i+1):
        if i%j == 0:
            sum += j
    return 10*sum

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# find lower and upper limit for search range
def test_facts(d):
    i = 1 
    prev = 1
    while True:
        fact = factorial(i)
        presents = calc_presents(fact)
        if presents >= d:
            p1 = calc_presents(prev)
            p2 = calc_presents(fact)
            break
        prev = fact
        i += 1
    return prev,fact

def search(d,low):
    i = low
    mx = 0
    while True:
        presents = calc_presents(i)
        if presents >= mx:
            mx = presents
            factors(i)
            print(str(i) + " " + str(presents) + " " + str(mx))
            print("")
        if presents >= d:
            print("Found: " + str(i) + " " + str(presents))
            break
        i += 2

def process(data):
    for d in data:
        low,high = test_facts(d)
        search(d,22*low//10)

def day20(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])

