def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def isCoprime(a, b):
    if gcd(a,b) == 1:
        return True
    
    return False

def coprimeWith(a):
    for i in range(2, a):
        if isCoprime(a, i):
            return i

def generate_key(p,q):
    while(isPrime(a,b) == True and p*q < 2**32):
        n = p*q
        k = (p-1)*(q-1)
        e = coprimeWith(k)

