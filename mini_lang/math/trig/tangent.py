from math import *

def tangent(code):
    content = code[len("tangent("):-1]
    return tan(int(content))
