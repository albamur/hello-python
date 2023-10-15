### Lists ###

#El array en una estructura mas inamovible
# Una lista es un conjunto de un array que nos permite aplicarle funciones propias de las listas

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Alba", "Muñoz"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0]) # Primero
print(my_other_list[1]) # Segundo
print(my_other_list[-1]) # Primero por atrás
print(my_other_list[-4]) # Cuarto por atrás
print(my_list.count(30)) # Cuenta los elementos 30 de la lista 
# print(my_other_list[4]) IndexError: fuera del rango
# print(my_other_list[-5]) IndexError: fuera del rango

print(my_other_list.index("Alba"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list) Error: No se puede hacer

# Creación, inserción, actualización y eliminación

my_other_list.append("albamur")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

#  Constantes: en Python no existen por su tipado dinámico
# Para dar a entender que una variable se quiere tratar como una constante se puede declarar con mayúsculas

CONST_NAME = ""

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))