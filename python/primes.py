def prime_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


# Get amount of prime number up to N
n = 50 
primes = list(prime_sieve(n))
print(len(primes))
