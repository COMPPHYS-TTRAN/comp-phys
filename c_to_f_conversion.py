"""	
>>> conversion(0)
32.0

To run doctests in verbose mode:
python -m doctest -v c_to_f_conversion.py

"""
import argparse

def conversion(Cel):
	
	F = Cel * (9./5.) + 32
	return F

if __name__ == "__main__":
    import doctest
    #doctest.testmod()

    #instantiate an object of the class argparse.ArumentParser()
    parser = argparse.ArgumentParser() 
    #Reading argument from command line by invoking the method add_argument()
    parser.add_argument('-x', type = float)
    
    args = parser.parse_args()
    x = args.x

    print conversion(x) #allows user to input from terminal command line
