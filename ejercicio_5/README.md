# Analizador descendente recursivo

## ¿Qué se hizo?

Se implementó un analizador descendente recursivo en Python que permite validar si una cadena cumple con una gramática simple.
El programa revisa paso a paso los tokens usando una función de emparejamiento (`match`).

---

## ¿Qué gramática se utilizó?

La gramática utilizada fue:

S → A | C
A → id = E ;
C → if ( E ) { A }
E → id | num

Esta gramática permite reconocer asignaciones y estructuras condicionales simples.

---

## ¿Cómo funciona el algoritmo?

El analizador funciona con funciones recursivas, donde cada función representa una regla de la gramática.

La función más importante es `match`, que verifica si el token actual es el esperado:

* Si coincide, avanza al siguiente token
* Si no coincide, genera un error

También se usa una función `avanzar()` para moverse en la lista de tokens.

---

## ¿Cómo se ejecuta?

En la terminal de Linux:

python3 main.py

---

## Ejemplos de entrada válidos

x = 5 ;
if ( x ) { y = 3 ; }

---

## Ejemplos de entrada inválidos

x = 5
if x { y = 3 ; }

---

## Conclusión

El analizador permite validar estructuras básicas usando una gramática independiente del contexto.
Se comprobó cómo funciona el parsing descendente recursivo y el uso del emparejamiento de tokens.

