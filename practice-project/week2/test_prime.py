import pytest
from secondtask import isPrime

def assertPrime(n: int, isValidPrime: bool):
    assert isPrime(n) == isValidPrime

#checking prime
def testPrimeNums():
    assertPrime(5, True)
    assertPrime(3, True)

#checking non prime
def testNonPrime():
    assertPrime(4, False)
    assertPrime(10, False)

#checking edge cases
def testEdge():
    assertPrime(1, False)
    assertPrime(2, True)

#checking negative
def testNegative():
    assertPrime(-1, False)
    assertPrime(-50, False)

def testLarge():
    assertPrime(512343, False)
    assertPrime(1111, False)

#checking types
    
''' 
def testDiffTypes():
    with pytest.raises(TypeError):
        isPrime("Hello")
    with pytest.raises(TypeError):
        isPrime(True)
'''

