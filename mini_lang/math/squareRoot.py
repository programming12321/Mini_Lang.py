from math import *

def squareRoot(code):
    content = code[len("squareRoot("):-1]
    return sqrt(int(content))
