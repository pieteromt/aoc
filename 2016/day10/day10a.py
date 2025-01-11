import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 6:
            cmd = w[0]      # "value"
            val = int(w[1])
            bot = int(w[5])
            data.append((cmd,val,bot))
        elif len(w) == 12:
            cmd = w[0]      # "bot"
            bot = int(w[1])
            dst0 = w[5]     # "output" or "bot"
            out0 = int(w[6])
            dst1 = w[10]
            out1 = int(w[11])
            data.append((cmd,bot,dst0,out0,dst1,out1))
        else:
            print("Error: " + str(len(w)))
            exit()
    f.close()
    return data
    
def init_bot(bots, bot):
    if not bot in bots:
        bots[bot] = { "values": [], "rule": None }

def init_output(outputs, out):
    if not out in outputs:
        outputs[out] = { "values": [] }

def init_bots(data):
    bots = {}
    outputs = {}
    for d in data:
        if d[0] == "value":
            init_bot(bots,d[2])
        else:
            if d[2] == "bot":
                init_bot(bots,d[3])
            else:
                init_output(outputs,d[3])
            if d[4] == "bot":
                init_bot(bots,d[5])
            else:
                init_output(outputs,d[5])
    return bots, outputs

def init_values_and_rules(data, bots):
    for d in data:
        if d[0] == "value":
            bots[d[2]]["values"].append(d[1])
        else:
            bots[d[1]]["rule"] = (d[2],d[3],d[4],d[5])

def part_one(bot):
    print("bot " + str(bot) + " compares 17 and 61")

def part_two(outputs):
    val = 1
    for out in range(3):
        val *= outputs[out]["values"][0]
    print("Multiply: " + str(val))

# return True if a move was made
def make_move(bots, outputs, bot):
    values = bots[bot]["values"]
    rule = bots[bot]["rule"]
    if len(values) == 2:
        min_val = min(values)
        max_val = max(values)
        if min_val == 17 and max_val == 61:
            part_one(bot)
        if rule[0] == "bot":
            bots[rule[1]]["values"].append(min_val)
        else:
            outputs[rule[1]]["values"].append(min_val)
        if rule[2] == "bot":
            bots[rule[3]]["values"].append(max_val)
        else:
            outputs[rule[3]]["values"].append(max_val)
        bots[bot]["values"] = []
        return True
    return False

def move_values(bots, outputs):
    while True:
        made_move = False
        for bot in sorted(bots.keys()):
            if make_move(bots, outputs, bot):
                made_move = True
        if not made_move:  # we're done
            break

def show_status(status, bots, outputs):
    print(status)
    for bot in sorted(bots.keys()):
        print("bot " + str(bot) + " : " + str(bots[bot]))
    for out in sorted(outputs.keys()):
        print("output " + str(out) + " : " + str(outputs[out]))
    print("")

def process(data):
    bots, outputs = init_bots(data)
    init_values_and_rules(data, bots)
    #show_status("before", bots, outputs)
    move_values(bots, outputs)
    #show_status("after", bots, outputs)
    part_two(outputs)

def day10(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day10 input.txt") 
    else:
    	day10(sys.argv[1])

