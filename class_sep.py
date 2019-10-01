from random import randint

def seperate_random(division_num, min_num=0, names=None, *things):
    '''
    Splits the things in tuple 'things' into multiple lists at random. Returns a dictionary of lists.
    A "min_num" argument specifies the minimum number of things in each list, unless the number
    of things needed is greater than those provided. "names" allows users to specify the list entries
    in the returned dictionary, with names being unused or numbers added as necessary.
    
    >>>seperate_random(3, 0, None, 'foo', 'fi', 'fy', 'fum', 'shrek')
    {0: [], 1: ['foo', 'fy'], 2: ['fi', 'fum', 'shrek']}
    
    >>>seperate_random(3, 2, None, 'foo', 'oof', 'ofo', 'fof', 'ooo', 'fff')
    {0: ['ooo', 'oof'], 1: ['ofo', 'foo'], 2: ['fof', 'fff']}

    >>>seperate_random(4, 1, ['Period 1', 'Period 2', 'Period 3',], 'James', 'Eric', 'Marie', 'Oliver', 'Grace', 'John')
    Names given do not match up with divisions. Extra numbers may be used or names n
    ot used. Continue? (y/n)y
    {'Period 1': ['Grace', 'John'], 'Period 2': ['Eric'], 'Period 3': ['Marie'], 1:
    ['James', 'Oliver']}
    '''
    
    num = 0
    if (division_num*min_num) > len(things):
        return "There are not enough numbers to satisfy the number of divisions \
    and the minimum number of things in each division. Please check your inputs."
    if names != None:
        try:
            x = len(names)
        except TypeError:
            raise Exception("Names given were not in tuple/list form")
        if len(names) != division_num:
            while True:
                continueon = input('Names given do not match up with divisions. Extra numbers may be used or names not used. Continue? (y/n)')
                if continueon == 'n':
                    raise KeyboardInterrupt
                elif continueon == 'y':
                    break
                else:
                    pass
            
    seperations = {}
    while num <= division_num-1:
        command = 'list' + str(num) + ' = []'
        exec(command)
        num += 1
    
    num = 0
    things = list(things)
    while num <= division_num-1:
        x = 0
        while x < min_num:
            yes = len(things)-1
            which = randint(0, yes)
            addition = things.pop(which)
            command = 'list' + str(num) + '.append(addition)'
            exec(command)
            x += 1
        num += 1
    for thing in things:
        which = randint(0, division_num-1)
        command = 'list' + str(which) + '.append(thing)'
        exec(command)
            
    num = 0
    if names:
        while num <= division_num-1:
            if len(names) >= division_num:
                sep = 'list' + str(num)
                command = 'seperations[names[num]] = list' + str(num)
                exec(command)
            else:
                if num >= len(names):
                    command = 'seperations[(num - (len(names)-1))] = list' + str(num)
                    exec(command)
                else:
                    command = 'seperations[names[num]] = list' + str(num)
                    exec(command)
            num += 1
    else:
        while num <= division_num-1:
            sep = 'list' + str(num)
            command = 'seperations[num] = list' + str(num)
            exec(command)
            num += 1
    return seperations

def divide(division_num, names=None, *things):
    pass
        
    

yes = seperate_random(3, 0, None, 'foo', 'fi', 'fy', 'fum', 'shrek')
print(yes)
