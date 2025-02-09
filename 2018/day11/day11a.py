import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(int(line))
    f.close()
    return data
    
def power_level(x,y,sernr):
    rack_id = x + 10
    pwr = rack_id * y
    pwr += sernr
    pwr *= rack_id
    pwr = (pwr//100)%10
    pwr -= 5
    return pwr

def test():
    tt = [(3,5,8),(122,79,57),(217,196,39),(101,153,71)]
    for t in tt:
        x,y,sernr = t
        pwr = power_level(x,y,sernr)
        print(str(t) + " " + str(pwr))

def calc_grid(sernr):
    grid = [[0] * 300 for i in range(300)]
    for y in range(300):
        for x in range(300):
            grid[y][x] = power_level(x+1,y+1,sernr)
    return grid

def find_max_power(grid):
    max_pwr = 0
    for y in range(300-2):
        for x in range(300-2):
            pwr = 0
            for dy in range(3):
                for dx in range(3):
                    pwr += grid[y+dy][x+dx]
            if pwr > max_pwr:
                max_pwr = pwr
                max_x = x+1
                max_y = y+1
    print(str(max_pwr) + " for " + str(max_x) + "," + str(max_y))

def process(sernr):
    #print("serial number: " + str(sernr))
    #test()
    grid = calc_grid(sernr)
    find_max_power(grid)

def day11(fname):
    data = read_data(fname)
    process(data[0])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day11 input.txt") 
    else:
    	day11(sys.argv[1])
