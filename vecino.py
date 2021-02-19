import csv #importo la libreria csv para poder leer la matriz
import random #importo la libreria random para hacer operaciones matematicas
from time import time #importo time para calcular el tiempo que tarde en ejecutarse el programa

matrizCiudades = [] #matriz donde guardare el las distancias entre ciudades del csv
solAleatoria =  [] #sera la matriz que guarda la solucion aleatoria generada por cada instancia
ciudadRecorrida = [] #matriz donde guardare el indice de la ciudad ya recorrida para comprobar si la hemos recorrido o no
solGanador = [] #combinacion aleatoria de la distancia ganadora de todas las generadas
distancia = 0 #distancia desde la ciudad correspondiente a la mas corta no repetida
ganador = 0 #sera la distancia mas corta entre ciudades de la solucion aleatoria mas corta entre todas las soluciones aleatorias generadas
contG = 0 #para evaluar la primera distancia y asignarsela a ganador

def calcularGanador(combinaciones):
    tiempo_inicial = time() #nada mas comenzar el programa creo una variable con el tiempo en ese momento
    reset()
    cargarMatriz()
    global solAleatoria
    global distancia
    global ganador
    for i in range(combinaciones):
        solAleatoria = generarAleatorio()
        distancia = evaluarDistancia()
        ganador = comparar(distancia)
    tiempo_final = time() #tras todos los calculos y con la solucion ganadora obtengo el tiempo actual
    tiempo_ejecucion = tiempo_final-tiempo_inicial #al tiempo final le resto el tiempo inicial para calcular el tiempo que ha llevado realizar todo el proceso del algoritmo
    return ganador, round(tiempo_ejecucion,2), solGanador

#este metodo vale para cargar la matriz correspondiente que haya subido el usuario
def cargarMatriz():
    global matrizCiudades
    fichero = "./archivos/matriz.csv" #le asigno a una variable la ruta de la matriz con los valores de las ciudades
    with open(fichero,'r') as csvfile: #para leer el fichero csv de las ciudades
        reader = csv.reader(csvfile) 
        for row in reader: #cada fila es un array correspondiente a una ciudad
            matrizCiudades.append(row) #agrego el array especifico como nuevo elemento del array matrizCiudades

#este metodo me genera una solucion aleatoria para el tamaño de ciudades que contenga el fichero csv
def generarAleatorio():
    global matrizCiudades
    sol = [0 for i in range(len(matrizCiudades))]
    for i in range(len(sol)):
        sol[i]=i
    random.shuffle(sol) #desordeno la solucion para que sea aleatoria
    return sol

def evaluarDistancia():
    global solAleatoria
    global matrizCiudades
    global ciudadRecorrida
    
    #las siguientes 3 lineas son para sacar una solucion mayor que cualquiera existente de una ciudad a otra dentro del array, para poder compararla al principio, pensando en que no sabemos los valores de la matriz
    distanciaSol = 0#se la suma total de las menores distancias de la solucion
    distanciaMenor = 0#sera la variable para comparar la menor ciudad dentro de las posibles distancias que tenga una ciudad a las demas, cunado se sepa cual es la menor, se le sumara a distancia

    for i in range(len(solAleatoria)):#hara 15 iteracciones, una por indice de solucion
        ciudad = solAleatoria[i]#el indice de la ciudad de la solucion aleatoria correspondiente a i
        distanciaMenor = 0
        cont = 0
        indiceMenorCiudad = 0
        for j in range(len(matrizCiudades[ciudad])):#para recorrer todas las distancias desde esa ciudad
            if(ciudad!=j):#descarto 0
                if(evaluarCiudad(j)==False):#evaluo que la ciudad no este repetida
                    if(cont==0):#cuando recorramos la primera ciudad de la solucion
                        distanciaMenor = matrizCiudades[ciudad][j]#para inicializar el valor de la distancia a comparar
                        indiceMenorCiudad = j
                        cont = cont+1
                    else:
                        if(matrizCiudades[ciudad][j]<distanciaMenor):#en caso de no entrar en este if, la menor ciudad seria la recogida en el if anterior
                            distanciaMenor = matrizCiudades[ciudad][j]
                            indiceMenorCiudad = j                    
        ciudadRecorrida.append(indiceMenorCiudad)#al recorrer todas las distancias y obtener la menor agrego el indice de la ciudad menor
        distanciaSol = distanciaSol+int(distanciaMenor)            
    ciudadRecorrida = []#para vaciar las ciudades recorridas una vez se haya calculado la menor distancia de la solucion aleatoria
    return distanciaSol

def evaluarCiudad(indiceCiudad):
    if indiceCiudad in ciudadRecorrida:
        return True
    else:
        return False

def comparar(distancia):#para comparar si el total de la distancia menor por cada ciudad de la solucion aleatoria es menor que la menor encontrada por otra solucion aleatoria
    global ganador
    global contG
    global solGanador
    if(contG == 0):
        contG = contG+1
        solGanador = solAleatoria
        return distancia
    else:
        if(distancia<ganador):
            solGanador = solAleatoria
            return distancia
        else:
            return ganador

def reset():#para resetear todas las variables cada vez que se use el programa
    global matrizCiudades
    global solAleatoria
    global ciudadRecorrida
    global solGanador
    global distancia
    global ganador 
    global contG

    if(len(matrizCiudades)>0):
        matrizCiudades=[]

    if(len(solAleatoria)>0):
        matrizCiudades=[]

    if(len(ciudadRecorrida)>0):
        matrizCiudades=[]
    
    if(len(solGanador)>0):
        matrizCiudades=[]

    distancia = 0

    ganador = 0

    contG = 0