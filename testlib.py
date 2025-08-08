import time


def testFunc1():
    t0 = time.time()
    time.sleep(1.2)
    t1 = time.time()
    print("{:.2f} s".format(t1-t0))


def testAdd(a, b):
    """  Adds two numbers and returns the result. """
    return a+b


def testSub(a, b):
    """  Subtracts two numbers and returns the result. """
    return a-b


def testMult(a, b):
    """  Multiplies two numbers and returns the result. """
    return a*b


def testDiv(a, b):
    """  Divides two numbers and returns the result. """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a/b


def testFib(n):
    """  Returns the nth Fibonacci number. """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
