from math import *

def sine(code):
    content = code[len("sine("):-1]
    return sin(int(content))
