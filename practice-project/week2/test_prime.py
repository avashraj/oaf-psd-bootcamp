from secondtask import isPrime

def assertPrime(n):
    assert isPrime(n) == True

def assertNotPrime(n):
    assert isPrime(n) == False

def testPrimeNums():
    assertPrime(5)
    assertPrime(3)
    assertPrime(2)

def testNonPrime():
    assertNotPrime(4)
    assertNotPrime(1)