"""
Mini examples of recursive functions
"""
def sum_list(lists):
    """
    Given an arbitrarily levelled list, return the sum of all its elements
    >>> sum_list([1,[2,[3,4],5],6])
    21
    >>> sum_list([1,2,3])
    6

    @param lists:
    @return:
    """
    # if isinstance(lists, int):
    #     return lists
    # else:
    #     return sum([sum_list(x) for x in lists])
    pass


def max_list(lists):
    """
    Given an arbitrarily levelled list, return the max of all its elements
    >>> max_list([1,[2,[3,4],5],6])
    6
    >>> sum_list([1,2,3])
    3

    @param lists:
    @return:
    """
    # if isinstance(lists, int):
    #     return lists
    # else:
    #     return max([max_list(x) for x in lists])
    pass


def factorial(n):
    # # Base case
    # if n == 0:
    #     return 1
    # # Recursive Case
    # else:
    #     return n*factorial(n-1)
    pass


def factorial_iterative(n):
    """
    Iteratively compute the factorial
    :param n: the value we are computing the factorial of
    :return: n!
    """
    # fact = 1
    # for i in range(1,n + 1):
    #     fact = i*fact
    # return fact
    pass


def fibonacci(n):
    # # Base case
    # if n == 1 or n == 0:
    #     return 1
    # # Recursive Case
    # else:
    #     return fibonacci(n - 1 ) + fibonacci(n - 2)
    pass

def pizzaParty(n):
    """
    How many slices of pizza do we need if every person will eat double
    what the one behind them ate and exactly what the person two behind
    them ate.
    Assume the first person will always eat 1 slice
    :return:
    """

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return 2*pizzaParty(n - 1) + pizzaParty(n - 2)
    pass



def recursive(variable):
    # The Base Case:
    # if (variable ...)
        # the simplest form of our variable
        # Where return of recursive(variable) is independently defined
    # (else)
        # return recursive( ... )
    pass


