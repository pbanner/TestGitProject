import time


def testFunc1():
    """ A simple delay function. """
    t0 = time.time()
    time.sleep(1.2)
    t1 = time.time()
    print("{:.2f} s".format(t1-t0))


def testFunc2():
    """ A simple print function. """
    print("Hello world!")


def testFunc3():
    """ A simple print function. """
    print("Hello derp!")


def testFunc4():
    """  A placeholder function. """
    print("This is function 4")


def testFunc5():
    """  Another placeholder function. """
    print("This is function 5")


def testFunc7():
    """  Yet another placeholder function. """
    print("This is function 7")


def testFunc6():
    """  Yet another placeholder function. """
    print("This is function 6")


def testAdd(a, b):
    """
    Adds two numbers and returns the result.

    Parameters
    ----------
    a, b : int or float
        The numbers to be added.

    Returns
    -------
    int or float
        The sum of the two numbers.
    """
    return a+b


def testSub(a, b):
    """  Subtracts two numbers and returns the result. """
    return a-b


def testMult(a, b):
    """  Multiplies two numbers and returns the result. """
    return a*b


def testFib(n):
    """
    Returns the nth Fibonacci number. For n < 0, returns 0.
    If n == 0, returns 0; if n == 1, returns 1.
    For n > 1, computes the Fibonacci number iteratively.

    Parameters
    ----------
    n : int
        The position in the Fibonacci sequence (0-indexed).

    Returns
    -------
    int
        The nth Fibonacci number. 
    
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def testFactorial(n):
    """ 
    Returns the factorial of n.

    Parameters
    ----------
    n : int
        The number for which the factorial is to be calculated.

    Returns
    -------
    int
        The factorial of n.

    Raises
    ------
    ValueError
        If n is negative, as factorial is not defined for negative numbers.
    
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def testDiv(a, b):
    """  Divides two numbers and returns the result. """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a/b
