# Mini crud no relacional

Vamos a ver un mini base de datos donde tenemos las operaciones de un CRUD.

## Funcionalidades

El lenguaje soporta operaciones básicas:

* `INSERT` → Insertar documentos en una colección
* `FIND` → Consultar colecciones
* `UPDATE` → Actualizar registros por condición
* `DELETE` → Eliminar registros por condición

## Ejemplo de uso

```txt
INSERT usuarios {nombre:"Samuel", edad:20}
FIND usuarios
UPDATE usuarios SET edad:21 WHERE nombre="Samuel"
DELETE usuarios WHERE edad=20
```


## Ejecución

```bash
antlr4 -Dlanguage=Python3 CRUD.g4
python3 main.py
```
