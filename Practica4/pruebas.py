from random import randint
from random import randrange

def concatInt(x, y):
    if(x==y and x == 0):
        return concatInt(randrange(10), y)
    return x*10+y

def nuevoNumero(anterior):
    nuevo = randrange(10)
    return concatInt(anterior,nuevo)

def generarNumero(size, numero=None):
    if(numero==None):
        numero = 0
    if(size>0):
        numero = generarNumero(size-1,nuevoNumero(numero))
    return numero

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if(size==None or size < 100):
        size=randrange(100,151)
    print(size)
    return generarNumero(size)

#################################PARTE 2#####################################

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    Si a r−1 !≡ mod n y a*(2**(j*r)) !≡ −1 mod n para toda j en el rango [0, s − 1], entonces n no es
    primo
    """
    for k in range(0,4):
        pareja = obtenSyR(n)
        if pruebasMillerRabbin(pareja[0],pareja[1],n):
            return True

    return False

'''
Funcion que verfica las dos condiciones para que el test de miller rabbin sea válido
'''
def pruebasMillerRabbin(r,s,n):
    if not esPar(n):
        a = randrange(1,n)                                  #1<a<n-1
        x = potenciaModular(a,r,n)                          # a^r (mod n)
        if esCongruente(x,1,n) or esCongruente(x,-1,n):
            return True #b0

        for j in range(0,s):
            x = potenciaModular(x,2,n)
            if esCongruente(x,-1, n):
                return True
            if esCongruente(x,1, n):
                return False
    return False

'''
Funcion que regresa True si n es par, False si es impar
'''
def esPar(n):
    return n % 2 == 0

'''
Funcion que regresa la operacion (x^y)%m
Algoritmo obtenido de https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
la funcion original se llama power
La funcion que usabamos
def potenciaModular(x,y,m):
    x = x % m
    res = x
    while y > 1:
        res = (res * x) % m
        y -=1
    return res

'''
def potenciaModular(x,y,p):
        # Initialize result
        res = 1
        # Update x if it is more than or
        # equal to p
        x = x % p
        while (y > 0):
            # If y is odd, multiply
            # x with result
            if (y & 1):  #AND con 1 regresa 1  si y es impar, 1 = True
                res = (res * x) % p
            # y must be even now
            y = y>>1; # y = y/2
            x = (x * x) % p

        return res

'''
Funcion que nos dice si hay una relacion de congrencia a ≡ b (mod n)
Ejemplo :print(esCongruente(5,1,11)) regresa True;
'''

def esCongruente(a,b,n):
    if (a-b)%n==0:
        return True
    return False

'''
Funcion que encuentra un par [r,s],
r y s tales que (n − 1) = r(2^s ) con r par impar.
Ejemplo : listaSyR(13) = [3,2]

'''
def obtenSyR(n):
    r = n - 1
    s = 0
    while (r % 2 == 0):
        r //= 2
        s +=1
    return [r,s]
print(miller_rabin(4))
print(miller_rabin(6))
print(miller_rabin(8))
print(miller_rabin(22))
print(miller_rabin(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096))
print(miller_rabin(139008452377144732764939786789661303114218850808529137991604824430036072629766435941001769154109609521811665540548899435521))
print(miller_rabin(139008452377144732764939786789661303114218850808529137991604824430036072629766435941001769154109609521811665540548899435521))
print(miller_rabin(86361685550944446253863518628003995711160003644362813850237034701685918031624270579715075034722882265605472939461496635969950989468319466936530037770580747746862471103668212890625))
print(miller_rabin(9838904645695721399467507393637950834772530843079566176626772344224146023275504290547965580877752204878078969621050913955161578722652608345125565299893441))
#print(miller_rabin(15485863))
#print(miller_rabin(941083981))


################################PARTE 3#########################################
def wilson(p):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.

    """
    if esCongruente(factorialModular(p-1,p),-1,p):
        return True
    return False
'''
Funcion
que regresa el factoial de n en modulo m !n % m

'''
def factorialModular(n,m):
    num = n
    while n>1:
        num = (num * (n-1))%m
        n=n-1
    return num



#print(wilson(13))
#print(wilson(12))
#print(wilson(9838904645695721399467507393637950834772530843079566176626772344224146023275504290547965580877752204878078969621050913955161578722652608345125565299893441))
print(factorialModular(5,1000))
