'''
EJERCICIO N°: 4 Cree una función que dibuje un rectangulo de X filas y X columnas 
determinadas por el usuario


Descripción del programa:

1. Solicitar las dimensiones del rectángulo:

   1.1 Validar que las entradas (filas y columnas) sean números enteros positivos.

2. Dibujar el rectángulo:

   2.1 Usar dos bucles for anidados para imprimir las filas y columnas.

3. Validaciones:

   3.1 En caso de una entrada no válida, mostrar un mensaje y pedir nuevamente el dato.

'''

def dibujar_rectangulo():
    print("Programa para dibujar un rectángulo de X filas y X columnas")

    # Solicitar el número de filas
    while True:
        filas = input("Ingrese el número de filas del rectángulo: ")
        if filas.isdigit() and int(filas) > 0:
            filas = int(filas)
            break
        else:
            print("Entrada no válida. Debe ingresar un número entero positivo.")

    # Solicitar el número de columnas
    while True:
        columnas = input("Ingrese el número de columnas del rectángulo: ")
        if columnas.isdigit() and int(columnas) > 0:
            columnas = int(columnas)
            break
        else:
            print("Entrada no válida. Debe ingresar un número entero positivo.")

    # Dibujar el rectángulo
    for i in range(filas):
        for j in range(columnas):
            print("°", end="")  # Imprimir "°" sin salto de línea
        print()  # Hacer salto de línea al final de cada fila

dibujar_rectangulo() 