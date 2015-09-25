'''
#HW03
#Terry Tran
#Partner: Jacob Baca

>>> prime(33, 101)
[37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
>>> prime(1, 10)
[2, 3, 5, 7]

'''

import numpy as np 
import pdb

def prime(a, b):

    #pdb.set_trace()
    numbers = np.arange(a, b+1, 1)
    digits = np.arange(1, b+1, 1)
    prime_list = []
    for n in numbers:
        count = 0
        for d in digits:
            remain = n % d
            if remain == 0: #the remainder is zero when the number is 						#perfectly divisible
                            #prime number is only perfectly divisible twice
                count += 1
        if count == 2:
            prime_list.append(n)
    return prime_list     
        

if __name__ == "__main__":
    import doctest
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type = int)
    parser.add_argument('-b', type = int)
    args = parser.parse_args()
    a = args.a
    b = args.b
    
    print prime(a, b)