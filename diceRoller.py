import numpy as np

def basicRoll(num_dice, die_size):
    '''
    `num_dice`
        The number of dice to be rolled
    `die_size`
        The number of sides on the die to be rolled, (e.g. 4, 6, 20, 7)
        "f" or "F" are also valid sizes for fudge dice

    EX:
    To roll 2d6, num_dice = 2 and die_size = 6. 
    '''

    rolls = np.arange(num_dice)
    for ii in range(num_dice):
        try:
            rolls[ii] = (np.random.randint(die_size)+1)
        except:
            if die_size == "f" or die_size == "F":
                rolls[ii] = (np.random.randint(3)-1)
    
    return sum(rolls),rolls
    

def advancedRoll(num_dice, die_size, **kwargs):
    '''
    Optional arguments
    `keepHighest`
        Either a boolean, or an integer number of dice to keep.
    `keepLowest`
        Either a boolean, or an integer number of dice to keep.
    '''

    if len(kwargs) > 1:
        raise Exception("Too many keyword arguments. Only one is allowed")

    '''
    The rest of the program is composed of try/except statements to handle any optional arguments.
    If there are no optional arguments, the roller is done and the result is simply the sum of all rolls. 
    Otherwise, the result will depend on the various optional arguments.
    '''

    result, rolls = basicRoll(num_dice,die_size)

    # parse any kwargs and assign them to internal variables
    for key, value in kwargs.items():
        if key == "keepHighest":
            keepHighest = value
        elif key == "keepLowest":
            keepLowest = value
        else:
            print("Unknown keyword: ", key)

    try:
        if keepHighest>0: 
            rollsTemp = rolls
            highest_rolls = rollsTemp[np.argsort(rollsTemp)[-keepHighest:]]
            result = sum(highest_rolls)
        elif keepHighest<0:
            raise Exception("`keepHighest` must be greater than 0.")
    except NameError:
        pass

    try:
        if keepLowest>0: 
            rollsTemp = rolls
            lowest_rolls = rollsTemp[np.argsort(rollsTemp)[:keepLowest]]
            result = sum(lowest_rolls)
        elif keepLowest<0:
            raise Exception("`keepHighest` must be greater than 0.")
    except NameError:
        pass

    try:
        rerollOnce
        # for ii in range(len(a)):
        #     if a[ii] == 1:
        #         a.append(6)

    except NameError:
        pass
        
    try:
        reroll
        # while a[ii] is not None:
        #     if a[ii] == 1:
        #         a.append(6)
        #     ii +=1
        # throws an indexing error at the last index
    except NameError:
        pass

    return [result, rolls]
