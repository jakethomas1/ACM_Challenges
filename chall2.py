import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
# Set to store checked primes
checked_primes = set(primes)

def is_prime(number):
    # Return True if the number is in the checked primes set
    if number in checked_primes:
        return True
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for prime in primes:
        if prime * prime > number:
            break
        if number % prime == 0:
            return False

    primes.append(number)
    checked_primes.add(number)
    return True

#Write: k - 2n^2 = p, outerloop k, inner loop n... check there is a solution for all values of k
#Not sure how prime check should occur, need fast method.

def findN(k): #for k-2n^2 = p; given k is natural number > 1, n is some integer, p is prime
    #Note negative numbers are redundant solution for n, check either positive or negative
    n = 0
    while(True):
        if(is_prime(k - 2 * n**2)):
            return n
        n += 1
        if(n > int(math.sqrt(k / 2))):
            return (n if n==1 else None)


for i in range(1, 1000000, 2):
    if(findN(i) is None): print(i)


#1. 56423
#2. 33
#3. 45642112
#4. 142352322