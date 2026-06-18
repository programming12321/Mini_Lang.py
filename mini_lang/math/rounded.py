def rounded(code):
    content = code[len("rounded("):-1]
    return round(int(content))
