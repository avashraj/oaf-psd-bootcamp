
def isPrime(n):
    if not isinstance(n, int):
        raise TypeError
    if n > 1:
        for i in range(2,int(n/2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


