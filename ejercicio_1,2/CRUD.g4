grammar CRUD;

programa
    : sentencia+ EOF
    ;

sentencia
    : insertar
    | consultar
    | actualizar
    | eliminar
    ;

insertar
    : INSERT ID '{' atributo (',' atributo)* '}'
    ;

consultar
    : FIND ID donde?
    ;

actualizar
    : UPDATE ID SET atributo donde?
    ;

eliminar
    : DELETE ID donde?
    ;

donde
    : WHERE ID '=' VALOR
    ;

atributo
    : ID ':' VALOR
    ;

INSERT : 'INSERT';
FIND   : 'FIND';
UPDATE : 'UPDATE';
DELETE : 'DELETE';
SET    : 'SET';
WHERE  : 'WHERE';

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

VALOR
    : '"' ~["\r\n]* '"'
    | [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
