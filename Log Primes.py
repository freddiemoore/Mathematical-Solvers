#Need to revisit the objective here. Taken from "The art of computer programming" by Donald Knuth??

print("Type input here:")
n = int(input())
def log_primes(n):
    list_primes = []
    sum_log_primes = 0
    import math
    i = 2
    def test_prime(i):
        divisor = 2
        while divisor <= (i/2):
            if i % divisor == 0:
                return False
            else:
                divisor += 1
        return True
    m = len(list_primes)
    while m <= n:
        test_prime(i)
        x = test_prime(i)
        if x == True:
            list_primes.append(i)
            i += 1
            m = len(list_primes)
        else:
            i += 1
            m = len(list_primes)
    for c in list_primes:
        sum_log_primes = math.log(c) + sum_log_primes
    print(sum_log_primes)
    print(n)
    print(sum_log_primes / n)
log_primes(n)
