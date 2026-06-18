def printFloat(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printFloat("):-1]
        print(float(content))
