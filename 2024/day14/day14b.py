import sys

data = []
map = []
cols = 0   # x coord
rows = 0   # y coord

max_x = 0
max_y = 0

min_vx = 0
min_vy = 0
max_vx = 0
max_vy = 0



def set_ch(r,c,val):   # y,x
    global map
    row = map[r]
    new_row = row[:c]
    new_row.append(val)
    for i in range(c+1,cols):
        new_row.append(row[i])
    map[r] = new_row

def ch(row,col):  # y,x
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return map[row][col]
    else:
        return 0  # outside

def init_map():
    global map
    map = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            row.append(0)
        map.append(row)    
#
# x,y = top left
# x = col, y = row
# vx, vy = tiles per second

def read_data(fname):
    global data, max_x, max_y, min_vx, min_vy, max_vx, max_vy
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            row = []
            words = line.split()
            p = words[0].split('=')
            pp = p[1].split(',')
            x = int(pp[0])
            y = int(pp[1])
            row.append([x,y])
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            v = words[1].split('=')
            vv = v[1].split(',')
            vx = int(vv[0])
            vy = int(vv[1])
            if vx < min_vx:
                min_vx = vx
            if vy < min_vy:
                min_vy = vy
            if vx > max_vx:
                max_vx = vx
            if vy > max_vy:
                max_vy = vy
            row.append([vx,vy])
            data.append(row)
        else:
            break
    f.close()
    #print(data)

def show_map():
    for row in map:
        s = ""
        for cnt in row:
            if cnt == 0:
                s = s + "."
            else:
                #s = s + "X"
                s = s + str(cnt)
        print(s)

def save_map(nr):
    number = '{:08}'.format(nr)
    fname = "tree" + number + ".txt"
    f = open(fname,"w")
    f.write("------------------\n")
    f.write("   " + number+"\n")
    f.write("------------------\n")
    for row in map:
        s = ""
        for cnt in row:
            if cnt == 0:
                s = s + "."
            else:
                #s = s + "X"
                s = s + str(cnt)
        f.write(s+"\n")
    f.close()

def add_map():
    nr = len(data)
    for i in range(0,nr):
        r = data[i]
        x,y = r[0]
        vx,vy = r[1]
        cnt = ch(y,x)
        set_ch(y,x,cnt+1)

def count(nr):
    nx = (cols - 1)//2
    ny = (rows - 1)//2
    fac = 1
    sums = []
    for qy in range(0,2):
        for qx in range(0,2):   
            sum = 0
            qy0 = qy*(ny+1)
            qx0 = qx*(nx+1)
            for y in range(qy0,qy0+ny):
                for x in range(qx0,qx0+nx):
                    cnt = ch(y,x)
                    #print("x = " + str(x) + ", y = " + str(y) + ", cnt = " + str(cnt))
                    sum = sum + cnt
            sums.append(sum)
            fac = fac * sum
    #print("nr = " + str(nr) + " " + str(sums) + ", fac = " + str(fac))
    upper = sums[0] + sums[1]
    lower = sums[2] + sums[3]
    perc = (100*upper)//(upper + lower)
    #print(str(perc) + "   "  + str(sums) +  "   nr = " + str(nr))
    if perc < 40:
        save_map(nr)

def process():
    global data
    nr = len(data)
    for t in range(0,10000):
        for i in range(0,nr):  # number of robots
            r = data[i]
            new_r = []
            x,y = r[0]
            vx,vy = r[1]
            new_x = (x + vx) % cols
            new_y = (y + vy) % rows
            new_r.append([new_x,new_y])
            new_r.append([vx,vy])
            data[i] = new_r
        init_map()
        add_map()
        count(t)


def day14(fname):
    global cols, rows
    read_data(fname)
    #for row in data:
    #    print(row)
    #print("max_x = " + str(max_x) + ", max_y = " + str(max_y))
    #print("min_vx = " + str(min_vx) + ", max_vx = " + str(max_vx))
    #print("min_vy = " + str(min_vy) + ", max_vy = " + str(max_vy))
    cols = max_x + 1
    rows = max_y + 1
    print("cols = " + str(cols) + ", rows = " + str(rows))
    #init_map()
    #show_map()
    #print(" ")
    #add_map()
    #show_map()
    process()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day14 input.txt") 
    else:
    	day14(sys.argv[1])

