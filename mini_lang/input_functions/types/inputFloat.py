def inputFloat(code):
    content = code[len("inputFloat("):-1]
    return float(input(content))
