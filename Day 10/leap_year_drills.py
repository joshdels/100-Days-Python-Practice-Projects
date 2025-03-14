def is_leap_year(year):
    '''
    This is a leap year generator
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else: 
            return False
    else:
        return False
        
                
    # Write your code here. 
    # Don't change the function name.

print(is_leap_year(2100))