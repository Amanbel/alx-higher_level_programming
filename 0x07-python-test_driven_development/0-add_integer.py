#!/usr/bin/python3
"""function that adds two integers"""
def add_integer(a, b=98):
    """returns the sum of input values
    >>> add_integer(6, 'o')
	Traceback (most recent call last):
	TypeError: b must be an integer
	>>> add_integer('p', 7)
	Traceback (most recent call last):
	TypeError: a must be an integer
    >>> add_integer(9, 9)
    18
    >>> add_integer(2, 3)
    5
    >>> add_integer(9, 21)
    30
    >>> add_integer(-2, 15)
    13
    >>> add_integer(9, 'b')
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int)  and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
