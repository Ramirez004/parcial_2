from antlr4 import *
from CRUDLexer import CRUDLexer
from CRUDParser import CRUDParser

def analizar_entrada(texto):
    entrada = InputStream(texto)

    lexer = CRUDLexer(entrada)
    tokens = CommonTokenStream(lexer)

    parser = CRUDParser(tokens)

    arbol = parser.programa()

    print("Entrada válida")
    print(arbol.toStringTree(recog=parser))


if __name__ == "__main__":
    texto_prueba = """
    INSERT usuarios {nombre:"Samuel", edad:20}
    FIND usuarios   
    FIND usuarios WHERE edad=20
    UPDATE usuarios SET edad:21 WHERE nombre="Samuel"
    DELETE usuarios WHERE edad=20
"""
   

    analizar_entrada(texto_prueba)
