#!/usr/bin/env python
def check_in_range(n):
    if n in range(3,319):
        print( " %s is in the range"%str(n))
        is_in_range = True
    else :
        print("The number is outside the given range.")
        is_in_range = False
    
    return is_in_range
