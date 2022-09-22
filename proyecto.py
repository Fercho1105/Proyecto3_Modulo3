#Importamos las librerias a usar.
import matplotlib.pyplot as plt  #Para generar la grafica.
from random import randint #Para generar los numeros aleatorios.


def simulacion(canicas):  #Creamos la funcion para que haga la simulacion dependiedo las canicas que se le indiquen.
    niveles = 12  #Definimos los niveles que tendra nuestra simulacion.
    contenedores = [0]*(niveles) #Ahora hacemos una lista que simulara los contenedores de acuerdo a los niveles que son.

    #Ahora es cuando empezamos a calcular los resultados de las canicas.
    for h in range(canicas): 
        almacenar = -1
        for j in range(niveles):
            almacenar += randint(0, 1)
        contenedores[almacenar] += 1
    print(f"Se usaron {canicas} canicas como muestra")
    return contenedores  #Devolvemos los resultados que tenemos en los contenedores para posteriormente graficar estos datos en un histograma.


def grafica(contenedores):  #Creamos la función para graficar los resultados que obtuvimos.
    eje_x = [0,1,2,3,4,5,6,7,8,9,10,11,]  #Ya que son 12 niveles,hacemos un arreglo que sea el eje X del histograma, ponemos los niveles requeridos.
    plt.title('Simulación de la Máquina de Galton') #Ponemos nombre a la grafica.
    plt.bar(eje_x, contenedores, width=0.99) #Usamos plt.bar para hacer una gráfica de barras que se asemeja a un histograma y ponemos los datos requeridos. Modificamos la anchura de las barras para simular el histograma.
    plt.xlabel('Distribución de canicas') #Le ponemos nombre a los ejes.
    plt.ylabel('Cantidad de canicas')
    plt.show() #Mostramos la gráfica.

#Finalmente llamamos las funciones para hacer la simulación y su gráfica correspondiente.
galvin = simulacion(3000)
grafica(galvin)




# import numpy as np
# import matplotlib.pyplot as plt
# from random import randint
# levels = int(input("How many levels do you want?(min 1/ 20 by default) ") or 20)
# if levels >= 1:
#     lanes = [0]*(levels)
# else:
#     print("The value of levels can't be lower than 1.")
#     exit()
# for h in range((levels)**2*100):
#     stored = -1
#     for j in range(levels):
#         stored += randint(0, 1)
#     lanes[stored] += 1
# print((levels)**2*100, "balls were used in totall")
# print(lanes)
# X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5)
# plt.suptitle('Galton Board')
# plt.bar(X + 0.00, lanes, width=0.25)
# plt.show()
