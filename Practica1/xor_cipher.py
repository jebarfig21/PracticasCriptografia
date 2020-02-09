def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
    # Recorremos cada letra del mensaje, con la operacion ord() obtenemos un integer que representa al caracter en Unicode y finalmente hacemos un xor con la
    #operacion ^ y el 1 para cambiar en bit los 0's a 1's y los 1's a 0's
    cifrado = "";
    for i in range(len(message)): 
        cifrado = (cifrado + chr(ord(message[i]) ^ 1));
    return cifrado; 

"""
Descifra el mensaje recuperando el texto plano siempre y cuando haya sido cifrado con XOR.
Parámetro:
cryptotext -- el mensaje a descifrar.
"""
def decipher(criptotext):
    # Aplicamos la misma operacion que utiizamos para cifrar y asi revertir los 0's a 1's y los 1's a 0's
    return cipher(criptotext); 
   
