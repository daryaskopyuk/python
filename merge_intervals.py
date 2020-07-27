def sort_intervals(el):
    return el[0]

def merge(intervals):
    """
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge([[1, 5], [0, 0]])
    [[0, 0], [1, 5]]
    >>> merge([[2, 8], [1, 15], [17, 20]])
    [[1, 15], [17, 20]]
    """

    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=sort_intervals)

    for index, interval in enumerate(intervals):
        current = intervals[index]
        next = intervals[index + 1] if index + 1 < len(intervals) else False

        if current and next and current[1] >= next[0]:
            current[0] = min(current[0], next[0])
            current[1] = max(current[1], next[1])
            intervals.pop(index + 1)
            index -= 1

    return intervals


merge([[1, 3], [15, 18], [2, 6], [8, 10]])


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()