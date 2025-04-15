import random as r
import os
import obstacle

def d6(modifier = 0, number = 1):
    result = number * r.randint(1,6) + modifier
    return result

player_skill = d6(modifier = 6)
player_stamina = d6(12, 2)
player_luck = d6(6)

player = {"skill": player_skill, "stamina": player_stamina, "luck": player_luck, "weapon": 'arduino "cyberdeck'}

def testStat(stat):
    result = 0
    d1 = d6()
    d2 = d6()
    if stat == "stamina" or stat == "st":
        for i in range(4): result += d6()
    else:
        result = d1 + d2
        # Check if the provided stat exists and compare the result
    if hasattr(stat):
        current_stat = getattr(stat)
        if result <= current_stat:
            print(f"Test succeeded! Rolled {result} against {stat.upper()} ({current_stat}).")
            return True
        else:
            print(f"Test failed! Rolled {result} against {stat.upper()} ({current_stat}).")
            # Reduce the stat by 1 if the test fails
            if stat == "luck":
                setattr(stat, current_stat - 1)
                print(f"Oof lost a luck point.\nCurrent Luck: {player_luck}")
            return False
    else:
        raise ValueError(f"Invalid stat: {stat}. Valid stats are 'skill', 'stamina', or 'luck'.")

class Enemy:
    # Each enemy needs their own stats STAMINA and SKILL for battles
    virus = {"name": "virus", "stamina": d6(8,2), "skill": d6(6)}

def getFight(pc, enemy):
    print(f"Player Stats: Skill: {player_skill}, Stamina: {player_stamina}, Luck: {player_luck}")
    print(f"Player HP: {pc['stamina']} | Enemy HP: {enemy['stamina']}")
    while pc["stamina"] > 0 and enemy["stamina"] > 0:
        move = input("Hack, Firewall, or Flee? [default: hack]").lower() or "hack"
        if move == "hack":
            # Proceed to the attack phase
            player_attack = d6(0,2) + pc["skill"]
            enemy_attack = d6(0,2) + enemy["skill"]
            print(f"Your Roll: {player_attack} | Enemy roll: {enemy_attack}")
            if player_attack >= enemy_attack:
                print("You found a likely attack vector")
                enemy["stamina"] -= 2
            else:
                print("They've broken through a layer of proxies!")
                pc["stamina"] -= 2
        elif move == "firewall":
            print("You raise a firewall to defend yourself.")
            # Add any defensive logic here if needed
        elif move == "flee":
            print("You jack out of the system.")
            exit()
        else:
            print("Invalid move. Try again.")
            continue

        # Print updated health after each round
        print(f"Remaining HP: {pc['stamina']}")
        print(f"Enemy HP: {enemy['stamina']}")

        # Check for win/lose conditions
        if pc["stamina"] <= 0:
            print(f"{obstacle.skull}You died :(")
            exit()
        elif enemy["stamina"] <= 0:
            print("The last ICE shatters into a dozen dark blue polygons.\nThe recipe control config file presents itself adorned in gold rays, ripe for the taking.")
