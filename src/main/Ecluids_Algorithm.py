def Ecluids(n):
    primes = []
    sieve = [True] * (n + 1)  
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)  # p is prime
            for j in range(p * p, n + 1, p):
                sieve[j] = False 

    return primes

n = 30  # Replace with your desired value of 'n'
prime_list = Ecluids(n)
print(prime_list)