#
# testlib.py
# A collection of test functions and classes for demonstration purposes.
#
"""
A collection of test functions and classes for demonstration purposes.
"""

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


class oneAtomState:
    """
    A class for holding and manipulating the quantum state of a single atom.

    Attributes
    ----------
    n, l, j, mj : int
        The state of the atom.
    q : int
        The Fourier component for Floquet state, default is 0.

    """
    n=0; l=0; j=0; mj=0
    q=0

    def __init__(self,n_in,l_in,j_in,mj_in,q_in = 0):
        """
        Initializes the oneAtomState with quantum numbers n, l, j, mj
        and an optional Fourier component q_in (default 0).

        Parameters
        ----------
        n_in : int
            Principal quantum number.
        l_in : int
            Azimuthal quantum number.
        j_in : float
            Total angular momentum quantum number.
        mj_in : float
            Magnetic quantum number.
        q_in : int, optional
            Fourier component for Floquet state (default is 0).
        
        """
        self.n = int(n_in); self.l = int(l_in); self.j = j_in; self.mj = mj_in
        self.q = int(q_in)
    
    def __str__(self):
        """ Returns a string representation of the oneAtomState. """
        return "({:.0f}, {:.0f}, {:.1f}, {:.1f}, q={:.0f})".format(self.n, self.l, self.j, self.mj, self.q)
    
    def tolist(self):
        """ Converts the state to a list representation (useful for saving to files). """
        return [self.n, self.l, self.j, self.mj, self.q]
    
    def __eq__(self, other):
        """  Checks if two oneAtomStates are equal based on their quantum numbers. """
        if self.n == other.n and self.l == other.l and self.j == other.j and self.mj == other.mj and self.q == other.q:
            return True
        else:
            return False


class twoAtomState:
    """
    A class for holding and manipulating the quantum state of a single atom.

    Attributes
    ----------
    n1, l1, j1, mj1 : int
        The state of the first atom.
    n2, l2, j2, mj2 : int
        The state of the second atom.
    q : int
        The Fourier component for Floquet state, default is 0.

    """
    n1=0; ll=0; jl=0; mjl=0
    n2=0; l2=0; j2=0; mj2=0
    q=0

    def __init__(self,n1_in,l1_in,j1_in,mj1_in,n2_in,l2_in,j2_in,mj2_in,q_in = 0):
        """
        Initializes the twoAtomState with quantum numbers for two atoms and a
        Fourier component q_in (default 0).

        Parameters
        ----------
        n1_in, l1_in, j1_in, mj1_in : int
            Quantum numbers for the first atom.
        n2_in, l2_in, j2_in, mj2_in : int
            Quantum numbers for the second atom.
        q_in : int, optional
            Fourier component for Floquet state (default is 0).
        
        """
        self.n1 = int(n1_in); self.l1 = int(l1_in); self.j1 = j1_in; self.mj1 = mj1_in
        self.n2 = int(n2_in); self.l2 = int(l2_in); self.j2 = j2_in; self.mj2 = mj2_in
        self.q = int(q_in)

    # Call as twoAtomState.fromOneAtomStates(s1, s2) where s1, s2 are oneAtomStates
    # Returns the relevant two-atom states
    @classmethod
    def fromOneAtomStates(cls, s1, s2):
        """ 
        Creates a twoAtomState from two oneAtomStates. 

        Parameters
        ----------
        s1, s2 : oneAtomState
            The one-atom states to combine into a two-atom state.

        Returns
        -------
        twoAtomState
            A new twoAtomState object created from the provided oneAtomStates.

        Raises
        ------
        Exception
            If the q values of the two states do not match.
        """
        if (s1.q != s2.q):
            raise Exception("The q values of the states must match.")
        return cls(s1.n, s1.l, s1.j, s1.mj, s2.n, s2.l, s2.j, s2.mj, s1.q)
    
    def __str__(self):
        """ Returns a string representation of the twoAtomState. """
        return "(({:.0f}, {:.0f}, {:.1f}, {:.1f}), ({:.0f}, {:.0f}, {:.1f}, {:.1f}), q={:.0f})".format(self.n1, self.l1, self.j1, self.mj1, self.n2, self.l2, self.j2, self.mj2, self.q)
    
    def tolist(self):
        """ Converts the two-atom state to a list representation. """
        return [self.n1, self.l1, self.j1, self.mj1, self.n2, self.l2, self.j2, self.mj2, self.q]
    
    def __eq__(self, other):
        """ Checks if two twoAtomStates are equal based on their quantum numbers. """
        if self.n1 == other.n1 and self.l1 == other.l1 and self.j1 == other.j1 and self.mj1 == other.mj1 and self.n2 == other.n2 and self.l2 == other.l2 and self.j2 == other.j2 and self.mj2 == other.mj2 and self.q == other.q:
            return True
        else:
            return False
