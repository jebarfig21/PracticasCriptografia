import numpy as np
import random
from numpy.linalg import det
def raiz(n):
    if n == int(np.sqrt(n)) * int(np.sqrt(n)):
        return int(np.sqrt(n))
    return -1



def generaLlaveAleatoria(alphabet,n):
    new_key=""
    while len(new_key) < n*n:
        new_key+= alphabet[random.randrange(len(alphabet))]

    if determinanteLlave(alphabet,new_key,n) == 0:
        return generaLlaveAleatoria(alphabet,n)

    return new_key


def llaveToMatriz(alphabet,llave,n):
    segmentos=[]
    for i in range(n):
        segmentos.append([])
    longitud=len(llave)
    aux=0
    for i in segmentos:
        for j in range(n):
            i.append(alphabet.index(llave[aux]))
            aux +=1

    return segmentos

#Funcion que regresa el determinante en el espacio modular
def determinanteLlave(alphabet,llave,n):
    matriz = llaveToMatriz(alphabet,llave,n)
    det    = int(round(np.linalg.det(matriz))) % len(alphabet)
    return det


def inversoDeterminante(alphabet,llave,n):
    det = determinanteLlave(alphabet,llave,n)
    for i in range(len(alphabet)):
        if (det * i)%len(alphabet) == 1:
            return i

    return False

def generaLlaveValida(alphabet,n):
    llave = generaLlaveAleatoria(alphabet,n)
    if(inversoDeterminante(alphabet,llave,n)==False):
        print(llave)
        return generaLlaveValida(alphabet,n)
    return llave

def matrizInversa(alphabet,llave,n):
    matriz=llaveToMatriz(alphabet,llave,n)
    detInv=inversoDeterminante(alphabet,llave,n)
    for i in range(n):
        for j in range(n):
            matriz[i][j]=(matriz[i][j]*detInv)%27

    return matriz

def mensajeToMatriz(alphabet,n,mensaje):
    mensaje=quitaEspacios(mensaje)
    sobrante=int((n-(len(mensaje)%n))%n)
    segmentos=[]
    for i in range(sobrante):
        mensaje+=("A")
    for i in range(len(mensaje)//n):
        segmentos.append([])
    aux = 0
    for i in segmentos:
        for j in range(n):
            i.append(alphabet.index(mensaje[aux]))
            aux +=1
    return segmentos

def quitaEspacios(mensaje):
    return mensaje.replace(" ", "")

def matrizInversa(alphabet,key,n):
    A=np.matrix(mensajeToMatriz(alphabet,n,key))
    deter= det(A)
    detInv = inversoDeterminante(alphabet,key,n)
    matrizInversa = (np.linalg.inv(A)*(deter*detInv))%27
    return matrizInversa
print(matrizInversa("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ","BCDE",2))
