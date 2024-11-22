'''
EJERCICIO N° 5: Cree una función que calcule el Factorial de un número entero positivo.

El factorial de un entero positivo n, el factorial de n o n factorial se define en principio como el producto de todos los números enteros positivos desde 1 (es decir, los números naturales) hasta n. La operación de factorial aparece en muchas áreas de las matemáticas, particularmente en combinatoria y análisis matemático.
'''

def calcular_factorial():
    while True:
        # Solicitar entrada del usuario
        entrada = input("Por favor, ingresa un número entero positivo: ")
        
        # Verificar si la entrada es un número entero positivo
        if entrada.isdigit():  # Verifica que la entrada sea solo números
            numero = int(entrada)
            if numero >= 0:  # Asegurarse de que sea positivo o cero
                break  # Salir del bucle si la entrada es válida
            else:
                print("El número debe ser entero y positivo. Inténtalo de nuevo.")
        else:
            print("Entrada no válida. Ingresa un número entero positivo.")

    # Calcular el factorial utilizando un bucle for
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i

    # Mostrar el resultado
    print(f"El factorial de {numero} es: {factorial}")


calcular_factorial()
