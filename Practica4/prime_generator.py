from random import randint
from random import randrange

####################################EJERCICIO 1#################################
'''
Funcion que "Concatena" dos numeros, es importante recalcar que bajo nuestra
lógica del problema, 0<=y<=9 siempre

Ejemplo concatInt(5189,5), va a regresar el entero 51895
'''
def concatInt(x, y):
    if(x==y and x == 0):
        return randrange(10)
    return x*10+y

'''
Funcion que va expandir el numero pasado como parametro n en una unidad,
esta nueva unidad es aleatoria

Ejemplo nuevoNumero(550), va a regresar 550a, donde a = [0,9]
'''
def nuevoNumero(n):
    return concatInt(n,randrange(10))

'''
Funcion que generar un numero aleatorio de tamaño size, el parametro numero se
usa para ir guardando el numero generado de manera recursiva

Ejemplo generarNumero(5), va a regresar un entero abcde, donde a,b,c,d,e = [0,9]
'''
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
    return generarNumero(size)


####################################EJERCICIO 2#################################

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    for k in range(0,4):
        pareja = obtenSyR(n)
        if pruebasMillerRabbin(pareja[0],pareja[1],n):
            return True

    return False

'''
Funcion que verfica las dos condiciones para que el test de miller rabbin sea válido
basado en el algoritmo descrito en :
https://www.youtube.com/watch?v=qdylJqXCDGs
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
Ejemplo esPar(8) ->True
'''
def esPar(n):
    return not n & 1

'''
Funcion que regresa la operacion (x^y)%m
Algoritmo(codigo) obtenido de https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
la funcion original se llama power
La funcion que usabamos
def potenciaModular(x,y,m):
    x = x % m
    res = x
    while y > 1:
        res = (res * x) % m
        y -=1
    return res
El problema se encontraba en esta funcion ya que nuestra funcion original es O(n) mientras que esta funcion es
O(log n)
'''
def potenciaModular(x,y,p):
        # Initialize result
        res = 1;
        # Update x if it is more than or
        # equal to p
        x = x % p;
        while (y > 0):
            # If y is odd, multiply
            # x with result
            if not esPar(y):  #AND con 1 regresa 1  si y es impar, 1 = True
                res = (res * x) % p
            # y must be even now
            y = y>>1; # y = y/2
            x = (x * x) % p

        return res;

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


####################################EJERCICIO 3#################################
def wilson(p):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.

    """
    if not esPar(p):
        if esCongruente(factorialModular(p-1,p),-1,p):
            return True

    return False

'''
def factorialModular(n,m):
    if(n == 0):
        return 1
    else:
        n = (n * factorialModular(n-1,m))%m
        return n
'''
def factorialModular(n,m):
    num = n
    while n>1:
        num = (num * (n-1))%m
        n=n-1
    return num
