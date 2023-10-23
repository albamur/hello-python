# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STRINGS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

# ---------------------------------- ASIGNACIÓN ---------------------------------- 
my_string = "Mi String"
my_other_string = 'Mi otro String'

# ---------------------------------- POSICIONES ---------------------------------- 
# En Python, las cadenas son tratadas como matrices de caracteres. 
# Esto significa que cada carácter en la cadena tiene un índice numérico que indica su posición
print(my_string[0])  # Salida: 'M'
print(my_string[3])  # Salida: 'S'

# ---------------------------------- FUNCIÓN LEN() ---------------------------------- 
# Se utiliza para obtener la longitud de una cadena, es decir, la cantidad de caracteres que contiene.

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)


# ---------------------------------- DIVISIÓN O SLICING DE CADENAS ---------------------------------- 
# El slicing es una técnica que nos permite extraer subcadenas de una cadena más grande. 
# Esto se logra especificando un rango de índices que representan los límites de la subcadena que deseamos extraer.

language = "Python"

# Desde el principio
principio = language[0:3] # Salida : Pyth
print(principio)

# Hasta el final
final = language[1:]  # Salida : ython
print(final)

ultimo_char = language[-1]
print(ultimo_char)

language_slice = language[0:6:2]
print(language_slice)


# Reverse
reversed_language = language[::-1]
print(reversed_language)




# ---------------------------------- Desempaquetado de caracteres ----------------------------------
a, b, c, d, e, f = language
print(a)
print(e)



# ---------------------------------- CARACTERES DE ESCAPE ---------------------------------- 
my_new_line_string = "Este es un String\ncon salto de línea"  # Nueva línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"    # Tabulación
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"   # Barra lateral
print(my_scape_string)

my_scape_string = "\"Este es un String \" escapado" # Comillas
print(my_scape_string)

my_scape_string = "\u00A9Este es un String \U0001F604 escapado" # Carácter Unicode
print(my_scape_string)

my_scape_raw = r"C:\Directorio\Archivo" # Obvia los caracteres de escape


# ---------------------------------- MODIFICAR CADENAS ---------------------------------- 
# Mayúsculas y minúsculas
texto = "Hola, Mundo!"
mayúsculas = texto.upper()  # Convierte a mayúsculas
minúsculas = texto.lower()  # Convierte a minúsculas
print(mayúsculas)
print(minúsculas)

# Eliminar espacios en blanco
cadena = "   ¡Hola, Mundo!   "
sin_espacios = cadena.strip()  # Elimina espacios en ambos extremos

print(sin_espacios)

# Reemplazar cadena
a =  "Hola Mundo"
print(a.replace( "O", "M"))

# Dividir cadenas en subcadenas
a =  "Hola Mundo"
print(a.split(",")) # Devuelve ['Hola', ' Mundo']



# ---------------------------------- CONCATENACIÓN DE CADENAS ---------------------------------- 

# Operador +
cadena1 = "Hola"
cadena2 = ", Mundo!"
concatenada = cadena1 + cadena2

print(concatenada)


# Format()
nombre = "Alice"
edad = 30
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)

print(mensaje)


# F-Strings
producto = "manzanas"
cantidad = 10
precio_unitario = 1.5
total = cantidad * precio_unitario

mensaje = f"Compraste {cantidad} {producto} a {precio_unitario} cada una."

print(mensaje)


# Join()

palabras = ["Hola", "a", "todos"]
frase = " ".join(palabras)

print(frase)



# ---------------------------------- FUNCIONES DEL SISTEMA ---------------------------------- 

print("Cadena") # Muestra en pantalla un valor (texto o valores).
len("Cadena") # Cuenta el número de caracteres de una cadena de entrada y devolver su valor.
#replace() # Permite sustituir caracteres dentro de una cadena.
str(78) # Devuelve la representación de cadena de un número.
ord("a") # Muestra el valor ASCII de una cadena de un carácter determinado.
input("¿?") # Entrada de datos por parte de un usuario a través de la consola.
chr(97) # Devuelve la cadena correspondiente a un número entero en relación con el código Unicode (por ejemplo, chr(97) devuelve la cadena “a”.


# Formateo

name, surname, age = "Alba", "Muñoz", 22
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Funciones del lenguaje

print(language.capitalize())    # Pone primera letra en mayúscula
print(language.upper())         # Pone todas las letras en mayúsculas
print(language.count("t"))      # Cuenta cuantas "t" hay en la cadena de texto
print(language.isnumeric())     # Boolean si es un numero o no
print("1".isnumeric())
print(language.lower())         # Pone primera letra en minúscula
print(language.lower().isupper())   # Comprueba si  está en mayúsculas
print(language.startswith("Py"))    # Comprueba si la cadena empieza por "Py"
print(language.replace("y","."))    # Remplaza la y por un .
print(language.find("y"))    # Devuelve la posición de lo encontrado
print("Py" == "py")  # No es lo mismo

print(language.capitalize())        # Pone primera letra en mayúscula
print(language.casefold())          # Devuelve el texto en minúsculas de manera mas agresiva pues haya algunos caracteres que lower no contempla
print(language.center("20", "-"))   # Alinea la cadena en el centro, utilizando un carácter específico como carácter de relleno.
print(language.count("t"))          # Cuenta cuantas "t" hay en la cadena de texto
print(language.encode())            # Codifica la cadena utilizando la codificación especificada. Por defecto se utilizará UTF-8.
print(language.endswith("."))       # Comprueba si la cadena termina con (.):
print(language.expandtabs())        # NO SE USA NUNCA: Reemplaza '\t' con espacios en blanco hasta la siguiente tabulación. 
print(language.find("y"))           # Devuelve la posición de lo encontrado
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # Formatea los valores especificados y los inserta dentro del marcador de posición de la cadena.

# format_map() : Similar al método format(), pero en lugar de pasar argumentos como pares de valores clave, toma un diccionario como su argumento y utiliza las claves del diccionario para reemplazar las llaves en la cadena
# Definir un diccionario con valores para formatear
valores = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Ciudad XYZ'
}

# Cadena con marcadores de posición
cadena = "Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}."

# Imprimir la cadena formateada
print(cadena.format_map(valores))


"""
# capitalize()	    Convierte el primer carácter a mayúsculas
# casefold()	        Convierte cadena en minúsculas
# center()	        Devuelve una cadena centrada
count()	            Devuelve el número de veces que aparece un valor especificado en una cadena
encode()	        Devuelve una versión codificada de la cadena.
endswith()	        Devuelve verdadero si la cadena termina con el valor especificado
expandtabs()	    - Establece el tamaño de pestaña de la cadena. - 
find()	            Busca en la cadena un valor específico y devuelve la posición donde se encontró
format()	        Formatea valores especificados en una cadena
format_map()	    Formatea valores especificados en una cadena tomando un diccionario como su argumento y utiliza las claves del diccionario para reemplazar las llaves en la cadena
index()	            Busca en la cadena un valor específico y devuelve la posición donde se encontró
isalnum()	        Devuelve True si todos los caracteres de la cadena son alfanuméricos
isalpha()	        Devuelve True si todos los caracteres de la cadena están en el alfabeto
isascii()	        Devuelve True si todos los caracteres de la cadena son caracteres ASCII
isdecimal()	        Devuelve True si todos los caracteres de la cadena son decimales
isdigit()	        Devuelve True si todos los caracteres de la cadena son dígitos
isidentifier()	    Devuelve True si la cadena es un identificador
islower()	        Devuelve True si todos los caracteres de la cadena están en minúsculas
isnumeric()	        Devuelve True si todos los caracteres de la cadena son numéricos
isprintable()	    Devuelve True si todos los caracteres de la cadena son imprimibles
isspace()	        Devuelve True si todos los caracteres de la cadena son espacios en blanco
istitle()	        Devuelve True si la cadena sigue las reglas de un título
isupper()	        Devuelve True si todos los caracteres de la cadena están en mayúsculas
join()	            Convierte los elementos de un iterable en una cadena
ljust()	            Devuelve una versión justificada a la izquierda de la cadena.
lower()	            Convierte una cadena en minúsculas
lstrip()	        Devuelve una versión recortada a la izquierda de la cadena.
maketrans()	        Devuelve una tabla de traducción para ser utilizada en las traducciones.
partition()	        Devuelve una tupla donde la cadena se divide en tres partes
replace()	        Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
rfind()	            Busca en la cadena un valor específico y devuelve la última posición donde se encontró
rindex()	        Busca en la cadena un valor específico y devuelve la última posición donde se encontró
rjust()	            Devuelve una versión justificada a la derecha de la cadena.
rpartition()	    Devuelve una tupla donde la cadena se divide en tres partes
rsplit()	        Divide la cadena en el separador especificado y devuelve una lista
rstrip()	        Devuelve una versión recortada a la derecha de la cadena.
split()	            Divide la cadena en el separador especificado y devuelve una lista
splitlines()    	Divide la cadena en los saltos de línea y devuelve una lista
startswith()    	Devuelve verdadero si la cadena comienza con el valor especificado
strip()	            Devuelve una versión recortada de la cadena.
swapcase()	        Intercambia mayúsculas y minúsculas y viceversa
title()	            Convierte el primer carácter de cada palabra a mayúsculas
translate()     	Devuelve una cadena traducida
upper()	            Convierte una cadena en mayúsculas
zfill()         	Rellena la cadena con un número especificado de valores 0 al principio
"""