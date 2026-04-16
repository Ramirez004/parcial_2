
# Parser CYK para Calculadora

Se implementó un parser utilizando el algoritmo **CYK** para reconocer expresiones aritméticas simples de una calculadora, junto con un parser predictivo para comparar su rendimiento.

La gramática utilizada para las expresiones fue:

```txt
E -> E + T | T
T -> T * F | F
F -> ( E ) | num
````

Ambos parsers procesan expresiones como:

```txt
1+1+1+1+1
```

El parser CYK fue implementado mediante tabla dinámica siguiendo el algoritmo CYK, mientras que el parser predictivo se desarrolló con análisis recursivo descendente.

## Comparación de tiempos

| Tamaño de Entrada | CYK (s)  | Predictivo (s) |
| ----------------- | -------- | -------------- |
| 39 caracteres     | 0.003124 | 0.000024       |
| 79 caracteres     | 0.022766 | 0.000038       |
| 119 caracteres    | 0.071808 | 0.000043       |
| 159 caracteres    | 0.176604 | 0.000052       |

## Comparación

Se observa que el parser CYK tarda más tiempo en procesar las expresiones conforme aumenta el tamaño de la entrada, mientras que el parser predictivo mantiene tiempos considerablemente menores.

## Conclusión

El parser predictivo presenta mejor rendimiento que el algoritmo CYK para este tipo de expresiones, ya que CYK requiere más operaciones al analizar la entrada.
