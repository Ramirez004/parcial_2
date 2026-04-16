tokens = []
pos = 0
token_actual = None

def init_parser(t):
    global tokens, pos, token_actual
    tokens = t
    pos = 0
    token_actual = tokens[pos]

def avanzar():
    global pos, token_actual
    pos += 1
    if pos < len(tokens):
        token_actual = tokens[pos]

def error():
    raise Exception("Error de sintaxis")

def match(token_esperado):
    global token_actual
    if token_actual == token_esperado:
        avanzar()
    else:
        error()

# Gramática

def S():
    if token_actual.isalpha():
        A()
    elif token_actual == "if":
        C()
    else:
        error()

def A():
    match(token_actual)  # id
    match("=")
    E()
    match(";")

def C():
    match("if")
    match("(")
    E()
    match(")")
    match("{")
    A()
    match("}")

def E():
    if token_actual.isalpha() or token_actual.isnumeric():
        match(token_actual)
    else:
        error()
