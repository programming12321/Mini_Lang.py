def absVal(code):
    content = code[len("absVal("):-1]
    return abs(int(content))
