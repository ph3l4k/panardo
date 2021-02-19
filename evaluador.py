'''#Array bidimensional
#tupla = [[0,26,17,15,27],[26,0,15,12,4],[17,15,0,2,18],[15,12,2,0,17],[27,4,18,17,0]]

#solucion=["c","a","e","d","b"]
# mas corta a ojo, 
#solucion=["a","d","c","b","e"]'''
distancia = 0

def valorLetra(arg):
    #97 para minusculas, 65 para mayusculas
    '''
        evaluo si es mayuscula o minuscula
            si fuera minuscula saldria con el resultado mas bajo (p.ej:a daria 32) mas de 25 por lo que pasaria al elif para devolver el valor de una letra minuscula
            primero evaluo las letras mayusculas, ya que si da mayor procedo a evaluar si es minuscula, en cualquiero otro caso el valor no seria el adecuado
        tambien evaluo que no sea menor que 0, para que solo devolvamos el valor de una letra, descartando valores no permitidos como otros caracteres del teclado
    '''
    if(ord(arg)-65 <= 25 and ord(arg)-65 >= 0):#26 porque quito la ñ y la ll (doble l)
        return ord(arg)-65
    elif(ord(arg)-97 <= 25 and ord(arg)-97 >= 0):
        return ord(arg)-97

def calcularDistancia(solucion,tupla):
    global distancia
    distancia = 0
    for letra in solucion:
        if(solucion.index(letra) != len(solucion)-1):
            distancia += int(tupla[valorLetra(letra)][valorLetra(solucion[solucion.index(letra)+1])])
        else:
            distancia += int(tupla[valorLetra(letra)][valorLetra(solucion[0])])
    return distancia 

#calcularDistancia(solucion,tupla)
#print(calcularDistancia(solucion,tupla))