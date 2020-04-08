import random
from utils import CryptographyException
from utils import prime_relative
from utils import egcd
from utils import modinv

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.

        Bajo la siguiente formula-> y = Ax+B(mod M), donde x es la posicion del elemento en el alfabeto, 
        y es la posicion del elemento en el nuevo orden.

        M = cardinalidad del alfabeto
        """
        self.M = len(alphabet)
        self.alphabet=alphabet
        if A is None:
            self.A=len(alphabet) + 1
            self.B=random.randint(0,len(alphabet))
        else:
            #Verificamos que la longitud del alfabeto y la llave A sean primos relativos
            if not prime_relative(A,len(alphabet)):
                raise CryptographyException
            self.A=A
            self.B=B
        #pass

    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        #Proceso para obtener un dicionario de la forma LETRA : INDICE
        dic={}
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = i     

        new_message=""
        
        #Aplicamos la formula para cifrar el mensaje
        for i in message:
            if i in self.alphabet:
                new_message+= self.alphabet[(((self.A*dic[i])+self.B)%self.M)]#y=Ax+B(mod M)
            else :
                new_message+=i
        return new_message

    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        dic={}#Dada la letra obtendremos su indice
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = i     

        new_message=""
        
        #Aplicamos la formula para descifrar el mensaje usando el
        #algoritmo extendido de euclides para poder encontrar el modular inverso del numero
        for i in criptotext:
            new_message+= self.alphabet[(modinv(self.A, len(self.alphabet))*(dic[i] - self.B) % len(self.alphabet))]

        return new_message
a = Affine("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 19, 25)

print(a.cipher("GO TVZÑO VÑZTL WG VT FTONJT WG NÑAI OIFDLG OI BÑSGLI TNILWTLFG OI JT FÑNJI ESGFRI BÑG XSXST ÑO JSWTVZI WG VIU VTOKT GO TUESVVGLI TWTLZT TOESZÑT LINSO PVTNI A ZTVZI NILLGWIL"))



