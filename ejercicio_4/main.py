import time

# Parser Predictivo

def parser_predictivo(expresion):
    i = 0

    def E():
        nonlocal i
        if i < len(expresion) and expresion[i].isdigit():
            i += 1
            while i < len(expresion) and expresion[i] == '+':
                i += 1
                if i < len(expresion) and expresion[i].isdigit():
                    i += 1
                else:
                    raise SyntaxError
        else:
            raise SyntaxError

    try:
        E()
        return i == len(expresion)
    except:
        return False

# CYK
def parser_cyk(expresion):
    tokens = list(expresion.replace(" ", ""))
    n = len(tokens)

    tabla = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if tokens[i].isdigit():
            tabla[i][i].add("NUM")
            tabla[i][i].add("E")
        elif tokens[i] == '+':
            tabla[i][i].add("PLUS")

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                izq = tabla[i][k]
                der = tabla[k + 1][j]

                if "PLUS" in izq and "NUM" in der:
                    tabla[i][j].add("PLUSNUM")

                if "E" in izq and "PLUSNUM" in der:
                    tabla[i][j].add("E")

    return "E" in tabla[0][n - 1]

# Pruebas

expresiones = [
    "+".join(["1"] * 20),
    "+".join(["1"] * 40),
    "+".join(["1"] * 60),
    "+".join(["1"] * 80)
]

print("Comparación de rendimiento:\n")

for exp in expresiones:
    inicio = time.perf_counter()
    parser_cyk(exp)
    tiempo_cyk = time.perf_counter() - inicio

    inicio = time.perf_counter()
    parser_predictivo(exp)
    tiempo_pred = time.perf_counter() - inicio

    print(f"Tamaño: {len(exp)} caracteres")
    print(f"CYK: {tiempo_cyk:.8f} s")
    print(f"Predictivo: {tiempo_pred:.8f} s")
    print("-" * 40)
