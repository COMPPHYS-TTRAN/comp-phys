‘’’
>>> x_int(1, 1)
1.0
>>> x_int(2, 1)
1.0
>>> x_other(1.5, 1, 1e-4)
0.8862269
>>> x_other(2.5, 1, 1e-4)
1.3293403

‘’’




import math
from math import factorial 
import pdb
    
def x_int(t, dx): 
    #pdb.set_trace()
    gamma = math.factorial(t-1)
    return gamma

def x_other(t, dx, tol):
    #pdb.set_trace()
    start = 0
    stop = 1000
    
    mdpoints = []
    x = start
   
    while x < stop:
        mdpoints.append((2.0*x + dx)/2)
        x += 1
        
    x_of_gamma = 0
    for x in mdpoints:
        x_of_gamma += x**(t-1.)*math.exp(-x)
        gamma = x_of_gamma*dx
        
        if x == len(mdpoints)-2:
            prev_gamma = gamma
	frac_diff = (abs(gamma - prev_gamma)/gamma)*100
	while frac_diff > tol:
            dx = dx/2.
            x_other(t, dx, tol)
                
    return gamma

def calculate_gamma(t, dx):
    tol = input('Enter desired tolerance: ')
    if t < 0 or t > 100:
        print 'Invalid t. Please enter t value from 1 to 100. '
        
    else:
        if type(t) == int:
            return x_int(t, dx)
        else:
            return x_other(t, dx, tol)

if __name__ == “main__”:
    import doctest
    import argparse
    doctest.testmod()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type = float, ‘-dx’, type = float)
    args = parser.parse_args()
    x = args.x
    dx = args.dx