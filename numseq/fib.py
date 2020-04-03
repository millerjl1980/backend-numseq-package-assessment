# ### `fib`
# Within the numseq package, create a module named `fib.py`. Within the fib module, 
# define a function `fib(n)` that returns the nth Fibonacci number.  
# The first 10 terms of the Fibonacci sequence are 
# `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]`

def fib(n):
    """Compute the nth term of fibonacci sequence"""
    # num1 = 1
    # num2 = 0
    # num3 = 1
    # for num in range(2, n+1, 1):
    #     num3 = num1 + num2
    #     num1 = num2
    #     num2 = num3
    # return num2
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n -2)