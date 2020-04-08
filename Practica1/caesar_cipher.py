import random #Importamos biblioteca para numeros aleatorios

class Caesar():

    """
    Constructor de clase que tiene como parámetro todos los atributos
    que necesita el algoritmo de cifrado de César.
   
    Parámetro:
    alphabet -- El alfabeto sobre quien se cifra el mensaje.
    key      -- El tamaño del desplazamiento sobre el alfabeto, si es 
                None, se debe de escoger una llave aleatoria, válida.
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
        dic={}
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = self.alphabet[(i+self.key)%len(self.alphabet)]                             

        new_message=match(message,dic,self.alphabet,flag)
        
        return new_message


    """
    Descifra el mensaje recibido como parámetro con el algoritmo de
    cifrado césar, regresa a texto claro un mensaje previamente cifrado con Cesar
    Parámetro:
        message -- el mensaje a cifrar.
    """
    def decipher(self, criptotext, flag=None):
        dic={}
        for i in range(len(self.alphabet)):
            dic[self.alphabet[i]] = self.alphabet[(i-self.key)%len(self.alphabet)]
        new_message=match(criptotext,dic,self.alphabet,flag)

        return new_message

"""
Funcion auxiliar que dado un texto, un diccionario, un alfabeto y una bandera hace el match del elemento en la osicion original con el elemento que esta en la posicion con desplazamiento; Esta funcion se sua tanto para cifrar como para decifrar:
Parametros:
- texto    : Es el texto que se queire cifrar o decifrar
- dic      : Es el diccionario que ya se hizo con desplazamiento
- alphabet : Es el alphabeto de la clase Caesar
- flag     : Es la bandera que se pasa en la clase para respetar o no los espacios
"""    
def match(texto,dic,alphabet,flag):
    new_message=""
    for i in range(len(texto)):
            if(flag):#Se deja el espacio en el mensaje de salida
                if(texto[i]==" "):
                    new_message+=texto[i]
                else:
                    new_message+=dic[texto[i]]
            else:
                if(" " in alphabet):#El caso en el que el espacio sea parte del alfabeto
                    new_message+=dic[texto[i]]
                else:    
                    if(texto[i]!=" "):#Cuando el espacio no es del alfabeto
                        new_message+=dic[texto[i]]
    return new_message
