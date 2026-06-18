def printBool(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printBool("):-1]
        print(bool(content))
