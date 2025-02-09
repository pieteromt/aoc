import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        data.append(line.replace("\n",""))
    f.close()
    return data
    
class Cart:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
        self.t = 0  # turn 0:left, 1:straight, 2:right, 3:left, etc.

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "  d: " + str(self.d) + "  t: " + str(self.t)

def set_xy(data,x,y,val):
    row = data[y]
    data[y] = row[:x] + val + row[x+1:]

def is_cart(val):
    return (val == "<") or (val == ">") or (val == "^") or (val == "v")

def replace(val):
    if (val == "<") or (val == ">"):
        return "-"
    else:
        return "|"

def get_dir(val):
    if val == "^":
        return 0
    elif val == ">":
        return 1
    elif val == "v":
        return 2
    else:
        return 3

def get_val(d):
    if d == 0:
        return "^"
    elif d == 1:
        return ">"
    elif d == 2:
        return "v"
    else:
        return "<"

def show_data(data):
    for d in data:
        print(d)
    print("")

def find_carts(data):
    carts = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            val = data[y][x]
            if is_cart(val):
                carts.append(Cart(x,y,get_dir(val)))
                set_xy(data,x,y,replace(val))
    return carts

def calc_delta(d):
    if d == 0:
        return 0,-1
    elif d == 1:
        return 1,0
    elif d == 2:
        return 0,1
    else:
        return -1,0

def new_d(d,t):
    if t == 0:
        return (d+3)%4  # turn left
    elif t == 1:
        return d
    else:
        return (d+1)%4  # turn right

# direction d
# 0 = up      ^
# 1 = right   >
# 2 = down    v
# 3 = left    <
def do_tick_cart(data, cart):
    x = cart.x
    y = cart.y
    d = cart.d
    dx, dy = calc_delta(d)
    x += dx
    y += dy
    val = data[y][x]
    if (val == "-") or (val == "|"):  # continue
        pass
    elif val == "\\":
        d = 3 - d
    elif val == "/":
        if d <= 1:
            d = 1 - d
        else:
            d = 5 - d
    elif val == "+":
        d = new_d(d, cart.t)    
        cart.t = (cart.t + 1)%3
    else:
        print("error: val is " + val)
        exit()
    cart.x = x
    cart.y = y
    cart.d = d

def crash(c1, c2):
    return (c1.x == c2.x) and (c1.y == c2.y)

def check_crashes(carts, i):
    c1 = carts[i]
    for j in range(len(carts)):
        if j == i:
            continue
        if crash(c1, carts[j]):
            return (c1.x, c1.y)
    return None

def cart_order(cart):
    return cart.x + (cart.y * 1000)

def do_tick(data, carts):
    carts.sort(key=cart_order)
    for i in range(len(carts)):
        cart = carts[i]
        do_tick_cart(data, cart)
        t = check_crashes(carts, i)
        if t != None:
            print("crash at " + str(t))
            return False
    #dc = data.copy()
    #for cart in carts:
    #    set_xy(dc, cart.x, cart.y, get_val(cart.d))
    #show_data(dc)
    return True

def process(data):
    #show_data(data)
    carts = find_carts(data)
    #for cart in carts:
    #    print(cart)
    #show_data(data)
    while do_tick(data, carts):
        pass

def day13(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])
