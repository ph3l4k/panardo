from evaluador import calcularDistancia
from time import time
import csv
import random

matrizCiudades = [] #Creo un array vacio donde ire añadiendole las filas correspondientes del archivo
longitudFichero = 0
soluciones = 0
ganador = 0
iteraccion = 0

def calcularGanador(combinacionesUsuario):
    tiempo_inicial = time()
    cargarMatriz()
    #antes de nada llamo a la funcion generarSoluciones para generarlas
    generarAleatorio(combinacionesUsuario)
    global ganador
    #para cada combinacion que queria el usuario calculo su solucion y comparo si es mejor que la actual ganadora
    for i in range(len(soluciones)):
        distancia = int(calcularDistancia(soluciones[i],matrizCiudades))
        comparar(distancia)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final-tiempo_inicial
    return ganador, round(tiempo_ejecucion,2)

def cargarMatriz():
    global matrizCiudades
    global longitudFichero

    if(len(matrizCiudades)>0):
        matrizCiudades=[]

    fichero = "./archivos/matriz.csv" #Le asigno a una variable la ruta de la matriz con los valores de las ciudades
    with open(fichero,'r') as csvfile:
        reader = csv.reader(csvfile) 
        for row in reader: #Cada fila es una lista correspondiente a una ciudad
            matrizCiudades.append(row)
    longitudFichero = len(matrizCiudades)

def generarAleatorio(combinacionesUsuario):
    global longitudFichero
    global soluciones
    soluciones = [0]*combinacionesUsuario
    #para crear un array con la dimension de numero de soluciones que quiere el usuario
    for i in range(combinacionesUsuario):
        soluciones[i] = [0]*longitudFichero

    #para generar soluciones aleatorias
    for i in range(combinacionesUsuario):
        for j in range(longitudFichero):
            #guardo en el array bidimensional de a hasta la longitud de la matriz de ciudades
            soluciones[i][j]=str(chr(j+97))
        #desordeno aleatoriamente la solucion creada
        random.shuffle(soluciones[i])

def comparar(distanciaFinal):
    global ganador
    global iteraccion
    if(iteraccion == 0):
        ganador = distanciaFinal
    else:
        if(distanciaFinal<ganador): 
            ganador = distanciaFinal
    iteraccion+=1
    return ganador