def generate_primes():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

primes = generate_primes()

for i, prime in enumerate(primes):
    if i >= 10:
        break
    print(prime)
