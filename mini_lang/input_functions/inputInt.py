def inputInt(code):
    content = code[len("inputInt("):-1]
    return int(input(content))
