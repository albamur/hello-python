### Challenges ###

"""
Reto #0: EL FAMOSO "FIZZ BUZZ”
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzzWhile():
    i = 1

    #for in range(100):
    while i <= 100:

        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0):
            print("fizz")
        else:
            print(i)
        
        i += 1

#fizzbuzzWhile()


def fizzbuzzFor():
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
        
        i += 1

#fizzbuzzFor()


"""
Reto #1: ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

"""

def is_anagrama(word_1, word_2):
    
    # Reverse
    reversed_word = word_1[::-1]

    if word_1.lower() == word_2.lower():
        return False

    return reversed_word.lower() == word_2.lower()
print(is_anagrama("amor","roma"))


"""
Reto #2: LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():
    i = 0
    j = 1
    k = i + j

    cont = 0

    for cont in range(50):
        print(i)
        
        i = j
        j = k
        k = i + j

        cont += 3    

fibonacci()



"""
Reto #3: ¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True


"""
Reto #4: ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""