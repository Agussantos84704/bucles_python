
# CODE:28
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por generar el bucle While True
- Dentro del bucle imprima con prints el menú
  de opciones en consola.

- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada operacion
  para almacenar la operación que se desea efectuar
  ingresada por consola con la función input
  Los valores que puede tomar la variable operacion van
  del "1" al "5", su programa no debe explotar si se ingresa
  otro texto distinto.

IMPORTANTE: Dentro del bucle primero debe solicitar al usuario
el ingreso de los dos números (numero_1 y numero_2) y luego
debe solicitar el ingreso de la operación a realizar
(debe respetar ese orden)

- Armar una serie de condicionales para evaluar
  que operación efectuar. Deberá guardar el resultado
  de la operación en una variable llamada resultado

- Si el usuario ingresa la operación de SALIR (opcion 5),
  deberá finalizar el bucle con la sentencia break.

- Si el usuario ingresa una opción fuera del rango
  solicitado de opciones, el programa no deberá 
  estallar, no deberá hacer nada permitiendo
  que el bucle While vuelva a realizar la consulta
  en la próxima iteración.
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    print("Ingrese los valores que desea operar:")
    print("Primer número:")
    numero_1 = float(input("Ingrese el primer número\n"))
    print("Segundo número:")
    numero_2 = float(input("Ingrese el segundo número\n"))
    print("Ingrese operación a realizar:")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación")
    print("4- División")
    print("5- SALIR")
    operacion = int(input())

    if operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4 or operacion == 5:
        print("¡Se termina el bucle!")
        break

print(f"Operación a realizar: {operacion}")

if operacion == 1:
    print("Sumar")
    resultado = numero_1 + numero_2
elif operacion == 2:
    print("Restar")
    resultado = numero_1 - numero_2
elif operacion == 3:
    print("Multiplicar")
    resultado = numero_1 * numero_2
elif operacion == 4:
    print("Dividir")
    resultado = numero_1 / numero_2
elif operacion == 5:
    resultado = "Muy bien, empecemos otra vez"
else:
    print("Algo salio mal en el bucle...")

print(f"El resultado es: {resultado}")