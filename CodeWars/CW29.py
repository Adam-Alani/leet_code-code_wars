import itertools
class Primes:
    @staticmethod
    def primes():
        numbers = itertools.count(2)
        while True:
            p = numbers.next()
            numbers = itertools.ifilter(lambda x, p=p: x % p, numbers)
            yield p