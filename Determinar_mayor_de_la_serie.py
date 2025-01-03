'''
EJERCICIO N°3:Cree una funcion que determine que numero de una serie de N numeros es mayor

El programa está diseñado para encontrar el mayor número de una serie de N números, 
ingresados por el usuario, siguiendo estos pasos:

1. Cantidad de números:
    1.1 Valida que el usuario ingrese un número entero positivo.
2. Ingreso de números:

    2.1 Cada entrada se valida para asegurarse de que sea numérica.
    2.2 Usa replace('.', '', 1) para manejar decimales y replace('-', '', 1) para números negativos.
    2.3 Actualiza la variable mayor si el número ingresado es mayor que el actual.

3. Resultado:

    3.1 Al finalizar, imprime el número mayor.
'''



def encontrar_mayor_numero():
    print("Programa para determinar el mayor de una serie de N números")

    # Solicitar la cantidad de números
    while True:
        cantidad = input("Ingrese la cantidad de números: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print("Entrada no válida. Debe ingresar un número entero positivo.")

    mayor = None  # Inicializar el valor máximo

    # Solicitar cada número
    for i in range(1, cantidad + 1):
        while True:
            numero = input(f"Ingrese el número {i}: ")
            if numero.replace('.', '', 1).replace('-', '', 1).isdigit():
                numero = float(numero)
                if mayor is None or numero > mayor:
                    mayor = numero
                break
            else:
                print("Entrada no válida. Debe ingresar un número.")

    # Mostrar el resultado
    print(f"El mayor número de la serie es: {mayor}")

encontrar_mayor_numero() 