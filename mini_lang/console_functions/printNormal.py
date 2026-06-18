def run_printNormal(code):
    if not code.endswith(")"):
        print("SyntaxError: missing parenthesis")
    else:
        content = code[len("printNormal("):-1]
        print(content)
