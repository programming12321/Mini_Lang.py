def printString(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printString("):-1]
        print(str(content))
