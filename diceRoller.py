import numpy as np

def basicRoll(num_dice, die_size):
    rolls = np.arange(num_dice)
    for ii in range(num_dice):
        try:
            rolls[ii] = (np.random.randint(die_size)+1)
        except:
            if die_size == "f" or die_size == "F":
                rolls[ii] = (np.random.randint(3)-1)
    return [sum(rolls), rolls]