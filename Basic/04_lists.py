# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LISTAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
# Son una estructura de datos que permite almacenar y organizar múltiples elementos en una secuencia ordenada.
# Las listas son objetos mutables, lo que significa que se pueden modificar agregando, eliminando o modificando 
# elementos después de su creación.


# ---------------------------------- DEFINICIÓN ---------------------------------- 

# Crear una lista vacía
mi_lista_vacia = []

# Crear una lista con elementos
frutas = ["manzana", "banana", "cereza", "uva"]

# Crear una lista con diferentes tipos de datos
mi_lista_mixta = [1, "Hola", True, 3.14]

# Crear una lista de números del 1 al 5 usando una comprensión de lista
numeros = [x for x in range(1, 6)]

# Crear una lista de cadenas utilizando el método split() en una cadena
mi_cadena = "Este es un ejemplo de cadena"
palabras = mi_cadena.split()

# Crear una lista de números pares utilizando un bucle for
numeros_pares = []
for i in range(2, 11, 2):
    numeros_pares.append(i)

# Crear una lista de listas (una lista de listas de números)
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Imprimir las listas creadas
print("Lista vacía:", mi_lista_vacia)
print("Lista de frutas:", frutas)
print("Lista mixta:", mi_lista_mixta)
print("Números del 1 al 5:", numeros)
print("Palabras en la cadena:", palabras)
print("Números pares del 2 al 10:", numeros_pares)
print("Lista de listas:", lista_de_listas)



# ---------------------------------- CARACTERÍSTICAS DE LAS LISTAS ---------------------------------- 

# Ordenadas: 
# Los elementos en una lista tienen un orden específico y se mantienen en el orden en el que fueron agregados. 
# Esto significa que podemos acceder a los elementos de una lista en función de su posición.


# Indexadas: 
# Cada elemento en una lista tiene un índice asociado que representa su posición en la lista. 
# Los índices comienzan desde 0 para el primer elemento, 1 para el segundo elemento, y así sucesivamente.


# Mutables: 
# Las listas son mutables, lo que significa que podemos cambiar, agregar o eliminar elementos después 
# de que la lista ha sido creada. Podemos modificar elementos individuales, agregar nuevos elementos 
# al final de la lista o eliminar elementos existentes.


# Permiten duplicados: Las listas pueden contener elementos duplicados, es decir, elementos con el mismo valor 
# pueden aparecer varias veces en la lista.


# Pueden contener diferentes tipos de datos: 
# Una lista puede contener elementos de diferentes tipos de datos, 
# como números, cadenas, booleanos, otras listas e incluso objetos más complejos.


# Tamaño dinámico: 
# No es necesario especificar un tamaño fijo para una lista al crearla. Podemos agregar o eliminar
# elementos según sea necesario, lo que hace que las listas sean muy flexibles.


# ---------------------------------- ACCEDER A SUS ELEMENTOS ---------------------------------- 

frutas = ["manzana", "naranja", "plátano", "pera", "fresa"]

# Acceder al segundo elemento (índice 1)
print(frutas[1])  # Salida: 'naranja' (segundo elemento)

# Acceso a elementos desde el final con índices negativos
print(frutas[-1])  # Salida: 'fresa' (último elemento)
print(frutas[-2])  # Salida: 'pera' (segundo elemento desde el final)

# Acceso a un rango de elementos usando slicing: el segundo indice es exclusivo
print(frutas[1:4])  # Salida: "naranja", "plátano", "pera" 
print(frutas[0:3])  # Salida: "manzana", "naranja", "plátano"


# ---------------------------------- CAMBIAR LOS VALORES ---------------------------------- 

## Cambiar un único valor ##

# Cambiar el segundo elemento (índice 1) a "kiwi"
frutas[1] = "kiwi"

print(frutas)  # Salida: ["manzana", "kiwi", "plátano", "pera", "fresa"]


## Cambiar un rango ##

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Cambiar los elementos de índice 0 a 3 (exclusivo) a [10, 20, 30]
numeros[0:3] = [10, 20, 30]

print(numeros)  # Salida: [10, 20, 30, 4, 5]


## Insertar elementos ##

# Insertar "pera" en el índice 1
frutas.insert(1, "pera")

print(frutas)  # Salida: ['manzana', 'pera', 'banana', 'naranja']


# ---------------------------------- AGREGAR ELEMENTOS ---------------------------------- 

# Lista de números
numeros = [1, 2, 3]
print("Lista inicial:", numeros)

# Agregar un nuevo número al final de la lista usando 'append()'
numeros.append(4)
print("Después de agregar un elemento al final:", numeros)

# Insertar un nuevo número en la posición 1 (índice 1) usando 'insert()'
numeros.insert(1, 5)
print("Después de insertar un elemento en la posición 1:", numeros)

# Extender la lista con otra lista usando 'extend()'
otra_lista = [6, 7]
numeros.extend(otra_lista)
print("Después de extender la lista con otra lista:", numeros)

# Agregar otros iterables a la lista 'numeros'

# Lista de números
numeros = [1, 2, 3]
otra_lista = [4, 5]
una_tupla = (6, 7)
una_cadena = "hola"

numeros.extend(otra_lista)
numeros.extend(una_tupla)
numeros.append(una_cadena)

print(numeros)  # Salida: [1, 2, 3, 4, 5, 6, 7, 'hola']


# ---------------------------------- BORRAR ELEMENTOS ---------------------------------- 

# Por su valor: Remove() #

colores = ["rojo", "verde", "azul", "amarillo", "verde"]

# Eliminar el elemento "verde" de la lista
colores.remove("verde")

print(colores)  # Salida: ['rojo', 'azul', 'amarillo', 'verde']


# Por su indice: Pop() #
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Eliminar el elemento en el índice 2 (valor 3)
elemento_eliminado = numeros.pop(2)

print(numeros)  # Salida: [1, 2, 4, 5]
print("Elemento eliminado:", elemento_eliminado)  # Salida: 3


# Borrar una lista entera: Clear() #
# Lista de letras
letras = ['a', 'b', 'c']

# Borrar la lista
letras.clear()

print(letras)  # Salida: []

# ---------------------------------- ELIMINAR ELEMENTOS ---------------------------------- 
# Ejemplo: Eliminar elementos de una lista usando del

frutas = ["manzana", "banana", "naranja", "kiwi"]

# Eliminar el elemento en el índice 1 (banana)
del frutas[1]
print(frutas)  # Salida: ['manzana', 'naranja', 'kiwi']

# También se puede eliminar un rango de elementos usando slicing
del frutas[0:2]
print(frutas)  # Salida: ['kiwi']

# Eliminar el último elemento de la lista
del frutas[-1]
print(frutas)  # Salida: []

# También se puede usar del para eliminar la lista completa
del frutas
# Al imprimir frutas aquí generará un error ya que la lista ha sido eliminada


# ---------------------------------- RECORRER UNA LISTA ---------------------------------- 

# Bucle for
frutas = ["manzana", "banana", "naranja", "uva"]

# Recorrer la lista e imprimir cada fruta
for fruta in frutas:
    print(fruta)

# Salida:
# manzana
# banana
# naranja
# uva

# Bucle a través de los números de índice (for con range())
frutas = ["manzana", "banana", "naranja", "uva"]

# Recorrer la lista y mostrar el elemento con su índice
for indice in range(len(frutas)):
    print("En el índice", indice, "se encuentra", frutas[indice])

# Salida:
# En el índice 0 se encuentra manzana
# En el índice 1 se encuentra banana
# En el índice 2 se encuentra naranja
# En el índice 3 se encuentra uva






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


# REPASAR LA ASIGNACIÓN MULTIPLE