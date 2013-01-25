_primeslist = [2]

def sieve():
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            yield start

        start += 1

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True
    
