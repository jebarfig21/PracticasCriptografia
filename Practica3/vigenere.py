import random

class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet=alphabet
        #Si no nos pasan la llave generamos una nosotros
        if password is None:
            new_key=""   #Cadena Vacia
            while len(new_key) < random.randint(4, 50):#Hasta que la cadena se de tamaño
                new_key += alphabet[random.randrange(len(alphabet))] #Vamos añadiendo elementos aleatorios a la cadena
            self.password = new_key
        else:
            self.password=password
        self.largoClave=len(self.password)

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        dic={}#Dada la letra obtendremos su indice
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = i

        new_message=""

        #Variable auxiliar que nos ayudara a contar el indice de la letra de nuestra llave
        j=0

        #Aplicamos la formula para cifrar el mensaje
        #En términos matemáticos puede expresarse la función de cifrado como: 
        #         E(Xi)=(Xi+Ki) mod L
        #Donde Xi es la letra en la posición i del texto a cifrar, 
        #Ki es el carácter de la clave correspondiente a Xi,pues se encuentran en la misma posición,
        #y L es el tamaño del alfabeto.
        for i in message:
            #utilizamos el modulo del largo de la clave para que volvamos a comenzar con
            #la primera letra de la llave una vez que terminemos de leer todas sus letras
            valorCifrado = (dic[i] + dic[self.password[j % self.largoClave]]) % 27
            new_message += self.alphabet[valorCifrado]
            j+=1
        return new_message


    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        dic={}#Dada la letra obtendremos su indice
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = i

        new_message=""

        j=0

        #Para descifrar realizamos la operación inversa
        for i in ciphered:
            valorDescifrado = (dic[i] - dic[self.password[j % self.largoClave]]) % 27
            new_message += self.alphabet[valorDescifrado]
            j+=1
        return new_message