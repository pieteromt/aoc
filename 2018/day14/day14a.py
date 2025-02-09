import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def print_recipes(recipes, elves):
    for i in range(len(recipes)):
        if i == elves[0]:
            print("("+str(recipes[i])+")",end='')
        elif i == elves[1]:
            print("["+str(recipes[i])+"]",end='')
        else:
            print(" "+str(recipes[i])+" ",end='')
    print("")

def do_round(recipes, elves):
    sum = recipes[elves[0]] + recipes[elves[1]]
    if sum >= 10:
        recipes.append(sum//10)
    recipes.append(sum%10)
    for i in range(len(elves)):
        idx = elves[i]
        val = recipes[idx]
        idx = (idx + val + 1)%len(recipes)
        elves[i] = idx

def do_rounds(recipes, elves, d):
    #print_recipes(recipes, elves)
    while True:
        do_round(recipes, elves)
        #print_recipes(recipes, elves)
        if len(recipes) >= (d + 10):
            break
    for i in range(10):
        print(recipes[d+i],end='')
    print("")

def process(data):
    for d in data:
        recipes = [3,7]
        elves = [0,1]
        do_rounds(recipes, elves, d)

def day14(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day14 input.txt") 
    else:
    	day14(sys.argv[1])
