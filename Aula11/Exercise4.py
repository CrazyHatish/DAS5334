def any_lowercase1(s): #works
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s): #always returns 'True' since 'c'.islower() == True
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): #returns True if the last letter is lowercase, else returns False
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s): #works
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s): #returns False if any letter is not lowercase
    for c in s:
        if not c.islower():
            return False
    return True
