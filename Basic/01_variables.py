# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VARIABLES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
# Las variables se utilizan para almacenar datos, cada variable tiene un nombre y almacena un valor.

# ---------------------------------- NOMBRES ---------------------------------- 
# Reglas para nombrar variables en Python
# · Deben comenzar con una letra o un guion bajo (_).
# · Solo puede contener caracteres alfanuméricos y guiones bajos.
# · Son sensibles a mayúsculas y minúsculas (Case sensitive).
# · No pueden comenzar con un número.
# · No se pueden utilizar palabras clave reservadas de Python como nombres de variables (if, else, for, while, def, class...).

# Nomenclaturas
# · camelCase 
# . snake_case (todo en minúscula y guiones bajos)
# · PascalCase

# Declarar una variable entera
edad = 30
print(edad)

# Declarar una variable decimal
altura = 1.75
print(altura)

# Declarar una variable de cadena (string) con "",'', y en mayúsculas
nombre = "Juan"
nombre2 = 'Juan'
NOMBRE = "Gómez"
print(nombre)
print(nombre2)
print(NOMBRE)

# Declarar una variable booleana
es_estudiante = True
print(es_estudiante)


# ---------------------------------- ASIGNACIÓN MÚLTIPLE ---------------------------------- 
# ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Alba", "Muñoz", 'albamur', 35


# ---------------------------------- CONCATENACIÓN ---------------------------------- 
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)


# ---------------------------------- FORZAR EL TIPO ---------------------------------- 
# Python es de tipado débil, aunque especifiquemos el tipo de dato este se puede sobrescribir

# Cambiamos su tipo
name = 35
age = "Alba"
print(name)
print(age)

address: str = "Mi dirección" # Aunque se indique el tipo de variable sigue siendo modificables
address = True
address = 5
address = 1.2
print(type(address))


# ---------------------------------- VARIABLES GLOBALES ---------------------------------- 
# Son aquellas que se declaran fuera de cualquier función o bloque de código y pueden ser 
# accedidas y modificadas desde cualquier parte del programa, incluyendo funciones y 
# bloques de código dentro de funciones.
global x
x = 10