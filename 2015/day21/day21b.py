import sys

def read_data(fname):
    f = open(fname,"r")
    data = {}
    for line in f:
        line = line.strip()
        w = line.split()
        name = w[0][:-1]  # remove ':'
        val = int(w[1])
        data[name] = val
    f.close()
    return data
    
def read_shop(fname):
    weapons = []
    armor = []
    rings = []
    f = open(fname,"r")
    state = 0
    for line in f:
        line = line.strip()
        if line:
            w = line.split()
            if w[0][-1] == ':': # title
                continue
            if state == 0:
                weapons.append([w[0], int(w[1]), int(w[2]), int(w[3])])
            elif state == 1:
                armor.append([w[0], int(w[1]), int(w[2]), int(w[3])])
            else:
                rings.append([w[0], int(w[1]), int(w[2]), int(w[3])])
        else:
            state = state + 1
    f.close()
    return weapons, armor, rings

def show_shop(data):
    for d in data:
        print(d)
    print("")

def show_data(data):
    for d in data:
        print(d + " : " + str(data[d]))
    print("")

def set_player(hitpoints, damage, armor, cost):
    data = {}
    data["Hit_Points"] = hitpoints
    data["Damage"] = damage
    data["Armor"] = armor
    data["Cost"] = cost
    return data

def play(attack, defend):
    damage = attack["Damage"] - defend["Armor"]
    if damage < 1:
        damage = 1
    #print(str(attack["Damage"]) + " " + str(defend["Armor"]) + " " + str(damage))
    #print("Hit_points before: " + str(defend["Hit_Points"]))
    defend["Hit_Points"] -= damage
    #print("Hit_points after: " + str(defend["Hit_Points"]))
    return (defend["Hit_Points"] <= 0)

# returns the cost of losing, or -1 if won
def play_game(player, boss):
    first = True
    while True:
        if first:
            done = play(player, boss)
        else:
            done = play(boss, player)
        if done:
            break
        first = not first
    # first means: player wins
    if first:
        return -1
    else:
        #print("Player loses! " + str(player["Cost"]))
        return player["Cost"]

def run_example():
    player = set_player(8,5,5,0)
    boss = set_player(12,7,2,0)
    cost = play_game(player, boss)
    if cost >= 0:
        print("Player wins!")
    else:
        print("Boss wins!")

def calc_props(cost, damage, armor, item):
    cost   += item[1]
    damage += item[2]
    armor  += item[3]
    return cost, damage, armor 

def calc_all_props(weapons, armors, rings):
    cost, damage, armor = 0,0,0
    for w in weapons:
        cost, damage, armor = calc_props(cost, damage, armor, w)
    for a in armors:
        cost, damage, armor = calc_props(cost, damage, armor, a)
    for r in rings:
        cost, damage, armor = calc_props(cost, damage, armor, r)
    return cost, damage, armor

def pick_weapon(weapons):
    for w in weapons:
        yield [w]

def pick_armor(armors):
    yield []
    for a in armors:
        yield [a]

def pick_rings(rings):
    yield []
    nr = len(rings)
    for i in range(nr):
        yield [rings[i]]
        for j in range(i+1,nr):
            yield [rings[i], rings[j]]

def simulate_all(weapons, armors, rings, data):
    m_cost = -1
    for w in pick_weapon(weapons):
        for a in pick_armor(armors):
            for r in pick_rings(rings):
                cost, damage, armor = calc_all_props(w,a,r)
                player = set_player(100, damage, armor, cost)
                boss = set_player(data["Hit_Points"], data["Damage"], data["Armor"], 0)
                cost = play_game(player, boss)
                if cost >= 0:  # player loses
                    if cost > m_cost:
                        m_cost = cost
    print("Maximal cost to lose: " + str(m_cost))

def day21(fname1, fname2):
    weapons, armors, rings = read_shop(fname1)
    #show_shop(weapons)
    #show_shop(armors)
    #show_shop(rings)
    data = read_data(fname2)
    #show_data(data)
    #run_example()
    simulate_all(weapons, armors, rings, data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: day21 shop.txt input.txt") 
    else:
    	day21(sys.argv[1], sys.argv[2])

