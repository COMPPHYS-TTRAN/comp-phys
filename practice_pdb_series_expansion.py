'''

	>>> L(1) - 0.69314718056 < 1e-6
	False

'''

import pdb
import math

def L(x, n = 100):
	if x <= -1:
        	print 'Error, x needs to be positive. Returning...'
		return 
	#pdb.set_trace()
	approx = 0
	for i in range(1, n):
		approx += (1./(i))*(x/(1.+x))**(i)
		if i == n-2:
			old_approx = approx 
	frac_error = (abs(approx - old_approx)/approx)*100
	if frac_error > 1e-6:
		print 'frac_error: ', frac_error
		print 'approx = ', approx, ',', 'But not within accuracy to the sixth digit'
		return approx



if __name__ == "__main__":
	import doctest
    	doctest.testmod()
	x = 1000
	y = L(x)
	print 'Series Approximation: ', y