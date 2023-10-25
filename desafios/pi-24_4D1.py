
# CODE:41
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por crear una variable llamada resultado
  para almacenar la palabra final que usted arme
  segun el criterio establecido en el enunciado.

- Deberá proveer por consola la palabra objetivo a ordenar
  la cual se almacenará en la variable llmada objetivo
- Deberá utilizar bucles para recorrer la palabra objetivo
  y deberá usar listas y todo método de strings a su disposición
  que lo ayude a resolver este desafio.
'''

print("Ordenar caracteres")
objetivo = input("Ingrese palabra de entrada:\n")
# Empezar aquí la resolución del ejercicio

mayus = ""

minus = ""

digit_par = ""

digit_nor = ""

for i in objetivo:
    if i.isupper():
        mayus += i
    elif i.islower():
        minus += i
    elif i.isdigit():
        num = int(i)
        if num % 2 == 0:
            digit_par += i
        else:
            digit_nor += i
        

print(f'{mayus}')

print(f'{minus}')

print(f'{digit_par}')

print(f'{digit_nor}')

mayus = ''.join(sorted(mayus))

minus = ''.join(sorted(minus))

digit_par = ''.join(sorted(digit_par))

digit_nor = ''.join(sorted(digit_nor))
    

resultado = minus + mayus + digit_nor + digit_par

print(f'El resultado es: {resultado}')

