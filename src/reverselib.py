#!/usr/bin/env python


def reverse(n):
    r = 0
    while n >= 1:
        r = r * 10 + n % 10
        n = n // 10
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
