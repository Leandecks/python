# Leandro Gridelli

primes = []

for number in range(2, int(input("Count until: ")) + 1):

    isPrime = True

    for prime in primes:
        if number % prime == 0:
            isPrime = False

    if isPrime:
        primes.append(number)

    print(f"{number} prime: {isPrime}")
