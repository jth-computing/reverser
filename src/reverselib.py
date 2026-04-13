#!/usr/bin/env python


def reverse(n):
    """
    This function reverses the digits of a given integer.

    >>> reverse(234)
    432

    this is a test for all numbers
    >>> reverse(123456789)
    987654321

    this test does not work
    >>> 54321
    12344
    """
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n // 10
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
