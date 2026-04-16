def tokenize(cadena):
    return cadena.replace("(", " ( ").replace(")", " ) ")\
                 .replace("{", " { ").replace("}", " } ")\
                 .replace("=", " = ").replace(";", " ; ").split()
