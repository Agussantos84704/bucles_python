
# CODE:26
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada cantidad_examenes
  para almacenar a cuantos exámenes se presentó
  el alumno (debe inicializarla en cero).
  Utilice un bucle e incremente en 1 la variable
  cantidad_examenes en cada iteración donde la nota
  sea positiva o cero.

- Crear una una variable llamada cantidad_ausentes
  para almacenar la cantidad de ausentes del
  alumno (debe inicializarla en cero).
  Utilice un bucle e incremente en 1 la variable
  cantidad_ausentes en cada iteración donde la nota
  sea negativa.

- BONUS: Todo el ejercicio se puede resolver
  en un único bucle, puede comenzar haciendo dos bucles
  por separado y luego ver como unirlos en uno solo

- Al final imprimir en pantalla todas las variables
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

cantidad_examenes = 0

cantidad_ausentes = 0

for i in notas:
    if i > 0:
        cantidad_examenes += 1
    else:
        cantidad_ausentes += 1

print(f'La cantidad de examenes rendidos son: {cantidad_examenes}')

print(f'La cantidad de ausencias es de: {cantidad_ausentes}')