# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OPERADORES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

# ---------------------------------- OPERADORES ARITMÉTICOS ---------------------------------- 
print("--- OPERADORES ARITMÉTICOS ---")

# Operaciones con enteros
print(3 + 4)    # Suma
print(3 - 4)    # Resta
print(3 * 4)    # Multiplicación
print(3 / 4)    # División
print(10 % 3)   # Resto
print(10 // 3)  # División aproximada: hace la division y si sale float aproxima a un entero
print(2 ** 3)   # Elevado
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)  
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float)) 


# ---------------------------------- OPERADORES DE ASIGNACIÓN ---------------------------------- 
print("--- OPERADORES DE ASIGNACIÓN ---")

# Operaciones con enteros
x = 27
x += 4
print(x)
x -= 5
print(x)
x *= 28
print(x)
x /= 2
print(x)
x //= 3
print(x)
x **= 2
print(x)
x %= 6
print(x)


# ---------------------------------- OPERADORES COMPARATIVOS ---------------------------------- 
print("--- OPERADORES COMPARATIVOS ---")

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "aba")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("aba"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


# ---------------------------------- OPERADORES LÓGICOS ---------------------------------- 
print("--- OPERADORES LÓGICOS ---")

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) # Convertir el resultado de la comparación a lo contrario: 3 > 4 --> False --> True


# ---------------------------------- OPERADORES DE IDENTIDAD ---------------------------------- 
print("--- OPERADORES DE IDENTIDAD ---")

a = 2
b = 2

print(a is b)
print(a is not b)


# ---------------------------------- OPERADORES DE MEMBRESÍA ---------------------------------- 
print("--- OPERADORES DE MEMBRESÍA ---")

a = "A"
b = "Alba"

print(a in b)
print(a not in b)