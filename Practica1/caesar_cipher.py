import random #Importamos biblioteca para numeros aleatorios

class Caesar():
    alphabet=""
    key=None

    """
    Constructor de clase que tiene como parámetro todos los atributos que necesita el algoritmo de cifrado de César.
    ParámetroS:
    alphabet -- El alfabeto sobre quien se cifra el mensaje.
    key      -- El tamaño del desplazamiento sobre el alfabeto, si es None, se debe de escoger una llave aleatoria, válida.
    """
    
    def __init__(self, alphabet, key=None):
        self.alphabet=alphabet
        if(key!=None):
            self.key=key%len(alphabet)
        else:
            self.key=random.randint(0,len(alphabet))
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """    
    def cipher(self, message, flag=None):
        new_message=""
        dic={}
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = self.alphabet[(i+self.key)%len(self.alphabet)]                             

        for i in range(len(message)):
            if(flag):
                if(message[i]==" "):
                    new_message+=message[i]
                else:
                    new_message+=dic[message[i]]
            else:
                if(" " in self.alphabet):
                    new_message+=dic[message[i]]
                else:    
                    if(message[i]!=" "):
                        new_message+=dic[message[i]]
        return new_message

    def decipher(self, criptotext, flag=None):

        new_message=""
        dic={}
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = self.alphabet[(i-self.key)%len(self.alphabet)]
                              
        for i in range(len(criptotext)):
            if(flag):
                if(criptotext[i]==" "):
                    new_message+=criptotext[i]
                else:
                    new_message+=dic[criptotext[i]]
            else:
                if(" " in self.alphabet):
                    new_message+=dic[criptotext[i]]
                else:    
                    if(criptotext[i]!=" "):
                        new_message+=dic[criptotext[i]]
        return new_message
