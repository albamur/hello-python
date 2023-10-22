# ---------------------------------- VARIABLES ---------------------------------- 
# Las variables se utilizan para almacenar datos, cada variable tiene un nombre y almacena un valor.
# Python NO sigue la nomenclatura CamelCase
# Python SI sigue la nomenclatura snake_case (todo en minúscula y guiones bajos)

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

# my_int_to_str_variable = str(my_int_variable)
# print(my_int_to_str_variable)
# print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
# print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Alba", "Muñoz", 'albamur', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Alba"
print(name)
print(age)

# ¿Forzamos el tipo?
# Python es de tipado débil, aunque especifiquemos el tipo de dato este se puede sobrescribir
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

# ---------------------------------- CONVERSIÓN DE TIPOS ---------------------------------- 
# str()
# int()
# float()

# tuple()
# list()