def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# Algorithme d'Euclide étendu
## y = b, pas négatif
def extended_gcd(e, k):
   if k == 0: return e, 1, 0
  
   gcd, x1, y1 = extended_gcd(k, e % k)
   x = y1
   y = x1 - (e // k) * y1
   if(y > 0):
       y = 0 - y
       x = 0 - x
   return gcd, x, y


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
            if i < a:
                return i

def generate_key(p,q):
    while(isPrime(p,q) == True and p*q < 2**32):
        n = p*q
        k = (p-1)*(q-1)
        e = coprimeWith(k) 
        d, b = extended_gcd(e,k)
        return n, e, d

def encrypt(message, e, n):
    return (message**e) % n

def decrypt(hiddenMess, d, n):
    return (hiddenMess**d) % n    
     

