def printInt(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printInt("):-1]
        print(int(content))
