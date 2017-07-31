def is_leap(year):
    leap = False
    
    if year % 4 != 0: # not divisible by 4
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

    
    return leap