"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):
    if n < 3:
        return 1
    return get_fib(n - 1) + get_fib(n - 2)
