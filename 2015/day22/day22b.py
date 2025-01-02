# 
# % python3 day22b.py spells.txt input.txt | grep minimum
# New minimum: 9999
# New minimum: 1937
# Final minimum = 1937
# 
import sys

# Hit_Points, Damage
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
    
def read_spells(fname):
    spells = {}
    f = open(fname,"r")
    titles = []
    for line in f:
        line = line.strip()
        if len(titles) == 0:
            titles = line.split()  # titles[0] = "Spell", titles[1] = "Cost" etc.
        else:
            w = line.split()
            props = {}
            name = w[0]
            props["name"] = name
            for i in range(1,len(w)):
                props[titles[i]] = int(w[i])
            spells[name] = props
    f.close()
    return spells

def set_player(hitpoints, armor, damage, mana):
    data = {}
    data["Hit_Points"] = hitpoints
    data["Armor"] = armor
    data["Damage"] = damage
    data["Mana"] = mana
    return data

# returns True if the player can play the spell
def can_play_spell(player, spell, active):
    name = spell["name"]
    if name in active:  # cannot start a spell that is active
        print("Cannot use spell " + name + " due to already active.")
        return False
    if player["Mana"] < spell["Cost"]:  # not enough mana
        print("Cannot use spell " + name + " due to too little mana.")
        return False
    return True

def cast_spell(player, spell, active):
    if can_play_spell(player, spell, active):
        name = spell["name"]
        player["Mana"] -= spell["Cost"]
        active[name] = spell["Effect"]
        armor = spell["Armor"]
        if armor != 0:
            print("Player casts " + name + ", increasing armor by " + str(armor))
            player["Armor"] += armor
        else:
            print("Player casts " + name + ".")
    else:
        player["Hit_Points"] = -1  # player has lost (illegal spell)

def execute_spell(spells, player, boss, spell, active):
    if can_play_spell(player, spell, active):
        player["Mana"] -= spell["Cost"]
        name = spell["name"]
        #----
        damage = spell["Damage"]
        print("Player casts " + name + ", dealing " + str(damage) + " damage.")
        boss["Hit_Points"] -= damage
        #----
        heals = spell["Heals"]
        if heals != 0:
            print("Player casts " + name + ", healing " + str(heals) + " hit points.")
            player["Hit_Points"] += heals
    else:
        player["Hit_Points"] = -1  # player has lost (illegal spell)

def execute_boss(player, boss):
    damage = boss["Damage"]
    armor = player["Armor"]
    damage -= armor
    if damage <= 0:
        damage = 1
    print("Boss attacks for " + str(damage) + " damage!")
    player["Hit_Points"] -= damage

def execute_active_spells(spells, player, boss, active):
    expired = []
    for name in active:
        active[name] -= 1  # decrease timer
        damage = spells[name]["Damage"]
        if damage != 0:
            boss["Hit_Points"] -= damage
            print(name + " deals " + str(damage) + " damage; its timer is now " + str(active[name]))
        mana = spells[name]["Mana"]
        if mana != 0:
            print(name + " provides " + str(mana) + " mana; its timer is now " + str(active[name]))
            player["Mana"] += mana
        armor = spells[name]["Armor"]
        if armor != 0:
            print(name + "'s timer is now " + str(active[name]))
        if active[name] == 0:
            print(name + " wears off.")
            expired.append(name)
            player["Armor"] -= armor
    # remove expired spells
    for name in expired:
        active.pop(name)

def finished(player, boss):
    return (player["Hit_Points"] <= 0) or (boss["Hit_Points"] <= 0)

def play_spell(spells, player, boss, spell, active):
    execute_active_spells(spells, player, boss, active)
    if not finished(player, boss):
        if spell == None:  # boss turn
            execute_boss(player, boss)
        else:
            if spell["Effect"] == 0: # instant spell
                execute_spell(spells, player, boss, spell, active)
            else:
                cast_spell(player, spell, active)

# note: if boss plays, spell is None
def play(spells, player, boss, spell, active):
    if spell != None:
        print("-- Player turn --")
    else:
        print("-- Boss turn -- ")
    print("- Player has " + str(player["Hit_Points"]) + " hit points, " + \
          str(player["Armor"]) + " armor, " + str(player["Mana"]) + " mana")
    print("- Boss has " + str(boss["Hit_Points"]) + " hit points")
    play_spell(spells, player, boss, spell, active)
    print("")
    return finished(player, boss)

# returns the Hit Points of the player after the game has finished
# if negative or zero, player has lost
# choices is the array of spell names for each turn
def play_game(spells, player, boss, choices):
    player_turn = True
    active = {}  # dict of active spell names, value is timer
    idx = 0
    while True:
        if player_turn:
            player["Hit_Points"] -= 1  # hard difficulty, extra minus point (part2)
            if idx < len(choices):
                spell = spells[choices[idx]]
                idx += 1
            else:
                print("Not enough spells to win...")
                return -1, 0  # not enough spells provided
        else:
            spell = None
        if play(spells, player, boss, spell, active):
            print("Play has finished: player = " + str(player["Hit_Points"]) + " boss = " + str(boss["Hit_Points"]))
            break
        player_turn = not player_turn
    return player["Hit_Points"], idx

# -------------------- EXAMPLES ----------------------------
def run_example(spells, player, boss, choices):
    points, idx = play_game(spells, player, boss, choices)
    if points > 0:
        print("Player wins!")
    else:
        print("Boss wins!")

def run_example1(spells):
    player = set_player(10,0,0,250)
    boss = set_player(13,0,8,0)
    choices = []
    choices.append("Poison")
    choices.append("Magic_Missile")
    run_example(spells, player, boss, choices)

def run_example2(spells):
    player = set_player(10,0,0,250)
    boss = set_player(14,0,8,0)
    choices = []
    choices.append("Recharge")
    choices.append("Shield")
    choices.append("Drain")
    choices.append("Poison")
    choices.append("Magic_Missile")
    run_example(spells, player, boss, choices)

def calc_cost(spells, choices, nr):
    mana = 0
    for idx in range(nr):
        name = choices[idx]
        mana += spells[name]["Cost"]
    return mana

def get_names(spells):
    names = []
    for name in spells:
        names.append(name)
    return names

# minimal cost
m_cost = -1

# returns the cost (in units of mana) when the player wins
def do_run(spells, data, names, choices):
    global m_cost
    player = set_player(50,0,0,500)
    boss = set_player(data["Hit_Points"], 0, data["Damage"], 0)
    points, idx = play_game(spells, player, boss, choices)
    if idx == 0: # not enough inputs, try extra choices
        for name in names:
            all_choices = choices + [name]
            cost = do_run(spells, data, names, all_choices)
            if m_cost == -1 or cost < m_cost:
                m_cost = cost
                print("New minimum: " + str(cost))
        return m_cost
    else: # enough input spells provided
        if points > 0:
            print("Player wins!")
            cost = calc_cost(spells, choices, idx)
        else:
            print("Boss wins!")
            cost = 9999
        return cost

def simulate(spells, data):
    names = get_names(spells)
    do_run(spells, data, names, [])
    print("Final minimum = " + str(m_cost))

def show_dict(data):
    for d in data:
        print(d + " : " + str(data[d]))
    print("")

def day22(fname1, fname2):
    spells = read_spells(fname1)
    #show_dict(spells)
    data = read_data(fname2)
    #show_dict(data)
    #run_example1(spells)
    #run_example2(spells)
    simulate(spells, data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: day22 spells.txt input.txt | grep minimum") 
    else:
    	day22(sys.argv[1], sys.argv[2])

