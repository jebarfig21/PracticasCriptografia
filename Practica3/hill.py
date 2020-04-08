from utils import CryptographyException
import numpy as np
import random
from numpy.linalg import det
class Hill():
    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet=alphabet                              #Se iniia con el alfabeto de parametro
        if raiz(n)==-1:                                     #Verificamos que n tenga raiz exacta
            raise CryptographyException                     #Lanzamos excepcion si no es exacta
        else:
            self.n=raiz(n)                                  #Manejamos como n la raiz ya que es mas intuitivo en los metodos tener matrices de nxn

        self.key=key                                        #Asignamos el parametro sin importar si es None, porque los metodos auxiliares son sobre self.key
        if key == None:                                     #Si el parametro fue None
            self.key=self.generaLlaveAleatoria()            #Generamos una llave aleatorio y la asiganmos
            while not self.esLlaveValida() :                #Verificacom que self.key sea valida, mientras no lo sea
                self.key=self.generaLlaveAleatoria()        #Generamos una llave aleatorio de nuevo hast que esta sirva

        else:                                               #Si key != None
            if not self.esLlaveValida() :                   #Y la llave que se uso en el parametro no es valida
                raise CryptographyException                 #Lanzamos una excepcion

    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        cadena =""                                                #Cadena vacia
        matriz_mensaje= self.cadenaToMatriz(message)              #Obtenemos la matriz numerica asociada al mensaje claro
        matriz_llave = self.cadenaToMatriz(self.key)              #Obtenemos la matriz numerica de cifrado asociada a la llave
        for i in matriz_mensaje:                                  #Por cada fila en la matriz de mensaje
            for j in matriz_llave:                                #Por cada vector en la matriz de la llave (Vector X Matriz)
                aux=multArr(i, j)                                 #Guardamos el valor de multpilicar el vector por la fila de Matriz mensaje
                cadena += self.alphabet[aux%len(self.alphabet)]   #Concatenamos la letra en el alfabeto asociada al resultado de aux
        cadena=cadena[0:len(message)]                             #recortamos la salida a la longitud del mensaje original,
                                                                  #en caso de que hayamos tenido que rellenar
        return cadena                                             #Regresamos el texto cifrado por el metodo de hill


    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        cadena =""                                                #Cadena vacia
        matriz_mensaje= self.cadenaToMatriz(ciphered)             #Otenemos la matriz numerica asociada al mensaje cifrado
        matriz_llave = self.matrizInversa()                       #Obtenemos la matriz numerica inversa(decifrar) asociada a la llave
        for i in matriz_mensaje:                                  #Por cada fila en la matriz de mensaje
            for j in matriz_llave:                                #Por cada vector en la matriz de la llave (Vector X Matriz)
                aux=multArr(i, j)                                 #Guardamos el valor de multpilicar el vector por la fila de Matriz mensaje
                cadena += self.alphabet[aux%len(self.alphabet)]   #Concatenamos la letra en el alfabeto asociada al resultado de aux

        cadena=cadena[0:len(ciphered)]                            #recortamos la salida a la longitud del mensaje cifrado
        return cadena                                             #Regresamos el texto decifrado


    #Funcion auxiliar que genera llave de hill aleatoria de tamaño n
    def generaLlaveAleatoria(self):
        new_key=""                                                         #Cadena Vacia
        while len(new_key) < self.n*self.n:                                #Hasta que la cadena se de tamaño
            new_key += self.alphabet[random.randrange(len(self.alphabet))] #Vamos añadiendo elementos aleatorios a la cadena
        return new_key                                                     #Regresamos llave

    #Funcion que regresa el determinante en el espacio modular
    def determinanteLlave(self):
        matriz = self.cadenaToMatriz(self.key)                            #Obtenemos la matriz numerica asociada a una cadena
        determinante    = int(round(det(matriz))) % len(self.alphabet)    #Usamos int round, por la forma de salida de la funcion det
        return determinante                                               #Regresamos el determinante asociada a la matriz


    #Funcion que regresa el determinante en el espacio modular, si no existe, regresa 0
    def inversoDeterminante(self):
        dete = self.determinanteLlave()                                   #Obtenemos el determinante de la llave
        for i in range(len(self.alphabet)):                               #Iteramos sobre todo el alfabeto
            if (dete * i)%len(self.alphabet) == 1:                        #Buscamos un inverso multiplicativo del determinante en el modulo
                return i                                                  #Regreso el inverso multiplicativo
        return 0                                                          #Si no encontro inverso regresa 0


    #Metodo auxiiar que revisa que la llave tenga inverso multiplicativo y que ese inverso no sea el mismo
    def esLlaveValida(self):
        if self.inversoDeterminante()==0 or self.inversoDeterminante()==self.determinanteLlave():
            return False
        return True

    def matrizInversa(self):
        matrizLlave=self.cadenaToMatriz(self.key)                       #Obtenemos la matriz que representa la llave, nos sirve para la funcion inv
        deter= det(matrizLlave)                                        #obtenemos el determinante de la matriz
        detInv = self.inversoDeterminante()                            #obtenemos el determiannte inverso de la matriz
        matrizInversa = np.linalg.inv(matrizLlave)*(deter*detInv)      #Multiplicamos or el determinante para quiar la division y despues usamos el inverso modular
        return matrizInversa.tolist()                                  #Regresamos la matriz como lista de python, porque si no regresa un objet matrix

    #Funcion que devuelve una matriz de matrices columnas de enteros
    #Este metodo se usas tanto para la llave como para el mensaje
    def cadenaToMatriz(self,mensaje):
        mensaje   = quitaEspacios(mensaje)                             #Quita los espacios del mensaje
        sobrante  = int((self.n-(len(mensaje)%self.n))%self.n)         #Obtiene el numero de elementos b tal que n | len(m)+b
        segmentos = []                                                 #Matriz vaica que va a contener matrices columnas
        for i in range(sobrante):                                      #Rellena el mensaje para cumplir con la longitud
            mensaje+=("A")                                             #A no afecta al final
        for i in range(len(mensaje)//self.n):                          #Generamos la matriz vacia con el numero de segmentos que necesitamos, tendran n elementos
            segmentos.append([])                                       #Añadimos la lista vacia a la lista de semgentos
        aux = 0                                                        #Variable que lleva el indice del mensaje de entrada
        for i in segmentos:                                            #Por cada sublista vacia
            for j in range(self.n):                                    #En un rango de  [0,n], recordemos que n =3 o n=2 en los ejemplos
                i.append(self.alphabet.index(mensaje[aux]))            #Escribimos en la amtriz el indice en el alfabeto del elemento en la cadena
                aux +=1                                                #Aumentamos el indice auxiliar para el mensaje de entrada
        return segmentos                                               #Regresamos una matriz llena de indices.


#Funcion que quita todos los espacios del mensaje de entrada
#Se usa en sipher y decipher
def quitaEspacios(mensaje):
    return mensaje.replace(" ", "")

#Regresa la raiz de n si esta es exacta, si no regresa -1, es mas intuitiva la implementacion
def raiz(n):
    if n == int(np.sqrt(n)) * int(np.sqrt(n)):
        return int(np.sqrt(n))
    return -1

#Regresa un producto punto entre dos listas de n elementos cada una, se multiplica indice por indice, y todos los resultados se suman
def multArr(arr1, arr2):
    aux = 0
    for i in range(len(arr1)):
            aux+= (int(round(arr1[i]))*int(round(arr2[i])))%27 #No olvidemos trabajar en el espacio modular
    return aux
