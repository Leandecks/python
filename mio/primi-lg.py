# Leandro Gridelli

primes = []

for number in range(2, 100):

    isPrime = True

    for prime in primes:
        if number % prime == 0:
            isPrime = False

    if isPrime:
        primes.append(number)

    print(f"{number} prime: {isPrime}")
