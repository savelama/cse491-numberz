# Implementation of Eratosthenes' Sieve functionality using Python's iterator functionality

class adder(object):
    def __init__(self):
        self._primeslist = [2]
        self.start = self._primeslist[-1] + 1

    def __iter__(self):
        return self

    def _is_prime(self, primes, n):
        for i in primes:
            if n % i == 0:
                return False
        return True

    def next(self):
        while 1:
            if self._is_prime(self._primeslist, self.start):
                self._primeslist.append(self.start)
                return self.start

            self.start += 1
