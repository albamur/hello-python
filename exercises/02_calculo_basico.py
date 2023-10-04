'''
Crear una calculadora básica en la que se pregunte por consola los números y operación a calcular.
Después la calculadora preguntará cual cree el usuario que va a ser resultado y devolverá si es
True or False y el resultado
'''

print("\n------------ CÁLCULO BÁSICO ------------\n")
print('Introduce dos números: ')

# Convertir los datos introducidos por consola de str a int para poder hacer las operaciones
num1 = int(input('Primero número: '))
num2 = int(input('Segundo número: '))

print("¿Es el primer numero positivo?: ", num1 > 0)
print("¿Es el segundo numero positivo?: ", num2 > 0)
print("¿Son los dos positivos o menores que 10: ", (num1 > 0 and num1 > 0) or (num1 < 10 and num2 < 10))

print("\nConcatenación con la función print:")
suma =  num1 + num2
resta= num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
div_aprox =  num1 // num2
elev = num1 ** num2

print("1. Suma:", suma)
print("2. Resta:",resta)
print("3. Multiplicación:", mult)
print("4. División:", div)
print("5. Resto:", mod)
print("6. Divisón aproximada:", div_aprox)
print("7. Elevado:", elev)

print("\nConcatenación con de strings:")
suma =  "1. Suma: " + str(num1 + num2)
resta= "2. Resta: " + str(num1 - num2)
mult = "3. Multiplicación: " + str(num1 * num2)
div = "4. División: " + str(num1 / num2)
mod = "5. Resto: " + str(num1 % num2)
div_aprox =  "6. Divisón aproximada: " + str(num1 // num2)
elev = "7. Elevado: " + str(num1 ** num2)

print(suma)
print(resta)
print(mult)
print(div)
print(mod)
print(div_aprox)
print(elev)

print("\n\n")