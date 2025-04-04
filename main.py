

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
    def testYourLuck(self):
        lucky = True
        d1 = d6()
        d2 = d6()
        result = d1 + d2
        if result <= self.luck:
            return lucky
        else:
            lucky = False
            return lucky


player = Player()
print(player)
print(player.testYourLuck())