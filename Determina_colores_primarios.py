'''
Cree una funcion que determine si un color es primario o no, 
se debe imprimir por pantalla la leyenda "el color X es primario "
o "el color X no es primario"
'''
'''
DESCRIPCIÓN DE REFERENCIA: 
Los colores primarios son aquellos que no se pueden obtener 
a través de la mezcla de ningún otro color. 
Estos suelen considerarse absolutos y únicos, ya que no tienen matices en común,
es decir, son claramente diferenciables entre sí.
La teoría tricromática o RGB establece que el ojo humano cuenta con tres tipos 
de células, denominadas conos, cada uno de los cuales es más sensible a la luz de un color 
diferente: rojo, verde y azul. Una teoría muy extendida, puesto que en ella se 
basan la mayoría de las tecnologías de visualización de color.
'''

def determinar_color_primario():
    print("Programa para determinar si un color es primario")

    while True:
        # Solicitar el color al usuario. Acomodo la entrada a minúscula
        color = input("Ingrese el nombre de un color (o 'salir' para terminar): ").strip().lower()
        
        # Salir del programa si el usuario lo desea
        if color == "salir":
            print("Terminando el programa. ¡Gracias!")
            break

        # Verificar si el color es primario
        es_primario = False
        for primario in ["rojo", "verde", "azul"]:
            if color == primario:
                es_primario = True
                break

        # Mostrar el resultado
        if es_primario:
            print(f"El color {color} es primario.")
        else:
            print(f"El color {color} no es primario.")


#Llamamos a la función
determinar_color_primario()
