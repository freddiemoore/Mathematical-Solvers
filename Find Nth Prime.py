print("Type Nth Prime")
n = int(input())
list_primes = []
def find_prime(n):
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
    print(list_primes[n-1])
    return list_primes[n-1]
find_prime(n)

#test change#















    







    
    





        
