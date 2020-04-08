class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)


#########################Falta comentar para que los usamos
######Son de esta pagina
#https://www.geeksforgeeks.org/implementation-affine-cipher/
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m