def sort_letters(text):
    """
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """

    count_by_letter = {}

    for letter in text:
        # todo - help(dict.get), help(dict.setdefault)
        # todo - from collections import Counter
        if letter in count_by_letter:
            count_by_letter[letter] += 1
        else:
            count_by_letter[letter] = 1


    for index, letter in enumerate(text):
        if letter not in index_by_letter:
            index_by_letter[letter] = index

#     for letter, count in count_by_letter.items():
#         reversed_pairs.append((count, -index_by_letter[letter], letter))

    reversed_pairs = [
        (count, -index_by_letter[letter], letter)
        for letter, count in count_by_letter.items()
    ]

    reversed_pairs.sort(reverse=True)

#     result = []
#     for count, index, letter in reversed_pairs:
#         result.append(letter * count)

    # todo - list comprehension
    return ''.join([
        letter * count
        for count, _, letter in reversed_pairs
    ])


# todo  - enumerate
