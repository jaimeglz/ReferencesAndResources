def fib(n):
    """Returns nth Fibonacci number
    Use:
        fib(n)
        
    Assumes n is an int >= 0
    """
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
