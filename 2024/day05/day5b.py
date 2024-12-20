import sys

order = []
updates = []

def check_page(pages, i):
    ok = True
    #print(pages)
    p = pages[i]
    #print("page = " + p)
    for o in order:
        if o[0] == p:
            value = o[1]
            if value in pages:
                j = pages.index(value)
                if j <= i:
                    ok = False
                    break
    return ok


def check_pages(pages):
    all_ok = True
    nr = len(pages)
    for i in range(0,nr):
        ok = check_page(pages, i)
        if not ok:
            all_ok = False
            break
    return all_ok

def wrong(pages, i):
    ok = True
    p = pages[i]
    for o in order:
        if o[0] == p:
            value = o[1]
            if value in pages:
                j = pages.index(value)
                if j <= i:
                    ok = False
                    break
    if ok:
        return (0,0)
    else:
        return (i, j)

def wrong_index(pages):
    nr = len(pages)
    for i in range(0,nr):
        x,y = wrong(pages, i)
        if (x,y) != (0,0):
            break
    return (x,y)

def read_data(fname):
    global order, updates
    state = 0
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            if state == 0:
                words = line.split("|")
                n1 = words[0]
                n2 = words[1]
                #print("n1 = " + n1 + ", n2 = " + n2)
                order.append((n1,n2))
            else:
                words = line.split(",")
                nr = len(words)
                pages = []
                for i in range(0,nr):
                    n = words[i]
                    pages.append(n)
                updates.append(pages)
        else:
            if state == 0:
                state = 1
                continue
            else:
                break
    f.close()

def fix_pages(pages):
    print(pages)
    while not check_pages(pages):
        i, j = wrong_index(pages)
        print("wrong = " + str(i) +", " + str(j))
        p1 = pages[i]
        p2 = pages[j]
        pages[i] = p2
        pages[j] = p1
        print(pages)
    print(pages)

def day5(fname):
    sum = 0
    read_data(fname)
    for pages in updates:
        ok = check_pages(pages)
        if not ok:
            fix_pages(pages)
            nr = len(pages)
            mid = nr//2
            sum = sum + int(pages[mid])
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])

