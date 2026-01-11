import sys
import argparse


parser = argparse.ArgumentParser(description="print neows ")
parser.add_argiment_args("-n", help="number of times to to miew")
args = parser.parse_args()






"""
if len(sys.argv) == 1:
    n = 1

if len(sys.argv) == 3 and sys.argv[1] == "-n":
    n= sys.argv[2]
    
else:
    n = sys.argv[1]


def meow(n: int) -> str:
    Meow n times

    Args:
        n (int): times should meow
    Raise TypeError: If n is not an int

    Returns:
        str: meows n times separated by \n 

    
    return "meow\n" * n 
        

meows: str = meow(int(n))
print(meows, end="")

"""
