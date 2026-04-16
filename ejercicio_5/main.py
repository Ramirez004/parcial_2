from lexer import tokenize
from parser import S, init_parser

entrada = "x = 5 ;"

tokens = tokenize(entrada)

init_parser(tokens)
S()

print("Cadena válida")
