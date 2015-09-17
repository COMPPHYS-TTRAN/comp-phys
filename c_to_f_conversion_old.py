"""	
>>> conversion(1)
	33.8

To run doctests in verbose mode:
python -m doctest -v c_to_f_conversion.py

“””

def conversion(C):
	
	F = C * (9./5.) + 32
	return F

if __name__ == "__main__":
    import doctest
    #doctest.testmod()
