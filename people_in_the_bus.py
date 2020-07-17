def number(bus_stops):
    """
    >>> number([[10,0],[3,5],[5,8]])
    5
    >>> number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
    17
    >>> number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
    21
    >>> number([[0,0]])
    0
    """
    res = 0

    for stop in bus_stops:
        res = res + stop[0] - stop [1]
    return res


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()