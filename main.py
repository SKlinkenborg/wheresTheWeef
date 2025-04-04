import random as r

def d6(modifier = 0, number = 1):
    result = number * r.randint(1, 6) + modifier
    return result





class Player:
    def __init__(self):
        self.skill = d6(6)
        self.stamina = d6(12,2)
        self.luck = d6(6)

    def __str__(self):
        string = f"Skill: {self.skill}\nStamina: {self.stamina}\nLuck: {self.luck}"
        return string
    
    '''
    A standard Fighting Fantasy concept is to be invited to Test your luck. This involves rolling two dice. 
    If the result is less than or equal to your current LUCK, you are "Lucky" and, presumably, better things will happen than if you'd been "Unlucky". 
    Whatever the outcome, you lose 1 LUCK point as part of this process.
    '''
    def testYourStat(self, stat):
        d1 = d6()
        d2 = d6()
        result = d1 + d2

        # Check if the provided stat exists and compare the result
        if hasattr(self, stat):
            current_stat = getattr(self, stat)
            if result <= current_stat:
                print(f"Test succeeded! Rolled {result} against {stat.upper()} ({current_stat}).")
                return True
            else:
                print(f"Test failed! Rolled {result} against {stat.upper()} ({current_stat}).")
                # Reduce the stat by 1 if the test fails
                if stat == "luck":
                    setattr(self, stat, current_stat - 1)
                    print(f"Oof lost a luck point.\nCurrent Luck: {self.luck}")
                return False
        else:
            raise ValueError(f"Invalid stat: {stat}. Valid stats are 'skill', 'stamina', or 'luck'.")
        
    '''

    '''


player = Player()
print(player)
print(player.testYourStat("luck"))