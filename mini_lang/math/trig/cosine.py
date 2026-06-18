from math import *

def cosine(code):
    content = code[len("cosine("):-1]
    return cos(int(content))
