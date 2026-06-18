def printComplex(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printComplex("):-1]
        print(complex(content))
