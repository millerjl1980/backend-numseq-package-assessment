# ### `prime`
# Finally, create a module named `prime.py` within the numseq package. Define the following functions:
#  - `primes(n)`:  Returns a list of all prime numbers less than n
#  - `is_prime(m)` : Returns a boolean indicating whether `m` is a prime number
import math

def is_prime(n):
    """Returns a boolean indicating whether `m` is a prime number"""
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for num in range(3, 1 + max_divisor, 2):
        if n % num == 0:
            return False
    return True

def primes(n):
    """Returns a list of all prime numbers less than n"""
    primes = []
    for num in range(1+n):
        if is_prime(num):
            primes.append(num)
    return primes



