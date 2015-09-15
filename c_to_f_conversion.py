“””
	#!/usr/bin/python
	>>>conversion(1)
	33.8

“””

def conversion(C):
	
	F = C * (9./5.) + 32
	return F

if __name__ == "__main__":
    import doctest
    doctest.testmod()
