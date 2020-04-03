# ### `geo`
# Within the numseq package, create a module named `geo.py`. 
# Within this geo module, define 3 functions:

#  - `square(n)`

def square(n):
    """Returns the nth term of the numbers that can be arranged into square geometric shapes"""
    return n ** 2

#  - `triangle(n)` 

def triangle(n):
    """Returns the nth term of the numbers that can be arranged in triangular geometric shapes"""
    return (n*(n + 1)/2)


#  - `cube(n)`

def cube(n):
    """Returns the nth term of the numbers that can be arranged as symmetric cube shapes"""
    return n ** 3