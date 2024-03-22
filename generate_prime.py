import math
f = open('prime.txt', 'w')

def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for i in range(3,2**32):
    if prime(i):
        f.write(f" {i}")
        f.write("\n")
f.close()