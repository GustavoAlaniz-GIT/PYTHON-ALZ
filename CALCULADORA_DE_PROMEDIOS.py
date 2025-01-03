# Calcular promedio de Notas. Las mismas pueden ir de 0 a 10, o de 0 a 100.

def calcular_promedio_notas():
    print("Programa para calcular el promedio de N notas")

    # Solicitar la cantidad de notas
    while True:
        cantidad = input("Ingrese la cantidad de notas a promediar: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print("Entrada no válida. Debe ingresar un número entero positivo.")

    suma_notas = 0

    # Solicitar las notas una por una
    for i in range(1, cantidad + 1):
        while True:
            nota = input(f"Ingrese la nota {i} (entre 0 y 10): ")
            if nota.replace('.', '', 1).isdigit() and 0 <= float(nota) <= 10:
                suma_notas += float(nota)
                break
            else:
                print("Entrada no válida. Debe ingresar un número entre 0 y 10.")

    # Calcular el promedio
    promedio = suma_notas / cantidad

    # Presentar el resultado, con dos decimales después del punto decimal.
    print(f"El promedio de las {cantidad} notas ingresadas es: {promedio:.2f}")

#Llamamos a la función
calcular_promedio_notas() 

