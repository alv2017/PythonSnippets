import math

def is_prime(n):
    for i in range( 2, int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            return False
    return True

def prime_factors(n, factors=None, start = 2):
    if not factors:
        factors = []
    if n == 1:
        return factors
    if is_prime(n):
        factors.append(n)
        return factors
    for i in range(start, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n = n // i
            else:
                return prime_factors(n, factors, start = i + 1)            

if __name__=='__main__':
    for i in range(8990, 9000):
        N = i
        pf = prime_factors(N)
        print("Prime Factors of {0}:".format(N))
        print( pf )
        