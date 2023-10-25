
# CODE:24
# IMPORTANTE: NO borrar los comentarios

# Alumno:
# Usted ya cuenta con la lista numeros
# Crear una variable llamada suma_total
# inicializada en cero
# Realiza un bucle que recorra cada elemento
# En cada iteración incrementar el valor de suma_total
# (con el operador incremento) con cada número positivo
# Utilice un condicional para evaluar si el número
# es positivo

# TIP
# Utilice el debugger para ver como avanza
# el programa paso a paso
numeros = [1, 5, -1, 6, 10, 2, -5]

# Imprimir en pantalla la variable suma_total
# El resultado final de la suma deberá ser 24

suma_total = 0

for i in numeros:
    if i > 0:
        suma_total += i

print(f'La suma de los valores positivos es: {suma_total}')