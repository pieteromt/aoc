import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        ts = w[0] + "_" + w[1]
        if w[2].startswith("Guard"):
            guard = int(w[3].replace("#",""))
            data[ts] = guard
        elif w[2] == "wakes":
            data[ts] = "wakeup"
        else:
            data[ts] = "sleep"
    f.close()
    return data
    
# [1518-11-23_00:43]
def get_date_time(key):
    key = key.replace("[","").replace("]","")
    dt = key.split("_")
    date = dt[0].split("-")
    date = [int(item) for item in date]
    time = dt[1].split(":")
    time = [int(item) for item in time]
    return date, time

def set_single_val(bar,t,val):
    return bar[:t] + val + bar[t+1:]

def set_val(bar, minute, val):
    for t in range(minute,len(bar)):
        bar = set_single_val(bar,t,val)
    return bar

def set_sleep(bar, minute):
    return set_val(bar, minute, '#')

def set_awake(bar, minute):
    return set_val(bar, minute, '.')

def init_bar():
    return "." * 60

def show_bar(stats, date, guard, bar):
    print("{:02d}".format(date[1]) + "-" + "{:02d}".format(date[2]) + "   #" + "{:04d}".format(guard)  + "   " + bar)
    if guard in stats:
        stats[guard].append(bar)
    else:
        stats[guard] = [bar]

def count_sleep(bar):
    cnt = 0
    for i in range(len(bar)):
        if bar[i] == '#':
            cnt += 1
    return cnt

def max_minute(bars):
    n = len(bars[0])  # 60
    hist = [0] * n
    for bar in bars:
        for i in range(n):
            if bar[i] == '#':
                hist[i] += 1
    return hist.index(max(hist))

def do_stats(stats):
    max_guard = 0
    max_min = 0
    for guard in stats:
        minutes = max_minute(stats[guard])
        if minutes > max_min:
            max_min = minutes
            max_guard = guard
    print("Max guard is " + str(max_guard))
    print("Max minute is " + str(max_min))
    print("Answer is " + str(max_guard * max_min))

def process(data):
    stats = {}
    guard = 0
    bar = init_bar()
    for d in sorted(data.keys()):
        date, time = get_date_time(d)
        rec = data[d]
        if rec == "wakeup":
            #print("Guard " + str(guard) + " wakes up at " + str(get_date_time(d)))
            bar = set_awake(bar, time[1])
        elif rec == "sleep":
            #print("Guard " + str(guard) + " goes asleep at " + str(get_date_time(d)))
            bar = set_sleep(bar, time[1])
        else:
            if guard != 0:
                show_bar(stats, date, guard, bar)
            guard = rec
            bar = init_bar()
            #print("Guard " + str(guard) + " begins shift at " + str(get_date_time(d)))
    show_bar(stats, date, guard, bar)
    do_stats(stats)

def day4(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])
