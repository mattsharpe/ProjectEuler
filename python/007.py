# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?
import datetime

def sieve_of_eratosthenes():
    primes = []
    discard = set()
    limit = 1000000

    for i in range(2, limit):
        if i in discard:
            continue

        primes.append(i)

        # now we've got a prime we add it's multiples to the discard set 
        # starting with it's square and counting up in multiples of i)
        for nonPrime in range(i*i, limit, i):
            discard.add(nonPrime)       

    return primes
   
    
start = datetime.datetime.now()
print(sieve_of_eratosthenes()[10000])
stop = datetime.datetime.now()
print(stop - start)